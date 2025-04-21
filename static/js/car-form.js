/**
 * upload images in car create edit form
 *  */

document.addEventListener("DOMContentLoaded", function () {
  // selectedImageId determines the id of image to be deleted
  var selectedImageId;
  document.querySelectorAll(".delete-image-btn").forEach((btn) => {
    btn.addEventListener("click", function () {
      selectedImageId = this.dataset.imageId;
    });
  });

  // when the delete is confirmed then call delete_car_image url
  document
    .getElementById("confirmDelete")
    .addEventListener("click", function () {
      if (!selectedImageId) return;
      loaderToggel(false);

      fetch(`/car/image/${selectedImageId}/delete/`, {
        method: "DELETE",
        headers: {
          "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
            .value,
          "X-Requested-With": "XMLHttpRequest"
        }
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.success) {
            // remove image preview
            document
              .getElementById(`image-preview-${selectedImageId}`)
              .remove(false);
            // closeModal function is defined in main.js
            closeModal();
            // show success message
            showToast("Image deleted successfully!");
          } else {
            alert("Error deleting image");
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

  //remove duplicate image input
  var element = document.getElementById("div_id_images");
  if (element) {
    element.remove(); // removes the element from the DOM
  }

  //drag and drop images in car forms
  const dropArea = document.getElementById("drop-area");
  const input = document.getElementById("id_image");
  const preview = document.getElementById("preview");

  // Virtual file list
  let fileBuffer = new DataTransfer();

  // Drag & Drop
  dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropArea.classList.add("bg-light");
  });

  dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("bg-light");
  });

  // every time changes the images list
  // preview the change on html
  dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    dropArea.classList.remove("bg-light");
    handleFiles(e.dataTransfer.files);
  });

  input.addEventListener("change", () => {
    handleFiles(input.files);
  });

  function handleFiles(files) {
    for (let file of files) {
      addFileToPreview(file);
      fileBuffer.items.add(file);
    }
    input.files = fileBuffer.files;
  }

  function addFileToPreview(file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      const col = document.createElement("div");
      col.className = "col-12 col-md-4 position-relative";

      col.innerHTML = `
              <div class="border rounded shadow-sm overflow-hidden position-relative">
                  <img src="${e.target.result}" class="img-fluid rounded" alt="preview">
                  <button type="button" class="btn btn-sm btn-danger position-absolute top-0 end-0 m-1 delete-btn">&times;</button>
              </div>
          `;
      preview.appendChild(col);

      const deleteBtn = col.querySelector(".delete-btn");
      deleteBtn.addEventListener("click", () => {
        removeFile(file);
        col.remove();
      });
    };
    reader.readAsDataURL(file);
  }

  function removeFile(fileToRemove) {
    let newBuffer = new DataTransfer();
    for (let i = 0; i < fileBuffer.items.length; i++) {
      const file = fileBuffer.items[i].getAsFile();
      if (file !== fileToRemove) {
        newBuffer.items.add(file);
      }
    }
    fileBuffer = newBuffer;
    input.files = fileBuffer.files;
  }

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
