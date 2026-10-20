"""Builds the HTML pages, sitemap.xml and robots.txt.

Run from anywhere:  python3 tools/build.py
"""
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
LOGO = '<svg class="logo" viewBox="0 0 300 64" role="img" aria-label="The Arch Apartments">  <g fill="none" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">    <path d="M8 58V28a20 20 0 0 1 40 0v30"/>    <path d="M16 58V30a12 12 0 0 1 24 0v28"/>    <path d="M18 46c3.3 0 3.3-2.6 6.6-2.6s3.3 2.6 6.6 2.6 3.3-2.6 6.6-2.6"/>    <path d="M4 58h48"/>  </g>  <text x="66" y="38" font-family="Cormorant Garamond, Georgia, serif" font-size="32" font-weight="600" fill="var(--ink)" letter-spacing="0.5">The Arch</text>  <text x="67.5" y="56" font-family="DM Sans, Helvetica Neue, Arial, sans-serif" font-size="10.5" font-weight="600" fill="var(--accent)" letter-spacing="5.2">APARTMENTS</text></svg>'

import json as _j
# Change this to your own domain when you have one (keep the trailing slash).
SITE_URL = 'https://kaylag98.github.io/Arch/'
PAGES = []
def head(title, desc, home=False, path='', image='images/building/whalebone-pier.jpg', schema=None):
    p = '' if home else 'index.html'
    url = SITE_URL + path
    PAGES.append(path)
    ld = ''.join(f'\n  <script type="application/ld+json">{_j.dumps(x, ensure_ascii=False)}</script>' for x in (schema or []))
    return f'''<!DOCTYPE html>
<html lang="en-ZA">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{url}">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#8a5a3b">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="The Arch Apartments">
  <meta property="og:locale" content="en_ZA">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{SITE_URL}{image}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{SITE_URL}{image}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=DM+Sans:wght@400;500;600&family=Inter:wght@400;600&display=swap" rel="stylesheet">
  <link rel="icon" href="images/brand/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/brand/icon.png">
  <link rel="stylesheet" href="css/style.css">{ld}
</head>
<body>

<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="index.html">{LOGO}</a>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false">☰</button>
    <nav class="site-nav">
      <a href="apartment-1.html">Luxury Sea View</a>
      <a href="apartment-2.html">Dream View</a>
      <a href="things-to-do.html">Things to do</a>
      <a href="{p}#location">Location</a>
      <a href="{p}#faq">FAQ</a>
      <a class="btn" href="book.html">Book now</a>
    </nav>
  </div>
</header>
'''

FOOT = '''
<footer class="site-footer">
  <div class="container footer-inner">
    <div><span class="footer-logo">@@LOGO@@</span>Umhlanga Arch, 1 Ncondo Place<br>Ridgeside, Umhlanga, KwaZulu-Natal</div>
    <div>
      Email: <a data-email href="mailto:explorecape@gmail.com">explorecape@gmail.com</a><br>
      <span data-phone-wrap>Phone: <a data-phone href="tel:+27837142186">+27 83 714 2186</a></span><br>
      <span data-whatsapp-wrap><a data-whatsapp href="https://wa.me/27837142186">Chat on WhatsApp</a></span>
    </div>
    <div>© <span id="year"></span> The Arch Apartments</div>
  </div>
</footer>

<div class="lightbox" hidden>
  <button class="lightbox-close" aria-label="Close">×</button>
  <button class="lightbox-prev" aria-label="Previous photo">‹</button>
  <img alt="">
  <button class="lightbox-next" aria-label="Next photo">›</button>
</div>

<script src="js/config.js"></script>
<script src="js/main.js"></script>
</body>
</html>
'''
FOOT = FOOT.replace('@@LOGO@@', LOGO)

