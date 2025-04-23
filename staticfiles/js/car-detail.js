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
          var imagesrc = document.getElementById('profile-placeholder').getAttribute('src');
          image_url =
            data.image_url == "placeholder"
              ? imagesrc
              : data.image_url;
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
                    <span class="dropdown-item edit-btn" data-id="${data.id}">
                      Edit
                    </span>
                  </li>
                  <li>
                  <hr class="dropdown-divider">
                  </li>
                  <li>
                    <span class="dropdown-item delete-btn" data-id="${data.id}">
                      Delete
                    </span>
                  </li>
                </ul>
              </span>
            </div>
            <p class="comment-content">
            ${data.content} 
             <br>
             <small class="comment-time">Now</small>
             </p>
          </div>`;
          document
            .getElementById("comments-list")
            .insertAdjacentHTML("beforeend", newComment);
          this.reset();
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });
  }
});
