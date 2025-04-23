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
    for (child of elem.children) {
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
          "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
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
            // remove car from list
            document
              .getElementById(`row-car-${selectedCarId}`)
              .remove(false);
            // closeModal function is defined 
            closeModal();
            // show success message
            showToast("Car deleted successfully!");
          } else {
            alert("Error deleting car");
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        })
        .finally(() => {
          // loaderToggel function is defined
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