def img(src, alt, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<img{c} src="{src}" alt="{alt}" loading="lazy">'

def gallery(items):
    return '<div class="gallery" data-gallery>\n' + '\n'.join('      ' + img(s, a) for s, a in items) + '\n    </div>'

APTS = {
 'apartment-1': dict(
   name='2 Bedroom Luxury Sea View Apartment', other='apartment-2', other_name='Dream View Apartment',
   tagline='Two bedrooms, two bathrooms and a sunny balcony looking straight down the coast.',
   facts=['Sleeps 4', '2 bedrooms', '2 bathrooms', 'Sea-view balcony'],
   card='Bright and airy, with light oak floors, an open-plan lounge with large windows and a furnished balcony facing the ocean. A king bedroom with en-suite and a twin room make it ideal for families and friends.',
   about=[
     'Unwind and relax as you step into this luxury apartment. High up in the iconic Umhlanga Arch, it offers beautiful panoramic views of Umhlanga’s coastline through large windows. Whether you are visiting for work or taking a holiday, this apartment is perfect for you.',
     'The open-plan living area has a deep corner sofa, a smart TV and a solid timber coffee table, flowing into a dining table for four and a sleek, fully equipped kitchen. Step out onto the furnished balcony for a morning coffee or a sundowner, with the whole coast laid out below you.',
     'Both bedrooms have sweeping views from their large windows. The main bedroom has a king-size bed dressed in fresh linen and its own en-suite with a walk-in glass shower. The second bedroom has two single beds and built-in wardrobes, with a second shower room next door. It is a great set-up for families and groups of friends.',
     'You’ll have a professional concierge service in the building, Wi-Fi, air conditioning throughout and up to two parking bays. Daily housekeeping is available on request at an additional cost.',
   ],
   space=[('Main bedroom','King-size bed, en-suite walk-in shower'),('Second bedroom','Two single beds, built-in wardrobes'),('Bathrooms','En-suite shower room plus a second shower room'),('Living area','Corner sofa, smart TV, panoramic windows'),('Kitchen &amp; dining','Fully equipped kitchen, dining table for four'),('Balcony','Furnished'),('Parking','Up to 2 parking bays')],
   amen=['Sea &amp; beach views','City skyline views','Furnished balcony','Air conditioning','Wi-Fi','Smart TV','Fully equipped kitchen','Cooking basics','Crockery &amp; cutlery','Fridge','Dining table for four','Fresh bed linen &amp; towels','Concierge service','Daily housekeeping on request (extra cost)','Up to 2 parking bays','Biometric access &amp; 24hr security'],
   maxguests='4 guests maximum', maxn=4, beds=2, baths=2,
   seo='2-bedroom self-catering apartment at Umhlanga Arch, Umhlanga Ridge: king and twin rooms, 2 bathrooms, furnished balcony and panoramic ocean views. Sleeps 4.',
   photos=[('cover.jpg','Open-plan lounge with ocean views'),('main-bedroom.jpg','King bedroom'),('balcony.jpg','Furnished balcony with ocean view'),('kitchen.jpg','Fully equipped kitchen'),('dining.jpg','Dining and living area'),('living.jpg','Lounge with corner sofa'),('main-bedroom-view.jpg','Main bedroom with view'),('ensuite.jpg','En-suite with walk-in shower'),('second-bedroom.jpg','Twin bedroom'),('balcony-view.jpg','Balcony overlooking the coast'),('vanity.jpg','Bathroom vanity'),('bathroom.jpg','Second shower room'),('kitchen-detail.jpg','Kitchen details')],
 ),
 'apartment-2': dict(
   name='Dream View Apartment', other='apartment-1', other_name='2 Bedroom Luxury Sea View Apartment',
   tagline='A one-bedroom showpiece with 180-degree views of the ocean, an island kitchen and an en-suite with a bath.',
   facts=['1 bedroom','Sleeps 2','180° ocean views','Island kitchen'],
   card='Our one-bedroom showpiece, with 180-degree views of the ocean from the living area. Rich timber, statement art, an island kitchen and an en-suite with a bath, all opening onto a balcony overlooking the coast.',
   about=[
     'Welcome to our beautiful apartment in the prestigious Umhlanga Arch, known for its picturesque views and prime location. Enjoy stunning 180-degree views of the ocean from every angle of the living area, and wake up to breathtaking sea views from the bedroom. Experience the best of coastal living in this luxurious space.',
     'Inside, deep charcoal walls, smoked oak joinery, brass lighting and bold contemporary art set the tone. The open-plan living area centres on a sumptuous modular sofa and a timber-slatted media wall with a smart TV and soundbar, leading to a dining table beneath a woven pendant. The kitchen is made for cooking, with an island, an oven, a microwave and a large fridge.',
     'Step out onto the balcony to take in the coastline, then retreat to the bedroom with its sea views and en-suite bathroom with a bath.',
     'The apartment is fully air-conditioned with Wi-Fi throughout.',
   ],
   space=[('Bedroom','Sea views, en-suite'),('En-suite','Bath'),('Living area','180° ocean views, modular sofa, smart TV &amp; soundbar'),('Kitchen &amp; dining','Island with seating, oven, microwave, dining table'),('Balcony','Ocean views')],
   amen=['180° ocean views','Beach &amp; city skyline views','Balcony','En-suite with bath','Air conditioning','Wi-Fi','Smart TV &amp; soundbar','Island kitchen','Oven','Microwave','Cooking basics','Crockery &amp; cutlery','Fridge with water dispenser','Coffee machine','Bed linen &amp; towels','Biometric access &amp; 24hr security'],
   maxguests='2 guests maximum', maxn=2, beds=1, baths=1,
   seo='1-bedroom apartment with a penthouse feel at Umhlanga Arch: 180-degree ocean views, island kitchen and en-suite with bath. Perfect for couples. Sleeps 2.',
   photos=[('cover.jpg','Open-plan living with 180-degree ocean views'),('lounge-sunny.jpg','Lounge with ocean and city views'),('ensuite-view.jpg','En-suite and bedroom with sea views'),('kitchen.jpg','Island kitchen'),('bath.jpg','En-suite bath'),('main-bedroom.jpg','Bedroom'),('kitchen-island.jpg','Kitchen island with bar seating'),('dining.jpg','Dining area'),('balcony.jpg','Balcony with ocean views')],
 ),
}

# ---------- index ----------
ADDR = {'@type':'PostalAddress','streetAddress':'Umhlanga Arch, 1 Ncondo Place','addressLocality':'Umhlanga','addressRegion':'KwaZulu-Natal','addressCountry':'ZA'}
BIZ = {'@context':'https://schema.org','@type':'LodgingBusiness','@id':SITE_URL+'#business','name':'The Arch Apartments','description':'Two beautifully furnished self-catering sea-view apartments in Umhlanga Arch, Umhlanga Ridge, Durban.','url':SITE_URL,'logo':SITE_URL+'images/brand/logo.png','image':[SITE_URL+'images/building/whalebone-pier.jpg',SITE_URL+'images/apartment-1/cover.jpg',SITE_URL+'images/apartment-2/cover.jpg'],'address':ADDR,'telephone':'+27837142186','email':'explorecape@gmail.com','checkinTime':'15:00','checkoutTime':'10:00','smokingAllowed':False,'amenityFeature':[{'@type':'LocationFeatureSpecification','name':n,'value':True} for n in ['Sea views','Air conditioning','Wi-Fi','Furnished balcony','Biometric access control','24-hour security']]}
def crumbs(*items):
    return {'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':i+1,'name':n,'item':SITE_URL+u} for i,(n,u) in enumerate(items)]}
