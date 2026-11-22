"""
Data models for Faran Sports website.
All data stored as Python dicts/lists (no database yet).
"""

# ── Store Information ─────────────────────────────────────────────────────────
STORE_INFO = {
    "name": "Faran Sports",
    "tagline": "Your Ultimate Sports Destination in Kanpur",
    "city": "Kanpur",
    "state": "Uttar Pradesh",
    "whatsapp": "918840185575",
    "whatsapp_display": "8840185575",
    "whatsapp_link": "https://wa.me/918840185575",
    "email": "faransports@gmail.com",
    "address": "Faran Sports, Kanpur, Uttar Pradesh, India",
    "description": (
        "Faran Sports is Kanpur's premier sports equipment destination, "
        "offering top-quality gear across Cricket, Badminton, Football, "
        "Gym Equipment, Fitness Supplements, Running, and Table Tennis. "
        "We are committed to fueling every athlete's journey."
    ),
}

# ── Sub-Brands / Ecosystem ───────────────────────────────────────────────────
SUB_BRANDS = [
    {
        "name": "Faran Sports",
        "slug": "faran-sports",
        "icon": "fa-solid fa-baseball-bat-ball",
        "description": (
            "The flagship store for all sports equipment — cricket bats, "
            "badminton rackets, footballs, running shoes, and much more."
        ),
    },
    {
        "name": "Faran Supplement House",
        "slug": "faran-supplement-house",
        "icon": "fa-solid fa-dumbbell",
        "description": (
            "Retail & wholesale supplier of genuine fitness supplements — "
            "whey protein, mass gainers, BCAAs, and pre-workouts from "
            "trusted brands."
        ),
    },
    {
        "name": "Faran Gym House",
        "slug": "faran-gym-house",
        "icon": "fa-solid fa-person-running",
        "description": (
            "Complete gym setup solutions — cardio machines, weight plates, "
            "benches, functional trainers, and commercial gym equipment."
        ),
    },
    {
        "name": "AB Strong Powered By Faran Sports",
        "slug": "ab-strong",
        "icon": "fa-solid fa-bolt",
        "description": (
            "Our own brand of premium gym equipment engineered for "
            "durability, performance, and affordability."
        ),
    },
]

# ── Categories ────────────────────────────────────────────────────────────────
CATEGORIES = [
    {"slug": "cricket", "name": "Cricket", "icon": "fa-solid fa-baseball-bat-ball",
     "image_placeholder": "cricket.jpg",
     "description": "Professional cricket gear from top Indian and international brands."},
    {"slug": "badminton", "name": "Badminton", "icon": "fa-solid fa-shuttlecock",
     "image_placeholder": "badminton.jpg",
     "description": "Rackets, shuttlecocks, shoes, and accessories for every level."},
    {"slug": "football", "name": "Football", "icon": "fa-solid fa-futbol",
     "image_placeholder": "football.jpg",
     "description": "Match balls, boots, jerseys, shin guards and training gear."},
    {"slug": "gym-equipment", "name": "Gym Equipment", "icon": "fa-solid fa-dumbbell",
     "image_placeholder": "gym.jpg",
     "description": "Home and commercial gym machines, weights, and accessories."},
    {"slug": "fitness-supplements", "name": "Fitness Supplements", "icon": "fa-solid fa-capsules",
     "image_placeholder": "supplements.jpg",
     "description": "100 % genuine whey proteins, mass gainers, BCAAs, and more."},
    {"slug": "running", "name": "Running", "icon": "fa-solid fa-person-running",
     "image_placeholder": "running.jpg",
     "description": "Performance running shoes, apparel, and hydration gear."},
    {"slug": "table-tennis", "name": "Table Tennis", "icon": "fa-solid fa-table-tennis-paddle-ball",
     "image_placeholder": "table-tennis.jpg",
     "description": "Tables, paddles, balls, and nets for recreational and pro play."},
]

# helper look-up
CATEGORY_MAP = {c["slug"]: c for c in CATEGORIES}

