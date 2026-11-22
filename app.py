"""
Faran Sports – Flask Application
"""

import os
from flask import Flask, render_template, request, jsonify
from models import (
    STORE_INFO, SUB_BRANDS, CATEGORIES, CATEGORY_MAP,
    BRANDS, BRAND_MAP, PRODUCTS, PRODUCT_MAP,
    TESTIMONIALS, get_products, get_product, get_related_products,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "app", "templates")
STATIC_DIR = os.path.join(BASE_DIR, "app", "static")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "faran-sports-secret-key-prod")
app.config["DEBUG"] = False


# ── Context processor – inject globals into every template ────────────────────
@app.context_processor
def inject_globals():
    return dict(
        store=STORE_INFO,
        categories=CATEGORIES,
        brands=BRANDS,
        sub_brands=SUB_BRANDS,
    )


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def home():
    """Home page – hero, about, categories, products, brands, testimonials, contact."""
    featured_products = PRODUCTS[:8]  # first 8 as featured
    return render_template(
        "index.html",
        featured_products=featured_products,
        testimonials=TESTIMONIALS,
    )


@app.route("/products")
def products_page():
    """Product listing with optional category / brand / sort query params."""
    category = request.args.get("category", "")
    brand = request.args.get("brand", "")
    sort = request.args.get("sort", "")
    filtered = get_products(
        category=category or None,
        brand=brand or None,
        sort=sort or None,
    )
    active_category = CATEGORY_MAP.get(category)
    active_brand = BRAND_MAP.get(brand)
    return render_template(
        "products.html",
        products=filtered,
        active_category=active_category,
        active_brand=active_brand,
        current_category=category,
        current_brand=brand,
        current_sort=sort,
    )


@app.route("/product/<int:product_id>")
def product_detail(product_id):
    """Individual product page."""
    product = get_product(product_id)
    if not product:
        return render_template("404.html"), 404
    related = get_related_products(product_id)
    return render_template(
        "product_detail.html",
        product=product,
        related_products=related,
        category=CATEGORY_MAP.get(product["category"]),
    )


@app.route("/about")
def about():
    """About Faran Sports ecosystem."""
    return render_template("about.html")


@app.route("/contact")
def contact():
    """Contact page with WhatsApp integration."""
    return render_template("contact.html")


# ── API ───────────────────────────────────────────────────────────────────────

@app.route("/api/products")
def api_products():
    """JSON API for AJAX product filtering."""
    category = request.args.get("category", "")
    brand = request.args.get("brand", "")
    sort = request.args.get("sort", "")
    filtered = get_products(
        category=category or None,
        brand=brand or None,
        sort=sort or None,
    )
    return jsonify(
        {
            "count": len(filtered),
            "products": filtered,
        }
    )


# ── Error handlers ────────────────────────────────────────────────────────────

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# ── Run ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