idx = head('The Arch Apartments | Sea-View Holiday Apartments in Umhlanga', 'Self-catering sea-view apartments in Umhlanga Arch, Umhlanga Ridge, Durban. A 2-bedroom family apartment and a 1-bedroom penthouse-style stay. Book direct.', home=True, path='', schema=[BIZ])
cards = ''
for k, a in APTS.items():
    facts = ''.join(f'<li>{f}</li>' for f in a['facts'])
    cards += f'''
      <article class="card">
        <a href="{k}.html">{img(f"images/{k}/cover.jpg", a["name"], "card-media")}</a>
        <div class="card-body">
          <h3 data-apt-name="{k}">{a["name"]}</h3>
          <ul class="facts">{facts}</ul>
          <p>{a["card"]}</p>
          <div class="btn-row">
            <a class="btn" data-book="{k}" href="book.html">Book</a>
            <a class="btn ghost" href="{k}.html">View apartment</a>
          </div>
        </div>
      </article>'''
idx += f'''
<section class="hero">
  <img class="hero-media" src="images/building/whalebone-pier.jpg" alt="Aerial view of Whalebone Pier and Umhlanga beach">
  <div class="container hero-content">
    <div class="eyebrow">Umhlanga Ridge · Durban · KwaZulu-Natal</div>
    <h1>The Arch Apartments</h1>
    <p>Two beautifully furnished apartments high above Umhlanga in the landmark Umhlanga Arch, with sweeping ocean views.</p>
    <div class="btn-row">
      <a class="btn light" href="book.html">Check availability</a>
      <a class="btn outline-light" href="#apartments">See the apartments</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container center">
    <div class="eyebrow">Welcome</div>
    <h2>Your home above the coast</h2>
    <p class="lead">Umhlanga Arch is an iconic development, and our two apartments sit high above Umhlanga with large windows, furnished balconies and some of the best ocean views KZN has to offer. Have a drink on the balcony, shop the high street in style or dress up for a night out at The Baron. Stay in one apartment, or book both when family and friends travel together.</p>
    <div class="features">
      <div class="feature"><svg class="feature-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M2 15c2 0 2-1.5 4-1.5S8 15 10 15s2-1.5 4-1.5 2 1.5 4 1.5 2-1.5 4-1.5"/><path d="M2 19c2 0 2-1.5 4-1.5S8 19 10 19s2-1.5 4-1.5 2 1.5 4 1.5 2-1.5 4-1.5"/><circle cx="12" cy="7.5" r="3"/></svg><h3>Ocean views</h3><p>Wake up to the ocean from high above Umhlanga Ridge.</p></div>
      <div class="feature"><svg class="feature-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5 4.5 5.5v6c0 4.6 3.2 8.4 7.5 10 4.3-1.6 7.5-5.4 7.5-10v-6z"/><path d="m8.5 12 2.5 2.5 4.5-5"/></svg><h3>Safe &amp; secure</h3><p>Biometric access control, 24-hour CCTV and 24-hour ground-floor security.</p></div>
      <div class="feature"><svg class="feature-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 3h14l1.5 5H3.5z"/><path d="M3.5 8c0 1.4 1.1 2.5 2.5 2.5S8.5 9.4 8.5 8c0 1.4 1.1 2.5 2.5 2.5h2c1.4 0 2.5-1.1 2.5-2.5 0 1.4 1.1 2.5 2.5 2.5S20.5 9.4 20.5 8"/><path d="M5 10.5V21h14V10.5"/><path d="M10 21v-5h4v5"/></svg><h3>On the property</h3><p>The Baron and Prodigal Son restaurants, high-end shops and an aesthetic clinic.</p></div>
      <div class="feature"><svg class="feature-icon" viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="5" width="17" height="15.5" rx="2"/><path d="M3.5 10h17M8 3v4M16 3v4"/><path d="m9 15 2 2 4-4"/></svg><h3>Book direct</h3><p>Book here for our best available rate, with no platform fees.</p></div>
    </div>
  </div>
</section>

<section class="section alt" id="apartments">
  <div class="container">
    <div class="center">
      <div class="eyebrow">The apartments</div>
      <h2>Choose your apartment</h2>
      <p class="lead">We have two beautiful apartments, both beautifully furnished: a one-bedroom dream apartment with a penthouse feel, and a two-bedroom apartment that’s best for families and groups of friends.</p>
    </div>
    <div class="grid-2" style="margin-top:40px">{cards}
    </div>
  </div>
</section>

<section class="section" id="gallery">
  <div class="container">
    <div class="center">
      <div class="eyebrow">Gallery</div>
      <h2>Life at The Arch</h2>
      <p class="lead">Tap any photo to see it full size.</p>
    </div>
    {gallery([("images/arch/courtyard.jpg","The courtyard and lawn at Umhlanga Arch"),("images/building/view-south.jpg","Ocean view along the coast from The Arch"),("images/arch/the-baron.jpg","The Baron bar and grill at Umhlanga Arch"),("images/arch/shopping.jpg","Shopping on the Arch high street"),("images/arch/lawn.jpg","The lawn and shops at Umhlanga Arch"),("images/arch/promenade.jpg","Strolling the Arch precinct"),("images/apartment-1/balcony-view.jpg","Balcony view over Umhlanga")]).replace('class="gallery"','class="gallery gallery-7"')}
  </div>
</section>

<section class="section alt" id="location">
  <div class="container grid-2" style="align-items:center">
    <div>
      <div class="eyebrow">Location</div>
      <h2>The best of Umhlanga on your doorstep</h2>
      <p>Umhlanga Arch is an iconic mixed-use development in Ridgeside, Umhlanga Ridge. On the property you’ll find The Baron and Prodigal Son restaurants, high-end shops, an aesthetic clinic and a Hilton Garden Inn. Below you, the coast stretches from Umhlanga’s famous lighthouse to the Durban skyline, with beaches, shopping and some of KwaZulu-Natal’s best restaurants just a short drive away.</p>
      <ul class="nearby">
        <li><span>The Baron, Prodigal Son &amp; high-end shops</span><span>On the property</span></li>
        <li><span>Gateway Theatre of Shopping</span><span>approx. 5 min drive</span></li>
        <li><span>Umhlanga Village, beach &amp; promenade</span><span>approx. 10 min drive</span></li>
        <li><span>King Shaka International Airport</span><span>approx. 15 min drive</span></li>
        <li><span>Durban city centre &amp; uShaka Marine World</span><span>approx. 25 min drive</span></li>
      </ul>
    </div>
    <a class="map-card" href="https://www.google.com/maps/search/?api=1&amp;query=Umhlanga+Arch+1+Ncondo+Place+Umhlanga" target="_blank" rel="noopener">
      {img("images/building/view-south.jpg","View along the coast from Umhlanga Arch")}
      <span class="map-card-label">Umhlanga Arch, 1 Ncondo Place<span>Open in Google Maps →</span></span>
    </a>
  </div>
</section>

<section class="section">
  <div class="container grid-2" style="align-items:center">
    <div class="map-wrap" style="aspect-ratio:4/3">{img("images/guide/umhlanga-beach.jpg","Umhlanga beach and lighthouse")}</div>
    <div>
      <div class="eyebrow">Explore</div>
      <h2>Things to do in Umhlanga</h2>
      <p>From sunrise walks along the promenade to the lighthouse, to sharks, safaris and the Valley of a Thousand Hills, there’s plenty to see from your base at The Arch.</p>
      <a class="btn" href="things-to-do.html">See our local guide</a>
    </div>
  </div>
</section>

<section class="section alt" id="faq">
  <div class="container">
    <div class="center">
      <div class="eyebrow">Good to know</div>
      <h2>Frequently asked questions</h2>
    </div>
    <div class="faq">
      <details><summary>Where exactly is The Arch?</summary><p>Both apartments are in Umhlanga Arch, 1 Ncondo Place, Ridgeside, Umhlanga, KwaZulu-Natal. Full arrival instructions are sent with your booking confirmation.</p></details>
      <details><summary>Can we book both apartments together?</summary><p>Yes. Both apartments are in the same building, which makes them ideal for families and groups who want to be together but still have their own space. Simply book each apartment for the same dates.</p></details>
      <details><summary>Which apartment should I choose?</summary><p>The 2 Bedroom Luxury Sea View Apartment has a king room and a twin room and sleeps up to four, so it’s best for families and groups of friends. The Dream View Apartment is a one-bedroom apartment with a penthouse feel and 180-degree ocean views, ideal for couples or a special trip.</p></details>
      <details><summary>What time are check-in and check-out?</summary><p>Check-in is between 15:00 and 21:00, and check-out is before 10:00.</p></details>
      <details><summary>Is there parking?</summary><p>The Luxury Sea View Apartment comes with up to two parking bays. For the Dream View Apartment, let us know when you book if you’re arriving by car and we’ll send you the parking details.</p></details>
      <details><summary>Is the building secure?</summary><p>Yes. Umhlanga Arch has biometric access control, 24-hour CCTV and 24-hour security on the ground floor, plus a professional concierge service.</p></details>
      <details><summary>Is the apartment cleaned during my stay?</summary><p>As holiday apartments we don’t offer daily cleans, but if you’d like your apartment cleaned during your stay, just speak to the concierge and arrange payment through them.</p></details>
      <details><summary>Why book direct rather than through Airbnb?</summary><p>Booking direct means no platform service fees, so you get our best available rate, and you deal with us personally from enquiry to check-out.</p></details>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Ready to stay at The Arch Apartments?</h2>
    <p class="lead" style="margin:0 auto">Check live availability and book either apartment directly.</p>
    <div class="btn-row">
      <a class="btn light" data-book="apartment-1" href="book.html">Book the <span data-apt-name="apartment-1">Luxury Sea View Apartment</span></a>
      <a class="btn light" data-book="apartment-2" href="book.html">Book the <span data-apt-name="apartment-2">Dream View Apartment</span></a>
    </div>
  </div>
</section>
''' + FOOT
import re as _re, html as _h
_faq = [{'@type':'Question','name':_h.unescape(_re.sub('<[^>]+>','',q)),'acceptedAnswer':{'@type':'Answer','text':_h.unescape(_re.sub('<[^>]+>','',a))}} for q,a in _re.findall(r'<details><summary>(.*?)</summary><p>(.*?)</p></details>', idx)]
idx = idx.replace('</head>', '  <script type="application/ld+json">'+_j.dumps({'@context':'https://schema.org','@type':'FAQPage','mainEntity':_faq}, ensure_ascii=False)+'</script>\n</head>',1)
open('index.html','w').write(idx)

