(function () {
  var config = window.ARCH_CONFIG || { apartments: {} };

  function whatsappHref(text) {
    return "https://wa.me/" + config.whatsappNumber + "?text=" + encodeURIComponent(text);
  }

  function bookingHref(apt) {
    if (apt && apt.bookingUrl) return apt.bookingUrl;
    if (config.whatsappNumber) {
      return whatsappHref("Hi, I'd like to check availability for the " + (apt ? apt.name : "The Arch Apartments") + ". My dates are: ");
    }
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
    if (apt && (apt.bookingUrl || config.whatsappNumber)) {
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

  // WhatsApp links: <a data-whatsapp>
  document.querySelectorAll("[data-whatsapp]").forEach(function (el) {
    if (!config.whatsappNumber) { (el.closest("[data-whatsapp-wrap]") || el).remove(); return; }
    el.href = whatsappHref("Hi, I have a question about The Arch Apartments.");
    el.target = "_blank";
    el.rel = "noopener";
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

  // Gallery lightbox
  var box = document.querySelector(".lightbox");
  if (box) {
    var boxImg = box.querySelector("img"), list = [], pos = 0;
    function show(i) {
      pos = (i + list.length) % list.length;
      boxImg.src = list[pos].src;
      boxImg.alt = list[pos].alt;
    }
    function close() { box.hidden = true; document.body.style.overflow = ""; }
    document.querySelectorAll("[data-gallery]").forEach(function (g) {
      var imgs = Array.prototype.slice.call(g.querySelectorAll("img"));
      imgs.forEach(function (im, i) {
        im.addEventListener("click", function () {
          list = imgs; show(i);
          box.hidden = false; document.body.style.overflow = "hidden";
        });
      });
    });
    box.querySelector(".lightbox-close").addEventListener("click", close);
    box.querySelector(".lightbox-prev").addEventListener("click", function () { show(pos - 1); });
    box.querySelector(".lightbox-next").addEventListener("click", function () { show(pos + 1); });
    box.addEventListener("click", function (e) { if (e.target === box) close(); });
    document.addEventListener("keydown", function (e) {
      if (box.hidden) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") show(pos - 1);
      if (e.key === "ArrowRight") show(pos + 1);
    });
  }

  // Google Analytics / Google Ads (only loads once an ID is set in config.js)
  var tagIds = [config.googleAnalyticsId, config.googleAdsId].filter(Boolean);
  if (tagIds.length) {
    var gs = document.createElement("script");
    gs.async = true;
    gs.src = "https://www.googletagmanager.com/gtag/js?id=" + tagIds[0];
    document.head.appendChild(gs);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    tagIds.forEach(function (id) { window.gtag("config", id); });
    document.querySelectorAll("[data-book]").forEach(function (el) {
      el.addEventListener("click", function () {
        var apt = el.getAttribute("data-book");
        window.gtag("event", "book_click", { apartment: apt });
        if (config.googleAdsId && config.googleAdsBookLabel) {
          window.gtag("event", "conversion", { send_to: config.googleAdsId + "/" + config.googleAdsBookLabel });
        }
      });
    });
  }

  var year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();
})();
