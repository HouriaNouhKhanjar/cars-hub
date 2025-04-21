document.addEventListener("DOMContentLoaded", function () {
  // hide response message toast after 5 s
  setTimeout(() => {
    document.querySelectorAll(".toast").forEach((el) => {
      el.remove();
    });
  }, 5000);

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
