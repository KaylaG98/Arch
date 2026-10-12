(function () {
  var config = window.ARCH_CONFIG || { apartments: {} };

  function bookingHref(apt) {
    if (apt && apt.bookingUrl) return apt.bookingUrl;
    var subject = encodeURIComponent("Booking enquiry – " + (apt ? apt.name : "The Arch"));
    return "mailto:" + config.contactEmail + "?subject=" + subject;
  }

  // Apartment names from config
  document.querySelectorAll("[data-apt-name]").forEach(function (el) {
    var apt = config.apartments[el.getAttribute("data-apt-name")];
    if (apt) el.textContent = apt.name;
  });

  // "Book" buttons: <a data-book="apartment-1">
  document.querySelectorAll("[data-book]").forEach(function (el) {
    var apt = config.apartments[el.getAttribute("data-book")];
    el.href = bookingHref(apt);
    if (apt && apt.bookingUrl) {
      el.target = "_blank";
      el.rel = "noopener";
    }
  });

  // Airbnb links: <a data-airbnb="apartment-1">
  document.querySelectorAll("[data-airbnb]").forEach(function (el) {
    var apt = config.apartments[el.getAttribute("data-airbnb")];
    if (apt && apt.airbnbUrl) el.href = apt.airbnbUrl;
    else el.remove();
  });

  // Embedded InnStyle widgets: <div data-embed="apartment-1">
  document.querySelectorAll("[data-embed]").forEach(function (el) {
    var apt = config.apartments[el.getAttribute("data-embed")];
    if (!apt || !apt.embedUrl) return;
    var frame = document.createElement("iframe");
    frame.src = apt.embedUrl;
    frame.title = "Check availability – " + apt.name;
    frame.loading = "lazy";
    frame.className = "booking-frame";
    el.innerHTML = "";
    el.appendChild(frame);
  });

  // Contact details
  document.querySelectorAll("[data-email]").forEach(function (el) {
    el.href = "mailto:" + config.contactEmail;
    el.textContent = config.contactEmail;
  });
  document.querySelectorAll("[data-phone]").forEach(function (el) {
    if (!config.contactPhone) { (el.closest("[data-phone-wrap]") || el).remove(); return; }
    el.href = "tel:" + config.contactPhone.replace(/\s/g, "");
    el.textContent = config.contactPhone;
  });

  // Photos: show a tidy placeholder if an image file hasn't been added yet
  document.querySelectorAll("img[data-photo]").forEach(function (img) {
    function fail() {
      var ph = document.createElement("div");
      ph.className = img.className + " photo-placeholder";
      ph.setAttribute("role", "img");
      ph.setAttribute("aria-label", img.alt);
      ph.innerHTML = "<span>" + img.alt + "</span>";
      img.replaceWith(ph);
    }
    if (img.complete && img.naturalWidth === 0) fail();
    else img.addEventListener("error", fail);
  });

  // Mobile nav
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open);
    });
    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  var year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();
})();
