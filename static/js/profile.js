document.addEventListener("DOMContentLoaded", function() {
  document.querySelectorAll(".clickable-row").forEach(function(row) {
    row.addEventListener("click", function() {
      window.location = row.dataset.href;
    });
  });

  function getLabel(elem) {
    return Array.from(elem.parentNode.children).filter(
      (child) => child.tagName == 'LABEL'
    );
  }

  const inputImage = document.getElementById('id_profile_image');

  if(inputImage) {
    var label = getLabel(inputImage)[0];
    var parent = inputImage.parentNode;
    parent.textContent = "";
    parent.appendChild(label);
    parent.appendChild(inputImage);
  }
});