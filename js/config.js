/*
 * ============================================================
 *  THE ARCH — SITE SETTINGS
 *  This is the only file you need to edit to connect bookings.
 * ============================================================
 *
 * InnStyle gives you a booking link (and optionally an embeddable
 * booking widget) for each property. Find them in your InnStyle
 * account under the booking engine / website integration settings,
 * or ask InnStyle support for the "direct booking URL" for each unit.
 *
 *  - bookingUrl: the page guests are sent to when they click "Book".
 *  - embedUrl:   (optional) a URL InnStyle provides for embedding the
 *                availability calendar / booking form in an iframe.
 *                Leave as "" to just show a "Book now" button.
 *
 * Until bookingUrl is filled in, "Book" buttons open a WhatsApp chat
 * (or the enquiry email if no WhatsApp number is set).
 */
window.ARCH_CONFIG = {
  contactEmail: "explorecape@gmail.com",
  contactPhone: "+27 83 714 2186",
  whatsappNumber: "27837142186",        // international format, no + or spaces

  // Google tracking: paste your IDs here when you have them, e.g. "G-ABC123XYZ"
  googleAnalyticsId: "",                // GA4 Measurement ID (G-...)
  googleAdsId: "",                      // Google Ads tag ID (AW-...)
  googleAdsBookLabel: "",               // optional conversion label for "Book" clicks

  apartments: {
    "apartment-1": {
      name: "2 Bedroom Luxury Sea View Apartment",
      bookingUrl: "",                   // TODO: InnStyle booking link
      embedUrl: "",                     // TODO: optional InnStyle widget URL
      airbnbUrl: "https://www.airbnb.co.uk/rooms/49722888"
    },
    "apartment-2": {
      name: "Dream View Apartment",
      bookingUrl: "",                   // TODO: InnStyle booking link
      embedUrl: "",                     // TODO: optional InnStyle widget URL
      airbnbUrl: "https://www.airbnb.co.uk/rooms/812778798092691373"
    }
  }
};