# ── Brands ────────────────────────────────────────────────────────────────────
BRANDS = [
    {"slug": "sg", "name": "SG", "logo_placeholder": "sg.png"},
    {"slug": "ss", "name": "SS", "logo_placeholder": "ss.png"},
    {"slug": "yonex", "name": "Yonex", "logo_placeholder": "yonex.png"},
    {"slug": "cosco", "name": "Cosco", "logo_placeholder": "cosco.png"},
    {"slug": "nivia", "name": "Nivia", "logo_placeholder": "nivia.png"},
    {"slug": "ab-strong", "name": "AB Strong", "logo_placeholder": "ab-strong.png"},
    {"slug": "muscleblaze", "name": "MuscleBlaze", "logo_placeholder": "muscleblaze.png"},
    {"slug": "optimum-nutrition", "name": "Optimum Nutrition", "logo_placeholder": "on.png"},
    {"slug": "stag", "name": "Stag", "logo_placeholder": "stag.png"},
    {"slug": "adidas", "name": "Adidas", "logo_placeholder": "adidas.png"},
    {"slug": "nike", "name": "Nike", "logo_placeholder": "nike.png"},
    {"slug": "puma", "name": "Puma", "logo_placeholder": "puma.png"},
]

BRAND_MAP = {b["slug"]: b for b in BRANDS}


def _wa(product_name, price):
    """Build a WhatsApp order link with pre-filled message."""
    import urllib.parse
    msg = (
        f"Hi Faran Sports! 👋\n"
        f"I'm interested in: *{product_name}*\n"
        f"Listed Price: ₹{price:,}\n"
        f"Please share availability and delivery details. Thank you!"
    )
    return f"https://wa.me/{STORE_INFO['whatsapp']}?text={urllib.parse.quote(msg)}"


