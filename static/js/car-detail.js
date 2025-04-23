document.addEventListener("DOMContentLoaded", function () {
  // setup tooltip bootstrap
  const tooltipTriggerList = document.querySelectorAll(
    '[data-bs-toggle="tooltip"]'
  );
  const tooltipList = [...tooltipTriggerList].map(
    (tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl)
  );

  //
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
          const countSpan = document.getElementById(`like-count-${carId}`);
          countSpan.textContent = data.total_likes;
          const labelSpan = document.getElementById(`like-label-${carId}`);
          labelSpan.textContent = data.liked ? "liked" : "like";
          this.classList.toggle("active", data.liked);
          this.blur();
        })
        .catch((err) => console.error("Error:", err));
    });
  });

  // add comment
  var selectedCommentId;
  var commentForm = document.getElementById("comment-form");
  if (commentForm) {
    commentForm.addEventListener("submit", function (e) {
      e.preventDefault();
      const formData = new FormData(this);

      fetch("/comments/add/", {
        method: "POST",
        headers: { "X-CSRFToken": formData.get("csrfmiddlewaretoken") },
        body: formData
      })
        .then((res) => {
          if (!res.ok) {
            alert(res.statusText);
            throw new Error(`HTTP error ${res.status}`);
          }
          return res.json();
        })
        .then((data) => {
          const noCommentsElement = document.getElementById("no-comments");
          if (noCommentsElement) {
            noCommentsElement.remove();
          }
          const commentsCount = document.getElementById("comments-count");
          if (commentsCount) {
            commentsCount.innerText = `( ${data.count} comments)`;
          }
          var imagesrc = document
            .getElementById("profile-placeholder")
            .getAttribute("src");
          image_url =
            data.image_url == "placeholder" ? imagesrc : data.image_url;
          const newComment = `
          <div class="comment" id="comment-${data.id}">
          <div>
            <img src="${image_url}" class="rounded-circle" width="40">
            <strong>${data.user}</strong>
             <span class="btn-group dropend comment-actions">
                <button type="button" class="btn text-primary dropdown-toggle" data-bs-toggle="dropdown"
                        aria-expanded="false">
                        <i class="fa-solid fa-gear"></i>
                </button>
                <ul class="dropdown-menu">
                  <li>
                    <button class="dropdown-item edit-btn"
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
                            id="delete-btn-${data.id}"
                            data-id="${data.id}">
                              Delete
                    </button>
                  </li>
                </ul>
              </span>
            </div>
            <div class="comment-content" id="comment-content-${data.id}">
              <p class="comment-text">
                   ${data.content}
                  <br>
                  <small class="comment-time">
                    ${data.created}
                  </small>
              </p>
              <textarea class="form-control my-3 edit-input d-none">${data.content}</textarea>
              <button class="btn btn-sm action-button-secondary save-edit d-none"
                      data-id="${data.id}"
                       id="save-btn-${data.id}">Save</button>
              <button class="btn btn-sm action-button-accent cancel-edit d-none"
                      data-id="${data.id}"
                       id="cancel-btn-${data.id}">Cancel</button>
            </div>
          </div>`;
          document
            .getElementById("comments-list")
            .insertAdjacentHTML("beforeend", newComment);
          const editBtn = document.getElementById(`edit-btn-${data.id}`);
          editBtn.addEventListener("click", function () {
            handleEdit(editBtn);
          });
          const cancelBtn = document.getElementById(`cancel-btn-${data.id}`);
          cancelBtn.addEventListener("click", function () {
            handelCancelEditing(cancelBtn);
          });
          const saveEditingBtn = document.getElementById(`save-btn-${data.id}`);
          saveEditingBtn.addEventListener("click", function () {
            handelSaveEditing(saveEditingBtn);
          });
          const deleteBtn = document.getElementById(`delete-btn-${data.id}`);
          deleteBtn.addEventListener("click", function () {
            selectedCommentId = deleteBtn.dataset.id;
          });

          this.reset();
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });
  }

  // edit comment
  document.querySelectorAll(".edit-btn").forEach((btn) => {
    btn.addEventListener("click", function () {
      handleEdit(btn);
    });
  });

  function handleEdit(btn) {
    const parent = document.getElementById(`comment-content-${btn.dataset.id}`);
    parent.querySelector(".comment-text").classList.add("d-none");
    parent.querySelector(".edit-input").classList.remove("d-none");
    parent.querySelector(".save-edit").classList.remove("d-none");
    parent.querySelector(".cancel-edit").classList.remove("d-none");
    btn.classList.add("d-none");
  }

  document.querySelectorAll(".cancel-edit").forEach((btn) => {
    btn.addEventListener("click", function () {
      handelCancelEditing(btn);
    });
  });
  
  function handelCancelEditing(btn) {
    const parent = document.getElementById(`comment-content-${btn.dataset.id}`);
      parent.querySelector(".comment-text").classList.remove("d-none");
      parent.querySelector(".edit-input").classList.add("d-none");
      parent.querySelector(".save-edit").classList.add("d-none");
      parent.querySelector(".cancel-edit").classList.add("d-none");
      document
        .getElementById(`edit-btn-${btn.dataset.id}`)
        .classList.remove("d-none");
  }

  document.querySelectorAll(".save-edit").forEach((btn) => {
    btn.addEventListener("click", function () {
       handelSaveEditing(btn);
    });
  });

  function handelSaveEditing(btn) {
    const commentId = btn.dataset.id;
    const parent = document.getElementById(`comment-content-${commentId}`);
    const newContent = parent.querySelector(".edit-input").value;
    const formData = new FormData();
    formData.append("content", newContent);
    loaderToggel(false);
    fetch(`/comments/${commentId}/edit/`, {
      method: "POST",
      headers: {
        "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
          .value
      },
      body: formData
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.success) {
          const newContent = `${data.content}<br>
                              <small class="comment-time">
                                   ${data.created}
                              </small>`;
          parent.querySelector(".comment-text").innerHTML = newContent;
          parent.querySelector(".comment-text").classList.remove("d-none");
          parent.querySelector(".edit-input").classList.add("d-none");
          parent.querySelector(".save-edit").classList.add("d-none");
          parent.querySelector(".cancel-edit").classList.add("d-none");
          document
            .getElementById(`edit-btn-${commentId}`)
            .classList.remove("d-none");
        }
      })
      .finally(() => {
        // loaderToggel function is defined in main.js
        loaderToggel(true);
        showToast("Comment was updated successfully.");
      });
  }

  // selectedCommentId determines the id of comment to be deleted
  
  document.querySelectorAll(".delete-btn").forEach((btn) => {
    btn.addEventListener("click", function () {
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
            alert(res.statusText);
            throw new Error(`HTTP error ${res.status}`);
          }
          return res.json();
        })
        .then((data) => {
          if (data.success) {
            // remove comment from comments list
            document
              .getElementById(`comment-${selectedCommentId}`)
              .remove(false);
            // reduce number of comments after deleting
            const comments = document.querySelectorAll(".comment");
            const commentsCount = document.getElementById("comments-count");
            commentsCount.innerText = `( ${comments.length} comments)`;
            if (comments.length === 0) {
              const commentsList = document.getElementById("comments-list");
              commentsList.innerHTML = `<span id="no-comments">No Comments</span>`;
            }
            // closeModal function is defined in main.js
            closeModal();
            // show success message
            showToast("Comment deleted successfully!");
          } else {
            alert("Error deleting car");
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        })
        .finally(() => {
          // loaderToggel function is defined in main.js
          loaderToggel(true);
        });
    });

  // show success message as a bootstrap toast
  function showToast(message) {
    const toast = document.createElement("div");
    toast.className =
      "toast align-items-center text-bg-success border-0 bottom-fixed center-0 end-0 m-3";
    toast.role = "alert";
    toast.innerHTML = `
        <div class="d-flex">
          <div class="toast-body">${message}</div>
          <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
        </div>`;
    document.body.appendChild(toast);
    new bootstrap.Toast(toast, { delay: 4500 }).show();
    setTimeout(() => toast.remove(), 5000);
  }

  //close modal
  function closeModal() {
    const modal = bootstrap.Modal.getInstance(
      document.getElementById("confirm-modal")
    );
    modal.hide();
  }
  // loader show/hide
  function loaderToggel(hide) {
    const loader = document.getElementById("loader");
    const modal = document.getElementById("confirm-modal");
    loader.style.visibility = hide ? "hidden" : "visible";
    modal.style.zIndex = hide ? "1100" : "10";
  }
});
