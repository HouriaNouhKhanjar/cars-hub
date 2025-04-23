document.addEventListener("DOMContentLoaded", function () {
  const tooltipTriggerList = document.querySelectorAll(
    '[data-bs-toggle="tooltip"]'
  );
  const tooltipList = [...tooltipTriggerList].map(
    (tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl)
  );
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
});
