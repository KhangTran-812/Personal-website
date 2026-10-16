/* ============================================================
   Khang B. Tran — Portfolio interactions
   Typing effect (Typed.js w/ fallback), mobile nav, scrollspy,
   reveal-on-scroll, footer year.
   ============================================================ */

(function () {
  "use strict";

  // Gate scroll-reveal styles to JS-enabled browsers (see .js .reveal in CSS).
  document.documentElement.classList.add("js");

  var prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Typing effect ---------- */
  // Static fallback text already lives in the HTML (#typed), so the page
  // reads correctly even if the CDN script or JS is unavailable.
  function initTyped() {
    if (typeof window.Typed !== "function") return;
    var target = document.getElementById("typed");
    if (!target || prefersReducedMotion) return;

    new window.Typed("#typed", {
      strings: [
        "Aspiring Application Developer",
        "Quality Assurance Enthusiast",
        "Full-Stack Java Developer"
      ],
      typeSpeed: 45,
      backSpeed: 28,
      backDelay: 2000,
      startDelay: 600,
      loop: true,
      smartBackspace: false
    });
  }

  /* ---------- Mobile navigation ---------- */
  function initNav() {
    var toggle = document.getElementById("nav-toggle");
    var nav = document.getElementById("site-nav");
    if (!toggle || !nav) return;

    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });

    // Close the panel after choosing a destination.
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        nav.classList.remove("nav-open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* ---------- Reveal on scroll ---------- */
  function initReveal() {
    var items = document.querySelectorAll(".reveal");
    if (!items.length || prefersReducedMotion || !("IntersectionObserver" in window)) {
      items.forEach(function (el) { el.classList.add("is-visible"); });
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.08 }
    );

    items.forEach(function (el) { observer.observe(el); });
  }

  /* ---------- Scrollspy (active nav link) ---------- */
  function initScrollspy() {
    var links = Array.prototype.slice.call(document.querySelectorAll(".site-nav a[href^='#']"));
    if (!links.length || !("IntersectionObserver" in window)) return;

    var map = {};
    links.forEach(function (link) {
      var id = link.getAttribute("href").slice(1);
      map[id] = link;
    });

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          var link = map[entry.target.id];
          if (!link) return;
          if (entry.isIntersecting) {
            links.forEach(function (l) { l.classList.remove("is-active"); });
            link.classList.add("is-active");
          }
        });
      },
      { rootMargin: "-40% 0px -55% 0px" }
    );

    ["about", "projects", "skills", "experience", "contact"].forEach(function (id) {
      var section = document.getElementById(id);
      if (section) observer.observe(section);
    });
  }

  /* ---------- Footer year ---------- */
  function initYear() {
    var el = document.getElementById("year");
    if (el) el.textContent = String(new Date().getFullYear());
  }

  initTyped();
  initNav();
  initReveal();
  initScrollspy();
  initYear();
})();