# ---------- apartment pages ----------
import re as _re2, html as _h2
for k, a in APTS.items():
    facts = ''.join(f'<li>{f}</li>' for f in a['facts'])
    about = '\n      '.join(f'<p>{p}</p>' for p in a['about'])
    space = ''.join(f'\n        <li><span>{x}</span><span>{y}</span></li>' for x, y in a['space'])
    amen = ''.join(f'<li>{x}</li>' for x in a['amen'])
    _apt = {'@context':'https://schema.org','@type':'Apartment','name':a['name'],'description':' '.join(_re2.sub('<[^>]+>','',x) for x in a['about'][:1]),'url':SITE_URL+k+'.html','image':[SITE_URL+f'images/{k}/{f}' for f,_ in a['photos'][:5]],'numberOfBedrooms':a['beds'],'numberOfBathroomsTotal':a['baths'],'occupancy':{'@type':'QuantitativeValue','maxValue':a['maxn']},'petsAllowed':False,'address':ADDR,'containedInPlace':{'@id':SITE_URL+'#business'},'amenityFeature':[{'@type':'LocationFeatureSpecification','name':_h2.unescape(x),'value':True} for x in a['amen']]}
    pg = head(f'{a["name"]} | Umhlanga Holiday Apartment | The Arch Apartments', a['seo'], path=k+'.html', image=f'images/{k}/cover.jpg', schema=[_apt, crumbs(('Home',''),(a['name'],k+'.html'))])
    pg += f'''
<section class="apt-hero">
  <div class="container">
    <div class="eyebrow"><a href="index.html">The Arch Apartments</a> · Umhlanga Ridge</div>
    <h1 data-apt-name="{k}">{a["name"]}</h1>
    <p class="lead">{a["tagline"]}</p>
    <ul class="facts">{facts}</ul>
    {gallery([(f"images/{k}/{f}", t) for f, t in a["photos"]])}
  </div>
</section>

<section class="section" style="padding-top:40px">
  <div class="container apt-layout">
    <div>
      <h2>About this apartment</h2>
      {about}
      <p>Also at The Arch: the <a href="{a["other"]}.html" data-apt-name="{a["other"]}">{a["other_name"]}</a>. Larger groups can book both and stay in the same building.</p>

      <h3 style="margin-top:1.5em">The space</h3>
      <ul class="rules">{space}
      </ul>

      <h3 style="margin-top:1.5em">What this place offers</h3>
      <ul class="amenities">{amen}</ul>

      <h3>House rules</h3>
      <ul class="rules">
        <li><span>Check-in</span><span>15:00 – 21:00</span></li>
        <li><span>Check-out</span><span>Before 10:00</span></li>
        <li><span>Guests</span><span>{a["maxguests"]}</span></li>
        <li><span>Smoking</span><span>Not allowed</span></li>
        <li><span>Parties or events</span><span>Not allowed</span></li>
        <li><span>Cleaning</span><span>No daily cleans; extra cleans can be booked via the concierge</span></li>
        <li><span>Building</span><span>Please respect quiet hours for neighbours</span></li>
      </ul>

      <h3 style="margin-top:2em" id="availability">Availability</h3>
      <div data-embed="{k}">
        <p>See live availability and prices for the <span data-apt-name="{k}">{a["name"]}</span>.</p>
        <a class="btn" data-book="{k}" href="book.html">Check availability &amp; book</a>
      </div>
    </div>

    <aside class="book-panel">
      <h3 data-apt-name="{k}">{a["name"]}</h3>
      <p style="color:var(--muted)">Book direct for our best rate, with no platform fees.</p>
      <a class="btn" data-book="{k}" href="book.html">Book now</a>
      <a class="btn ghost" href="{a["other"]}.html">View the <span data-apt-name="{a["other"]}">{a["other_name"]}</span></a>
      <small>Prefer Airbnb? <a data-airbnb="{k}" href="#">View on Airbnb</a></small>
    </aside>
  </div>
</section>
''' + FOOT
    open(f'{k}.html','w').write(pg)

