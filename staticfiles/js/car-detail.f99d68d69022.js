document.addEventListener("DOMContentLoaded", function () {
  // setup tooltip bootstrap
  const tooltipTriggerList = document.querySelectorAll(
    '[data-bs-toggle="tooltip"]'
  );
  const tooltipList = [...tooltipTriggerList].map(
    (tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl)
  );

  /**
   * like and dislike using ajax
   */
  document.querySelectorAll(".like-btn").forEach(function (btn) {
    btn.addEventListener("click", function () {
      const carId = this.dataset.carId;

      fetch(`/cars/${carId}/like/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
            .value,
          "Content-Type": "application/json"
        }
      })
        .then((res) => res.json())
        .then((data) => {
          if (!data.error) {
            const countSpan = document.getElementById(`like-count-${carId}`);
            countSpan.textContent = data.total_likes;
            const labelSpan = document.getElementById(`like-label-${carId}`);
            labelSpan.textContent = data.liked ? "liked" : "like";
            this.classList.toggle("active", data.liked);
            this.blur();
            showToast(
              `You have ${data.liked ? "liked" : "disliked"} this car`,
              "text-bg-success"
            );
          } else {
            showToast(data.error, "text-bg-danger");
          }
        })
        .catch((err) => {
          showToast(`Error while liking this car, ${err}`, "text-bg-danger");
          console.error("Error:", err);
        });
    });
  });

  /**
   * add a new comment using ajax
   */
  var selectedCommentId;
  var commentForm = document.getElementById("comment-form");
  if (commentForm) {
    commentForm.addEventListener("submit", async function (e) {
      e.preventDefault();
      const textarea = this.content;
      if (!textarea.value.trim()) {
        showToast("Comment cannot be empty or just spaces.", "text-bg-danger");
        textarea.focus();
        return;
      }
      const formData = new FormData(this);
      const res = await fetch("/comments/add/", {
        method: "POST",
        headers: { "X-CSRFToken": formData.get("csrfmiddlewaretoken") },
        body: formData
      });
      try {
        const data = await res.json();
        if (!res.ok) {
          showToast(res.statusText || "Something went wrong", "text-bg-danger");
          throw new Error(`HTTP error ${res.statusText || "Something went wrong"}`);
        } else {
          const noCommentsElement = document.getElementById("no-comments");
          if (noCommentsElement) {
            noCommentsElement.remove();
          }
          const commentsCount = document.getElementById("comments-count");
          if (commentsCount) {
            commentsCount.innerText = `( ${data.count} comments)`;
          }
          const image_url = data.image_url;
          // create element to add the new comment to comments box
          const newComment = `
          <div class="comment" id="comment-${data.id}">
          <div class="d-inline">
            <img src="${image_url}" class="rounded-circle" width="40" alt="user profile image" loading="lazy">
            <strong>${data.user}</strong>
             <div class="btn-group dropend comment-actions">
                <button type="button" class="btn text-primary dropdown-toggle" 
                        data-bs-toggle="dropdown"
                        aria-label="click to edit our delete this comment"
                        aria-expanded="false">
                        <i class="fa-solid fa-gear"></i>
                </button>
                <ul class="dropdown-menu">
                  <li>
                    <button class="dropdown-item edit-btn"
                            aria-label="click to edit this comment"
                            id="edit-btn-${data.id}"
                            data-id="${data.id}">
                        Edit
                    </button>
                  </li>
                  <li>
                  <hr class="dropdown-divider">
                  </li>
                  <li>
                    <button class="dropdown-item delete-btn"
                            data-bs-toggle="modal" data-bs-target="#confirm-modal"
                            aria-label="click to delete this comment"
                            id="delete-btn-${data.id}"
                            data-id="${data.id}">
                              Delete
                    </button>
                  </li>
                </ul>
              </div>
            </div>
            <div class="comment-content" id="comment-content-${data.id}">
              <p class="comment-text">
                   ${data.content}
                  <br>
                  <small class="comment-time">
                    ${data.created}
                  </small>
              </p>
              <form class="comment-form d-none">
               <div class="d-flex flex-column flex-wrap">
                  <label for="input-comment-${data.id}" class="form-label">Your Comment</label>
                  <textarea id="input-comment-${data.id}" class="form-control my-3 edit-input" required>${data.content}</textarea>
                </div>
                <button class="btn btn-sm action-button-secondary save-edit"
                        aria-label="click to update the comment"
                        data-id="${data.id}"
                        id="save-btn-${data.id}">Save</button>
                <button class="btn btn-sm action-button-accent cancel-edit"
                        data-id="${data.id}"
                        aria-label="click to cancel comment editing" 
                        id="cancel-btn-${data.id}">Cancel</button>
              </form>
            </div>
          </div>`;
          // add event listeners to action buttons for new comment
          document
            .getElementById("comments-list")
            .insertAdjacentHTML("beforeend", newComment);
          const editBtn = document.getElementById(`edit-btn-${data.id}`);
          editBtn.addEventListener("click", function () {
            handleEdit(editBtn);
          });
          const cancelBtn = document.getElementById(`cancel-btn-${data.id}`);
          cancelBtn.addEventListener("click", function (e) {
            e.preventDefault();
            handelCancelEditing(cancelBtn);
          });
          const saveEditingBtn = document.getElementById(`save-btn-${data.id}`);
          saveEditingBtn.addEventListener("click", async function (e) {
            e.preventDefault();
            handelSaveEditing(saveEditingBtn);
          });
          const deleteBtn = document.getElementById(`delete-btn-${data.id}`);
          deleteBtn.addEventListener("click", function () {
            selectedCommentId = deleteBtn.dataset.id;
          });
          // scroll down the comments box
          const commentBox = document.querySelector(".scroll-box");
          commentBox.scrollTop = commentBox.scrollHeight;

          // reset the comment textarea
          this.reset();
          showToast("You have commented on this car post", "text-bg-success");
        }
      } catch (error) {
        showToast(error, "text-bg-danger");
        console.error("Error:", error);
      }
    });
  }

  /**
   *  add event listener to comment edit button
   *  */
  document.querySelectorAll(".edit-btn").forEach((btn) => {
    btn.addEventListener("click", function () {
      handleEdit(btn);
    });
  });

  /**
   *  handel the comment edit action
   *  */
  function handleEdit(btn) {
    const parent = document.getElementById(`comment-content-${btn.dataset.id}`);
    parent.querySelector(".comment-form").classList.remove("d-none");
    parent.querySelector(".comment-text").classList.add("d-none");
    btn.classList.add("d-none");
  }

  /**
   *  add event listener to cancel button to cancel comment editing
   * */
  document.querySelectorAll(".cancel-edit").forEach((btn) => {
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      handelCancelEditing(btn);
    });
  });

  /**
   *  handel the comment cancel editing action
   * */
  function handelCancelEditing(btn) {
    const parent = document.getElementById(`comment-content-${btn.dataset.id}`);
    parent.querySelector(".comment-form").classList.add("d-none");
    parent.querySelector(".comment-text").classList.remove("d-none");
    document
      .getElementById(`edit-btn-${btn.dataset.id}`)
      .classList.remove("d-none");
  }

  /**
   *  add event listener to update comment
   * */
  document.querySelectorAll(".save-edit").forEach((btn) => {
    btn.addEventListener("click", async function (e) {
      e.preventDefault();
      handelSaveEditing(btn);
    });
  });

  /**
   *  handel the update comment
   * */
  async function handelSaveEditing(btn) {
    const commentId = btn.dataset.id;
    const parent = document.getElementById(`comment-content-${commentId}`);
    const newContent = parent.querySelector(".edit-input").value;
    if (!newContent || newContent.trim() === "") {
      showToast("can not save empty string", "text-bg-danger");
      return;
    }
    const formData = new FormData();
    formData.append("content", newContent);
    loaderToggel(false);
    const res = await fetch(`/comments/${commentId}/edit/`, {
      method: "POST",
      headers: {
        "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
          .value
      },
      body: formData
    });
    try {
      const data = await res.json();
      if (!res.ok) {
        showToast(res.statusText || "Something went wrong", "text-bg-danger");
        throw new Error(`HTTP error ${res.statusText || "Something went wrong"}`);
      } else {
        const newContent = `${data.content}<br>
        <small class="comment-time">
             ${data.created}
        </small>`;
        parent.querySelector(".comment-text").innerHTML = newContent;
        parent.querySelector(".comment-text").classList.remove("d-none");
        parent.querySelector(".comment-form").classList.add("d-none");
        document
          .getElementById(`edit-btn-${commentId}`)
          .classList.remove("d-none");
        showToast("Comment was updated successfully.", "text-bg-success");
      }
    } catch (error) {
      showToast(error, "text-bg-danger");
      console.error("Error:", error);
    } finally {
      loaderToggel(true);
    }
  }

  /**
   * add event listener to delete button
   */
  document.querySelectorAll(".delete-btn").forEach((btn) => {
    btn.addEventListener("click", function () {
      // selectedCommentId determines the id of comment to be deleted
      selectedCommentId = this.dataset.id;
    });
  });

  // when the delete is confirmed then call delete_comment url
  document
    .getElementById("confirmDelete")
    .addEventListener("click", function () {
      if (!selectedCommentId) return;
      loaderToggel(false);

      fetch(`/comments/${selectedCommentId}/delete/`, {
        method: "DELETE",
        headers: {
          "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
            .value,
          "X-Requested-With": "XMLHttpRequest"
        }
      })
        .then((res) => {
          if (!res.ok) {
            closeModal();
            showToast(
              `Couldn't delete the comment, ${res.statusText}`,
              "text-bg-danger"
            );
            throw new Error(`HTTP error ${res.status}`);
          }
          return res.json();
        })
        .then((data) => {
          // remove comment from comments list
          document.getElementById(`comment-${selectedCommentId}`).remove(false);
          // reduce number of comments after deleting
          const comments = document.querySelectorAll(".comment");
          const commentsCount = document.getElementById("comments-count");
          commentsCount.innerText = `( ${comments.length} comments)`;
          if (comments.length === 0) {
            const commentsList = document.getElementById("comments-list");
            commentsList.innerHTML = `<span id="no-comments">No Comments</span>`;
          }
          // closeModal
          closeModal();
          // show success message
          showToast("Comment deleted successfully!", "text-bg-success");
        })
        .catch((error) => {
          showToast(error, "text-bg-danger");
          console.error("Error:", error);
        })
        .finally(() => {
          loaderToggel(true);
        });
    });

  /**
   *  show success message as a bootstrap toast
   *  */
  function showToast(message, bgColorClass) {
    const toastEl = document.getElementById("message-toast");

    // Get the current scroll position and viewport size
    const scrollTop = window.scrollY;
    const viewportHeight = window.innerHeight;
    const toastHeight = toastEl.offsetHeight;

    // Position: center of the visible viewport
    toastEl.style.top = `${scrollTop + (viewportHeight - toastHeight) / 2}px`;
    toastEl.style.right = `5%`;

    // Add bg color class
    toastEl.classList.forEach((cls) => {
      if (cls.startsWith("text-bg-")) {
        toastEl.classList.remove(cls);
      }
    });
    toastEl.classList.add(bgColorClass);

    // Display the message
    const content = document.querySelector("#message-toast .toast-body");
    content.innerText = message;
    const btoast = bootstrap.Toast.getOrCreateInstance(toastEl, {
      delay: 4500
    });
    btoast.show();
    setTimeout(() => btoast.hide(), 5000);
  }

  //close the confirmation modal
  function closeModal() {
    const modal = bootstrap.Modal.getInstance(
      document.getElementById("confirm-modal")
    );
    modal.hide();
  }

  /**
   * close modal
   * */
  function closeModal() {
    const modal = bootstrap.Modal.getInstance(
      document.getElementById("confirm-modal")
    );
    modal.hide();
  }

  /**
   * loader show/hide
   * */
  function loaderToggel(hide) {
    const loader = document.getElementById("loader");
    const modal = document.getElementById("confirm-modal");
    loader.style.visibility = hide ? "hidden" : "visible";
    modal.style.zIndex = hide ? "1100" : "10";
  }
});