# ── Products ──────────────────────────────────────────────────────────────────
PRODUCTS = [
    # ── Cricket ───────────────────────────────────────────────────────────
    {
        "id": 1,
        "name": "SG Sunny Gold Cricket Bat",
        "slug": "sg-sunny-gold-bat",
        "category": "cricket",
        "sport": "Cricket",
        "brand": "sg",
        "price": 4299,
        "mrp": 5499,
        "discount": 22,
        "image_placeholder": "sg-sunny-gold.jpg",
        "description": (
            "The SG Sunny Gold is a classic English-willow cricket bat "
            "loved by club cricketers. Lightweight pickup, full-size profile, "
            "and a thick edge for powerful drives."
        ),
    },
    {
        "id": 2,
        "name": "SS Ton Reserve Edition Bat",
        "slug": "ss-ton-reserve",
        "category": "cricket",
        "sport": "Cricket",
        "brand": "ss",
        "price": 8999,
        "mrp": 12000,
        "discount": 25,
        "image_placeholder": "ss-ton-reserve.jpg",
        "description": (
            "Grade-1 English willow bat with a massive sweet spot and "
            "premium SS grip. Tournament-ready performance."
        ),
    },
    {
        "id": 3,
        "name": "SG Cricket Helmet – Aero Shield",
        "slug": "sg-aero-shield-helmet",
        "category": "cricket",
        "sport": "Cricket",
        "brand": "sg",
        "price": 2199,
        "mrp": 2999,
        "discount": 27,
        "image_placeholder": "sg-helmet.jpg",
        "description": (
            "Lightweight polycarbonate shell with titanium-grade steel grille. "
            "Comfortable padding and adjustable chin strap for a secure fit."
        ),
    },
    # ── Badminton ─────────────────────────────────────────────────────────
    {
        "id": 4,
        "name": "Yonex Astrox 88D Pro Racket",
        "slug": "yonex-astrox-88d",
        "category": "badminton",
        "sport": "Badminton",
        "brand": "yonex",
        "price": 7499,
        "mrp": 9990,
        "discount": 25,
        "image_placeholder": "yonex-astrox-88d.jpg",
        "description": (
            "Head-heavy attacking racket with Rotational Generator System for "
            "steep smashes. Strung with BG-65 at 24 lbs."
        ),
    },
    {
        "id": 5,
        "name": "Yonex Mavis 350 Shuttlecocks (6 pcs)",
        "slug": "yonex-mavis-350",
        "category": "badminton",
        "sport": "Badminton",
        "brand": "yonex",
        "price": 699,
        "mrp": 890,
        "discount": 21,
        "image_placeholder": "yonex-mavis-350.jpg",
        "description": (
            "Tournament-grade nylon shuttlecocks with consistent flight and "
            "superior durability. Medium speed (green cap)."
        ),
    },
    # ── Football ──────────────────────────────────────────────────────────
    {
        "id": 6,
        "name": "Nivia Storm Football – Size 5",
        "slug": "nivia-storm-football",
        "category": "football",
        "sport": "Football",
        "brand": "nivia",
        "price": 849,
        "mrp": 1099,
        "discount": 23,
        "image_placeholder": "nivia-storm.jpg",
        "description": (
            "Rubberised moulded football with excellent grip and air retention. "
            "Ideal for turf and hard-ground play."
        ),
    },
    {
        "id": 7,
        "name": "Cosco Milano Football – Size 5",
        "slug": "cosco-milano-football",
        "category": "football",
        "sport": "Football",
        "brand": "cosco",
        "price": 649,
        "mrp": 799,
        "discount": 19,
        "image_placeholder": "cosco-milano.jpg",
        "description": (
            "Hand-stitched PU football with 32-panel construction. "
            "Great touch and control on any surface."
        ),
    },
    {
        "id": 8,
        "name": "Nivia Encounter Football Shoes",
        "slug": "nivia-encounter-shoes",
        "category": "football",
        "sport": "Football",
        "brand": "nivia",
        "price": 1399,
        "mrp": 1799,
        "discount": 22,
        "image_placeholder": "nivia-encounter-shoes.jpg",
        "description": (
            "Lightweight synthetic-upper football studs with firm-ground soles. "
            "Snug fit for quick turns and sprints."
        ),
    },
    # ── Gym Equipment ─────────────────────────────────────────────────────
    {
        "id": 9,
        "name": "AB Strong Adjustable Dumbbells (Pair) – 20 kg",
        "slug": "ab-strong-adjustable-dumbbells-20",
        "category": "gym-equipment",
        "sport": "Gym",
        "brand": "ab-strong",
        "price": 3499,
        "mrp": 4999,
        "discount": 30,
        "image_placeholder": "ab-strong-dumbbells.jpg",
        "description": (
            "Cast-iron adjustable dumbbell set with rubber-grip handles. "
            "Includes weight plates from 1 kg to 5 kg for progressive overload."
        ),
    },
    {
        "id": 10,
        "name": "AB Strong Flat Bench Press",
        "slug": "ab-strong-flat-bench",
        "category": "gym-equipment",
        "sport": "Gym",
        "brand": "ab-strong",
        "price": 5999,
        "mrp": 7999,
        "discount": 25,
        "image_placeholder": "ab-strong-bench.jpg",
        "description": (
            "Heavy-duty flat bench with 300 kg load capacity. Powder-coated "
            "steel frame and high-density foam padding."
        ),
    },
    {
        "id": 11,
        "name": "AB Strong Olympic Barbell – 20 kg",
        "slug": "ab-strong-olympic-barbell",
        "category": "gym-equipment",
        "sport": "Gym",
        "brand": "ab-strong",
        "price": 4799,
        "mrp": 6499,
        "discount": 26,
        "image_placeholder": "ab-strong-barbell.jpg",
        "description": (
            "Chrome-plated 7-ft Olympic barbell with rotating sleeves and "
            "centre knurling. Ideal for squats, deadlifts, and bench press."
        ),
    },
    # ── Fitness Supplements ───────────────────────────────────────────────
    {
        "id": 12,
        "name": "MuscleBlaze Biozyme Whey Protein – 2 kg (Rich Chocolate)",
        "slug": "muscleblaze-biozyme-whey-2kg",
        "category": "fitness-supplements",
        "sport": "Fitness",
        "brand": "muscleblaze",
        "price": 3999,
        "mrp": 4999,
        "discount": 20,
        "image_placeholder": "mb-biozyme-whey.jpg",
        "description": (
            "Enhanced absorption whey protein with 25 g protein per serving. "
            "Added digestive enzymes for zero bloating. 100 % authentic."
        ),
    },
    {
        "id": 13,
        "name": "Optimum Nutrition Gold Standard Whey – 2 lbs",
        "slug": "on-gold-standard-whey-2lb",
        "category": "fitness-supplements",
        "sport": "Fitness",
        "brand": "optimum-nutrition",
        "price": 4599,
        "mrp": 5499,
        "discount": 16,
        "image_placeholder": "on-gold-standard.jpg",
        "description": (
            "World's #1 selling whey protein. 24 g protein, 5.5 g BCAAs per "
            "scoop. Double Rich Chocolate flavour."
        ),
    },
    {
        "id": 14,
        "name": "MuscleBlaze Mass Gainer XXL – 3 kg",
        "slug": "muscleblaze-mass-gainer-3kg",
        "category": "fitness-supplements",
        "sport": "Fitness",
        "brand": "muscleblaze",
        "price": 2499,
        "mrp": 3199,
        "discount": 22,
        "image_placeholder": "mb-mass-gainer.jpg",
        "description": (
            "High-calorie mass gainer with complex carbs and 20 g protein "
            "per serving. Chocolate flavour for hard gainers."
        ),
    },
    # ── Running ───────────────────────────────────────────────────────────
    {
        "id": 15,
        "name": "Adidas Runfalcon 3.0 Running Shoes",
        "slug": "adidas-runfalcon-3",
        "category": "running",
        "sport": "Running",
        "brand": "adidas",
        "price": 2999,
        "mrp": 3999,
        "discount": 25,
        "image_placeholder": "adidas-runfalcon.jpg",
        "description": (
            "Lightweight mesh-upper running shoes with Cloudfoam midsole for "
            "all-day cushioning. Perfect for daily runs and gym sessions."
        ),
    },
    {
        "id": 16,
        "name": "Nike Revolution 6 Running Shoes",
        "slug": "nike-revolution-6",
        "category": "running",
        "sport": "Running",
        "brand": "nike",
        "price": 3499,
        "mrp": 4495,
        "discount": 22,
        "image_placeholder": "nike-revolution-6.jpg",
        "description": (
            "Soft foam midsole, breathable knit upper, rubber outsole for "
            "road running. Versatile everyday trainer."
        ),
    },
    {
        "id": 17,
        "name": "Puma Velocity Nitro 2 Running Shoes",
        "slug": "puma-velocity-nitro-2",
        "category": "running",
        "sport": "Running",
        "brand": "puma",
        "price": 5499,
        "mrp": 7499,
        "discount": 27,
        "image_placeholder": "puma-velocity-nitro.jpg",
        "description": (
            "Nitrogen-infused NITRO foam for responsive cushioning. "
            "Engineered mesh and PUMAGRIP rubber outsole."
        ),
    },
    # ── Table Tennis ──────────────────────────────────────────────────────
    {
        "id": 18,
        "name": "Stag International Table Tennis Table",
        "slug": "stag-international-tt-table",
        "category": "table-tennis",
        "sport": "Table Tennis",
        "brand": "stag",
        "price": 18999,
        "mrp": 24999,
        "discount": 24,
        "image_placeholder": "stag-tt-table.jpg",
        "description": (
            "ITTF-approved 25 mm top with sturdy undercarriage and "
            "playback mode. Foldable with locking wheels for easy storage."
        ),
    },
    {
        "id": 19,
        "name": "Cosco Stiga 4-Star Table Tennis Racket",
        "slug": "cosco-stiga-4star-racket",
        "category": "table-tennis",
        "sport": "Table Tennis",
        "brand": "cosco",
        "price": 1299,
        "mrp": 1699,
        "discount": 24,
        "image_placeholder": "cosco-stiga-racket.jpg",
        "description": (
            "5-ply blade with ITTF-approved rubber on both sides. "
            "Excellent spin and control for intermediate players."
        ),
    },
    {
        "id": 20,
        "name": "Stag 3-Star Table Tennis Balls (Pack of 6)",
        "slug": "stag-3star-tt-balls",
        "category": "table-tennis",
        "sport": "Table Tennis",
        "brand": "stag",
        "price": 349,
        "mrp": 450,
        "discount": 22,
        "image_placeholder": "stag-tt-balls.jpg",
        "description": (
            "Competition-standard 40+ mm ABS balls. Consistent bounce and "
            "roundness for match play."
        ),
    },
]

