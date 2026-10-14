# The Arch Apartments

Website for The Arch: two sea-view apartments side by side in Umhlanga Arch, Umhlanga Ridge, Durban, with direct booking through InnStyle.

- Airbnb: [Apartment One](https://www.airbnb.co.uk/rooms/49722888) · [Apartment Two](https://www.airbnb.co.uk/rooms/812778798092691373)

It's a plain static site (HTML/CSS/JS, no build step). Open `index.html` in a browser to preview it.

## Pages

| File | What it is |
|---|---|
| `index.html` | Home: welcome, both apartments, gallery, location, FAQ |
| `apartment-1.html` | 2 Bedroom Luxury Sea View Apartment: photos, description, amenities, booking |
| `apartment-2.html` | Dream View Apartment: photos, description, amenities, booking |
| `book.html` | Booking page with both apartments |

## Connecting InnStyle bookings

Edit **`js/config.js`**. For each apartment:

- `bookingUrl`: the InnStyle direct booking link. Every "Book" button for that apartment goes here.
- `embedUrl` (optional): an InnStyle availability/booking widget URL, which is shown inline on the apartment page and on `book.html`.

You can also set the apartment names, enquiry email and phone number there. Until a `bookingUrl` is set, "Book" buttons open an enquiry email, so guests never hit a dead link.

## Content and photos

All photos are the professional Stephen Rowley shoot from the "Arch photos" folder in Google Drive, resized for the web:

- `images/apartment-1/`: 2 Bedroom Luxury Sea View Apartment (unit 1408) (2 bedrooms, light oak interiors)
- `images/apartment-2/`: Dream View Apartment (unit 1401)
- `images/building/`: hero image and coastal views

To change a description, edit the text in `apartment-1.html` / `apartment-2.html`. To swap a photo, replace the file in `images/` with one of the same name.

## Publishing

Any static host works. With **GitHub Pages**: go to repo Settings → Pages, then pick the `main` branch and `/ (root)`. With **Netlify**: drag the folder onto app.netlify.com/drop. Then point your domain at it.

## Logo

Logo files are in `images/brand/`:

- `logo.svg` / `logo.png`: for light backgrounds
- `logo-white.svg` / `logo-white.png`: for dark backgrounds or over photos
- `icon.svg` / `icon.png`: square icon (profile pictures, browser tab)

Use the PNGs for social media, InnStyle and email signatures.
