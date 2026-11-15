# Faran Sports — Premier Sports & Fitness Digital Storefront

A modern, animated, and personalized web application for **Faran Sports** (Kanpur, Uttar Pradesh), featuring seamless **WhatsApp-based purchasing**, dynamic product filtering, interactive canvas animations, and dedicated showcases for all business verticals.

---

## 🌟 Store Information & Verticals

- **Name:** Faran Sports
- **Location:** Kanpur, Uttar Pradesh, India
- **Official WhatsApp:** `+91 8840185575`
- **Email:** `faransports@gmail.com`

### The 4 Ecosystem Pillars:
1. **Faran Sports (Flagship Retail):** Authorized retailer for Cricket, Badminton, Football, Running, and Table Tennis gear from world-renowned brands (SG, SS, Yonex, Cosco, Nivia, Stag, Adidas, Nike, Puma).
2. **Faran Supplement House (Retail & Wholesale):** 100% verified, authentic sports nutrition — Whey Protein, Mass Gainers, BCAAs, and Pre-Workouts with bulk rates for fitness centres and trainers.
3. **Faran Gym House:** Commercial gym facility setup, machine ergonomics consultation, and fitness memberships in Kanpur.
4. **AB Strong (Powered By Faran Sports):** In-house heavy-duty gym equipment manufacturing — cast-iron dumbbells, Olympic barbells, flat/incline benches, power racks, and plates.

---

## 🚀 Local Development

### 1. Requirements
Ensure Python 3.8+ is installed on your system.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Flask Server
```bash
python app.py
```

Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

---

## ☁️ Deployment Guides

### Option 1: Deploy on Vercel (Ready Out-of-the-Box)

The project includes `vercel.json`, `api/index.py`, and `.vercelignore` pre-configured for Vercel Serverless Python runtime.

#### Method A: Deploy via Vercel CLI
```bash
npm i -g vercel
cd faran-sports
vercel
```
Follow the prompts (defaults are automatically recognized). For production:
```bash
vercel --prod
```

#### Method B: Deploy via GitHub
1. Push your repository to GitHub.
2. Log into [vercel.com](https://vercel.com) and click **"Add New Project"**.
3. Select your repository.
4. Leave build settings as default (Vercel automatically detects `vercel.json` and Python requirements).
5. Click **"Deploy"**.

---

### Option 2: Deploy with Gunicorn / Procfile (Render, Heroku, Railway)

The repository includes a production `Procfile` configured with `gunicorn`:
```
web: gunicorn app:app
```

#### Test Gunicorn Locally (Linux/macOS or WSL)
```bash
gunicorn app:app --bind 0.0.0.0:5000 --workers 4
```

#### Deploy on Render / Railway
1. Connect your GitHub repository.
2. Select **Web Service**.
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `gunicorn app:app` (or it will auto-detect from `Procfile`).

---

## 🔒 Production Configuration

- **Debug Mode:** Explicitly disabled (`debug=False`).
- **Port Binding:** Dynamically binds to `os.environ.get("PORT", 5000)`.
- **Host:** Binds to `0.0.0.0` for cloud container compatibility.
- **Environment Variables (Optional):**
  - `SECRET_KEY`: Set your custom secret key in your hosting dashboard.
  - `PORT`: Automatically set by Vercel/Render/Heroku.

---

## 📂 Project Architecture

```
faran-sports/
├── app.py                      # Production Flask app (debug=False, PORT binding)
├── models.py                   # Product data, categories, brands & WhatsApp URLs
├── requirements.txt            # Dependencies including gunicorn
├── Procfile                    # Web process command (gunicorn app:app)
├── vercel.json                 # Vercel serverless routing configuration
├── .vercelignore               # Ignored files for Vercel builds
├── .gitignore                  # Git ignore rules
├── generate_images.py          # SVG graphics generator for sport & product cards
├── README.md                   # Project & deployment documentation
├── api/
│   └── index.py                # Vercel serverless function entrypoint
└── app/
    ├── static/
    │   ├── css/
    │   │   └── style.css       # Kombai-inspired responsive stylesheet
    │   ├── js/
    │   │   ├── main.js         # Interactivity, search modal & filters
    │   │   └── particles.js    # Canvas particle animation system
    │   └── images/             # Vector SVGs & placeholders for all 20+ products
    └── templates/
        ├── base.html           # Master layout with preloader, nav, search & footer
        ├── index.html          # Kombai Hero Triptych, Bento 4-Pillars & Showroom card
        ├── products.html       # Full catalog with category/brand filters & views
        ├── product_detail.html # Product page with gallery, size selector & WhatsApp order
        ├── about.html          # Deep dive into the 4 Faran Group pillars
        ├── contact.html        # Interactive WhatsApp inquiry form & Kanpur showroom details
        └── 404.html            # Themed 404 page
```