# ---------- book ----------
bk = head('Book Direct | The Arch Apartments, Umhlanga', 'Book the 2 Bedroom Luxury Sea View Apartment or the Dream View Apartment at Umhlanga Arch directly for the best rate, with no platform fees.', path='book.html', schema=[crumbs(('Home',''),('Book','book.html'))])
choice = ''
for k, a in APTS.items():
    choice += f'''
      <article class="card book-choice">
        {img(f"images/{k}/cover.jpg", a["name"], "card-media")}
        <div class="card-body">
          <h3 data-apt-name="{k}">{a["name"]}</h3>
          <p style="color:var(--muted)">{a["tagline"]}</p>
          <div data-embed="{k}" style="width:100%"></div>
          <div class="btn-row" style="justify-content:center">
            <a class="btn" data-book="{k}" href="#">Check availability</a>
            <a class="btn ghost" href="{k}.html">Details</a>
          </div>
        </div>
      </article>'''
bk += f'''
<section class="section">
  <div class="container">
    <div class="center">
      <div class="eyebrow">Book direct</div>
      <h1 style="font-size:clamp(2.2rem,5vw,3.4rem)">Book your stay</h1>
      <p class="lead">Choose an apartment to check live availability and book securely. Travelling as a group? Book both apartments for the same dates.</p>
    </div>
    <div class="grid-2" style="margin-top:40px">{choice}
    </div>
    <p class="center" style="margin-top:40px;color:var(--muted)">Questions before you book? <a data-whatsapp href="https://wa.me/27837142186">WhatsApp us</a> or email <a data-email href="mailto:explorecape@gmail.com">explorecape@gmail.com</a>.</p>
  </div>
</section>
''' + FOOT
open('book.html','w').write(bk)

