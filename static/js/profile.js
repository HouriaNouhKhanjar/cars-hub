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

  //make summernote textarea width = 100%

  const iframe = document.getElementById("id_description_iframe");

  iframe.onload = function () {
    const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
    console.log(iframeDoc.querySelectorAll("html body div"));
    const target = iframeDoc.querySelector(".note-editor");
    console.log(target);
    if (target) {
      target.style.width = "100%!important";
    }
  };

  /**
   * upload images in car create edit form
   *  */
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
      col.className = "col-4 col-sm-3 col-md-2 position-relative";

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
});