# Add whatsapp_msg to every product
for _p in PRODUCTS:
    _p["whatsapp_msg"] = _wa(_p["name"], _p["price"])

PRODUCT_MAP = {p["id"]: p for p in PRODUCTS}


# ── Testimonials ──────────────────────────────────────────────────────────────
TESTIMONIALS = [
    {
        "id": 1,
        "name": "Rahul Verma",
        "sport": "Cricket",
        "avatar_placeholder": "avatar1.jpg",
        "rating": 5,
        "text": (
            "Bought an SG bat from Faran Sports — superb quality and the "
            "best price in Kanpur. Their WhatsApp ordering is so convenient!"
        ),
    },
    {
        "id": 2,
        "name": "Priya Sharma",
        "sport": "Badminton",
        "avatar_placeholder": "avatar2.jpg",
        "rating": 5,
        "text": (
            "Yonex rackets at genuine prices with proper warranty. "
            "Faran Sports is my go-to for all badminton gear."
        ),
    },
    {
        "id": 3,
        "name": "Amit Gupta",
        "sport": "Gym",
        "avatar_placeholder": "avatar3.jpg",
        "rating": 4,
        "text": (
            "Set up my entire home gym with AB Strong equipment from "
            "Faran Gym House. Great build quality and after-sales support."
        ),
    },
    {
        "id": 4,
        "name": "Sneha Tiwari",
        "sport": "Fitness",
        "avatar_placeholder": "avatar4.jpg",
        "rating": 5,
        "text": (
            "Finally a store in Kanpur that sells 100 % authentic supplements. "
            "Faran Supplement House is a blessing for fitness enthusiasts."
        ),
    },
    {
        "id": 5,
        "name": "Vikram Singh",
        "sport": "Football",
        "avatar_placeholder": "avatar5.jpg",
        "rating": 5,
        "text": (
            "Ordered Nivia football shoes on WhatsApp and received them the "
            "next day. Unbeatable service and pricing!"
        ),
    },
    {
        "id": 6,
        "name": "Deepak Yadav",
        "sport": "Running",
        "avatar_placeholder": "avatar6.jpg",
        "rating": 4,
        "text": (
            "Got Nike running shoes at a fantastic discount. The staff really "
            "knows their products and helped me pick the right fit."
        ),
    },
]


# ── Helper Functions ──────────────────────────────────────────────────────────

def get_products(category=None, brand=None, sort=None):
    """Return filtered & sorted product list."""
    results = PRODUCTS[:]
    if category:
        results = [p for p in results if p["category"] == category]
    if brand:
        results = [p for p in results if p["brand"] == brand]
    if sort == "price_asc":
        results.sort(key=lambda p: p["price"])
    elif sort == "price_desc":
        results.sort(key=lambda p: p["price"], reverse=True)
    elif sort == "discount":
        results.sort(key=lambda p: p["discount"], reverse=True)
    return results


def get_product(product_id):
    """Return a single product by id, or None."""
    return PRODUCT_MAP.get(product_id)


def get_related_products(product_id, limit=4):
    """Return products in the same category, excluding current."""
    product = get_product(product_id)
    if not product:
        return []
    return [
        p for p in PRODUCTS
        if p["category"] == product["category"] and p["id"] != product_id
    ][:limit]