# ---------- things to do ----------
G = 'images/guide/'
FEATURED = [
  ('Umhlanga Promenade &amp; Lighthouse', 'approx. 10 min drive', G+'promenade-lighthouse.jpg', 'Walk or jog the paved promenade that runs along the beachfront past the famous red-and-white Umhlanga Lighthouse. It’s at its best at sunrise, when the sun comes up straight out of the ocean, and the promenade leads you past cafés, rock pools and the pier.'),
  ('Umhlanga Main Beach', 'approx. 10 min drive', G+'umhlanga-beach.jpg', 'Golden sand and warm water most of the year, with lifeguards on duty and shark nets protecting the main bathing areas. Explore the rock pools at low tide, and always swim between the flags.'),
  ('Umhlanga Lagoon Nature Reserve', 'approx. 10 min drive', G+'lagoon-reserve.jpg', 'A shady boardwalk winds through coastal dune forest to the lagoon mouth and a quiet stretch of beach. Look out for birds, monkeys and the odd duiker along the way.'),
  ('Chartwell Drive', 'approx. 10 min drive', G+'chartwell-drive.jpg', 'The heart of Umhlanga village and home to some of the best restaurants and nightlife on the coast, from relaxed breakfast spots and coffee shops to cocktail bars and fine dining.'),
  ('High tea or a meal at The Oyster Box', 'approx. 10 min drive', G+'oyster-box.jpg', 'This landmark hotel overlooking the lighthouse is famous for its afternoon high tea and its curry buffet, a true Durban institution. Book ahead for a table with a sea view.'),
  ('On the property', 'At Umhlanga Arch', 'images/building/arch-exterior.jpg', 'Dress up for a night out at The Baron or enjoy a meal at Prodigal Son, browse the high-end shops, or book a treatment at the aesthetic clinic, all without leaving Umhlanga Arch.'),
]
def maps(q):
    return 'https://www.google.com/maps/search/?api=1&amp;query=' + q.replace(' ', '+')
