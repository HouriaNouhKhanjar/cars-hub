document.addEventListener("DOMContentLoaded", function () {
  // auto scroll to car list on home page
  const url = new URL(window.location.href);
  const isHome = url.pathname === "/";
  const hasSearch = url.searchParams.has("search");
  const hasPage = url.searchParams.has("page");
  const hasCategory = url.searchParams.has("category");

  if (isHome && (hasSearch || hasPage || hasCategory)) {
    const target = document.getElementById("cars-list");
    if (target) {
      target.scrollIntoView({ behavior: "smooth" });
    }
  }
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
