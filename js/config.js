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
 * Until bookingUrl is filled in, "Book" buttons fall back to the
 * enquiry email below so no guest hits a dead link.
 */
window.ARCH_CONFIG = {
  contactEmail: "hello@example.com",   // TODO: your enquiries email
  contactPhone: "",                     // TODO: optional, e.g. "+44 7700 900000"

  apartments: {
    "apartment-1": {
      name: "Apartment One",            // TODO: match your Airbnb listing name
      bookingUrl: "",                   // TODO: InnStyle booking link
      embedUrl: "",                     // TODO: optional InnStyle widget URL
      airbnbUrl: "https://www.airbnb.co.uk/rooms/49722888"
    },
    "apartment-2": {
      name: "Apartment Two",            // TODO: match your Airbnb listing name
      bookingUrl: "",                   // TODO: InnStyle booking link
      embedUrl: "",                     // TODO: optional InnStyle widget URL
      airbnbUrl: "https://www.airbnb.co.uk/rooms/812778798092691373"
    }
  }
};