SECTIONS = [
  ('Where to eat', 'Our favourite restaurants in and around Umhlanga. Book ahead for weekends and holidays.', [
    ('Prodigal Son', 'On the property', 'Right here at Umhlanga Arch, so a great dinner is only a lift ride away.', maps('Prodigal Son Umhlanga Arch')),
    ('Mitera', 'Umhlanga', 'One of our top picks for a meal out in Umhlanga.', maps('Mitera Umhlanga')),
    ('Marco’s', 'Chartwell Drive', 'A local favourite in Umhlanga village for wood-fired pizzas and fresh pasta. Don’t miss half-price pizza on Thursday nights.', maps('Marcos Italian Umhlanga')),
    ('The Oyster Box', 'By the lighthouse', 'The landmark hotel on the beachfront, famous for its curry buffet, high tea and sea views.', maps('The Oyster Box Umhlanga')),
    ('The Chef’s Table', 'Umhlanga', 'One of the area’s best fine-dining experiences, with a seasonal menu built on KwaZulu-Natal produce and an open kitchen.', maps('The Chefs Table Umhlanga')),
    ('Lupa Osteria', 'Lighthouse Mall', 'A relaxed Italian osteria serving pizza, pasta, seafood and grills.', maps('Lupa Osteria Umhlanga')),
  ]),
  ('Best coffee', 'Where we go for our morning coffee.', [
    ('Tiki Tonga', 'Chartwell Drive', 'A coffee roaster in Umhlanga village with rich, strong blends, outdoor seating and early opening hours.', maps('Tiki Tonga Coffee Umhlanga')),
    ('Daily Dose', 'Umhlanga', 'A local favourite for a great cup to start the day.', maps('Daily Dose Coffee Umhlanga')),
    ('Now Coffee', 'Glenashley', 'Our favourite coffee, and well worth the short drive to Glenashley.', maps('Now Coffee Glenashley')),
    ('Seattle Coffee Co.', 'Umhlanga', 'A dependable spot for a coffee and a quick bite.', maps('Seattle Coffee Umhlanga')),
  ]),
  ('Spas &amp; wellness', 'Treat yourself during your stay.', [
    ('The Spa at The Oyster Box', 'By the lighthouse', 'An award-winning spa in tropical gardens, with a hammam and hydrotherapy baths.', maps('Oyster Box Spa Umhlanga')),
    ('Skin Renewal Umhlanga', 'At Umhlanga Arch', 'Skin and body treatments without leaving the building.', maps('Skin Renewal Umhlanga Arch')),
    ('Fleur De Lis Spa', 'Walking distance', 'Massages, body wraps and a sauna in the Coastlands Skye building, right across the road from The Arch.', maps('Fleur De Lis Spa Coastlands Skye Umhlanga')),
  ]),
  ('Gyms &amp; fitness', 'Keep up your routine while you’re away.', [
    ('Virgin Active Gateway', 'approx. 5 min drive', 'A full health club at Gateway with a heated 25 m pool, classes and personal trainers. Check with the club about visitor access.', 'https://www.virginactive.co.za/gyms/gateway'),
    ('Fit24 Oceans Mall', 'Oceans Mall', 'A gym at Oceans Mall in Umhlanga, close to the beachfront.', maps('Fit24 Oceans Mall Umhlanga')),
  ]),
  ('Shopping &amp; getting around', '', [
    ('Gateway Theatre of Shopping', 'approx. 5 min drive', 'One of the biggest shopping centres in the southern hemisphere, with hundreds of shops, cinemas and restaurants.', maps('Gateway Theatre of Shopping')),
    ('King Shaka International Airport', 'approx. 15 min drive', 'An easy 15-minute drive, so you can be on your balcony soon after you land.', maps('King Shaka International Airport')),
  ]),
  ('Day trips', 'Easy outings from Umhlanga for a day of exploring.', [
    ('uShaka Marine World', 'approx. 25 min drive', 'Africa’s largest aquarium, with a water park, marine shows and a shipwreck to explore. A hit with children.', maps('uShaka Marine World')),
    ('Ballito &amp; the Dolphin Coast', 'approx. 25 min drive', 'Quieter beaches, rock pools and seaside restaurants up the North Coast, with dolphins often spotted offshore.', maps('Ballito')),
    ('Valley of a Thousand Hills', 'approx. 50 min drive', 'Rolling hills, craft markets, Zulu cultural experiences and country restaurants inland from Durban.', maps('Valley of a Thousand Hills')),
    ('Midlands Meander', 'approx. 1.5 hr drive', 'A scenic route through the KwaZulu-Natal Midlands, dotted with farm stalls, craft studios, cheese and chocolate makers, breweries and country cafés.', maps('Midlands Meander')),
    ('Big Five safari at Hluhluwe-iMfolozi', 'approx. 3 hr drive', 'Africa’s oldest proclaimed game reserve and home of the Big Five. Go for a long weekend or join a guided day tour.', maps('Hluhluwe-iMfolozi Park')),
  ]),
]
import json as _json
_LIC = {'CC BY 2.0':'https://creativecommons.org/licenses/by/2.0/','CC BY-SA 2.0':'https://creativecommons.org/licenses/by-sa/2.0/','CC BY-SA 4.0':'https://creativecommons.org/licenses/by-sa/4.0/','CC0':'https://creativecommons.org/publicdomain/zero/1.0/'}
from html import escape as _esc
_cr = _json.load(open('images/guide/credits.json'))
_items = ''.join(f'<li>{_esc(v["title"])} by {_esc(v["creator"])}, <a href="{v["page"]}" target="_blank" rel="noopener">source</a>, <a href="{_LIC.get(v["license"], v["page"])}" target="_blank" rel="noopener">{v["license"]}</a></li>' for v in _cr.values())
credits_html = f'''<section class="credits">
  <div class="container">
    <details><summary>Photo credits</summary><ul>{_items}</ul><p>Photos have been resized and cropped.</p></details>
  </div>
</section>'''
tt = head('Things to Do in Umhlanga: Local Guide | The Arch Apartments', 'Our local guide to Umhlanga: beaches, the best restaurants and coffee, spas, gyms, shopping and day trips from The Arch Apartments in Umhlanga Ridge.', path='things-to-do.html', image='images/building/hero-beach.jpg', schema=[crumbs(('Home',''),('Things to do in Umhlanga','things-to-do.html'))])
feat = ''.join(f"""
      <details class="place">
        <summary>
          <span class="place-media">{img(i, n)}<span class="place-label"><span class="place-title">{n}</span><span class="place-time">{t}</span></span></span>
          <span class="place-more">Read more</span>
        </summary>
        <p>{d}</p>
      </details>""" for n, t, i, d in FEATURED)
