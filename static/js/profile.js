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
});
