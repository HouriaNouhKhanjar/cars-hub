document.addEventListener("DOMContentLoaded", function() {
  document.querySelectorAll(".clickable-row").forEach(function(row) {
    row.addEventListener("click", function() {
      window.location = row.dataset.href;
    });
  });
});