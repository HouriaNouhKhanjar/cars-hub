document.addEventListener("DOMContentLoaded", function () {
  // hide response message toast after 5 s
    setTimeout(() => {
      document.querySelectorAll(".toast").forEach((el) => {
        el.remove();
      });
    }, 5000);
});
