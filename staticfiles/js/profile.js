document.addEventListener("DOMContentLoaded", function () {
  /**
   * Go to link on table row click
   */
  document.querySelectorAll(".clickable-row").forEach(function (row) {
    row.addEventListener("click", function () {
      window.location = row.dataset.href;
    });
  });

  /**
   * code for remove duplicate image input
   * from profile form
   */
  function removeExtraImageInput(elem) {
    for (let child of elem.children) {
      if (child.classList.contains("input-group")) {
        elem.removeChild(child);
      }
    }
  }

  const inputImage = document.getElementById("div_id_profile_image");

  if (inputImage) {
    removeExtraImageInput(inputImage);
  }
  // selectedCarId determines the id of car to be deleted
  var selectedCarId;
  document.querySelectorAll(".delete-car-btn").forEach((btn) => {
    btn.addEventListener("click", function () {
      selectedCarId = this.dataset.carId;
    });
  });

  // when the delete is confirmed then call delete_car url
  document
    .getElementById("confirmDelete")
    .addEventListener("click", function () {
      if (!selectedCarId) return;
      loaderToggel(false);

      fetch(`/car-delete/${selectedCarId}/`, {
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
              res.statusText || "Something went wrong",
              "text-bg-danger"
            );
            throw new Error(`HTTP error ${res.status}`);
          }
          return res.json();
        })
        .then((data) => {
          // remove car from list
          document.getElementById(`row-car-${selectedCarId}`).remove(false);
          closeModal();
          // show success message
          showToast("Car deleted successfully!", "text-bg-success");
        })
        .catch((error) => {
          showToast(error, "text-bg-danger");
          console.error("Error:", error);
        })
        .finally(() => {
          loaderToggel(true);
        });
    });

  // show message as a bootstrap toast
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
