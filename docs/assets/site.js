// Theme toggle (light is the default; the visitor's choice is remembered) and the phone menu.
(function () {
  var root = document.documentElement, theme = document.getElementById("theme"), menu = document.getElementById("menu"), nav = document.getElementById("nav");
  function sync() {
    var dark = root.dataset.theme === "dark";
    theme.setAttribute("aria-pressed", dark);
    theme.setAttribute("aria-label", dark ? "Light mode" : "Dark mode");
  }
  theme.addEventListener("click", function () {
    var next = root.dataset.theme === "dark" ? "light" : "dark";
    root.dataset.theme = next;
    try { localStorage.setItem("theme", next); } catch (e) {}
    sync();
  });
  menu.addEventListener("click", function () {
    var open = nav.classList.toggle("open");
    menu.setAttribute("aria-expanded", open);
  });
  document.addEventListener("keydown", function (ev) {
    if (ev.key === "Escape" && nav.classList.contains("open")) { nav.classList.remove("open"); menu.setAttribute("aria-expanded", false); menu.focus(); }
  });
  sync();
})();