import re as _re
def slug(n):
    return _re.sub(r'[^a-z0-9]+', '-', _re.sub(r'&amp;', 'and', n.lower()).replace('’', '')).strip('-')
def tip_img(n):
    return img(f'images/guide/{slug(n)}.jpg', n, 'tip-img')
def has_img(n):
    return os.path.exists(f'images/guide/{slug(n)}.jpg')
sections_html = ''
for i, (title, intro, items) in enumerate(SECTIONS):
    pics = all(has_img(n) for n, *_ in items)
    cards_ = ''.join(f"""
      <article class="tip">{tip_img(n) if pics else ''}<div class="tip-body"><h3>{n}</h3><div class="tip-meta">{t}</div><p>{d}</p><a href="{u}" target="_blank" rel="noopener">{'Visit website' if 'google.com/maps' not in u else 'View on map'} →</a></div></article>""" for n, t, d, u in items)
    intro_html = f'<p class="lead">{intro}</p>' if intro else ''
    sections_html += f"""
<section class="section{' alt' if i % 2 == 0 else ''}">
  <div class="container">
    <h2>{title}</h2>
    {intro_html}
    <div class="tip-grid" style="--cols:{4 if len(items) == 4 else 3}">{cards_}
    </div>
  </div>
</section>
"""
tt += f"""
<section class="hero hero-short">
  {img("images/building/hero-beach.jpg", "Umhlanga beach and lighthouse on a sunny day", "hero-media")}
  <div class="container hero-content">
    <div class="eyebrow">Local guide</div>
    <h1>Things to do in Umhlanga</h1>
    <p>Our favourite ways to spend your days while staying at The Arch. Tap any place to find out more.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2>Our favourites</h2>
    <div class="place-grid">{feat}
    </div>
  </div>
</section>

{sections_html}

{credits_html}
<section class="cta-band">
  <div class="container">
    <h2>Make The Arch your base</h2>
    <p class="lead" style="margin:0 auto">Two sea-view apartments, minutes from everything on this list.</p>
    <div class="btn-row">
      <a class="btn light" href="book.html">Check availability</a>
      <a class="btn outline-light" href="index.html#apartments">See the apartments</a>
    </div>
  </div>
</section>
""" + FOOT
open('things-to-do.html','w').write(tt)

print('ok')
import datetime as _dt
_today = _dt.date.today().isoformat()
_pri = {'':'1.0','apartment-1.html':'0.9','apartment-2.html':'0.9','book.html':'0.8','things-to-do.html':'0.7'}
open('sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{SITE_URL}{u}</loc><lastmod>{_today}</lastmod><priority>{_pri.get(u,"0.5")}</priority></url>\n' for u in PAGES) + '</urlset>\n')
open('robots.txt','w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n')
print('ok')
