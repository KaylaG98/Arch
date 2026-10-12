# The Arch

Website for The Arch: two self-catering apartments side by side in one building, with direct booking through InnStyle.

- Airbnb: [Apartment One](https://www.airbnb.co.uk/rooms/49722888) · [Apartment Two](https://www.airbnb.co.uk/rooms/812778798092691373)

It's a plain static site (HTML/CSS/JS, no build step). Open `index.html` in a browser to preview it.

## Pages

| File | What it is |
|---|---|
| `index.html` | Home: welcome, both apartments, gallery, location, reviews, FAQ |
| `apartment-1.html` / `apartment-2.html` | Full details, amenities, house rules and booking for each apartment |
| `book.html` | Booking page with both apartments |

## Connecting InnStyle bookings

Edit **`js/config.js`**. For each apartment:

- `bookingUrl`: the InnStyle direct booking link. Every "Book" button for that apartment goes here.
- `embedUrl` (optional): an InnStyle availability/booking widget URL, which is shown inline on the apartment page and on `book.html`.

You can also set the apartment names, enquiry email and phone number there. Until a `bookingUrl` is set, "Book" buttons open an enquiry email, so guests never hit a dead link.

## Adding your content

Search the HTML files for `TODO`. Each one marks text to replace with the details from your Airbnb listings (description, guests/bedrooms, amenities, house rules, reviews, town, address and map postcode).

**Photos:** add JPGs using these names:

```
images/building/hero.jpg         big photo at the top of the home page
images/building/gallery-1.jpg
images/apartment-1/cover.jpg, 1.jpg, 2.jpg, 3.jpg, 4.jpg
images/apartment-2/cover.jpg, 1.jpg, 2.jpg, 3.jpg, 4.jpg
```

A striped placeholder shows wherever a photo is missing. Aim for landscape images about 1600px wide.

## Publishing

Any static host works. With **GitHub Pages**: go to repo Settings → Pages, then pick the `main` branch and `/ (root)`. With **Netlify**: drag the folder onto app.netlify.com/drop. Then point your domain at it.
