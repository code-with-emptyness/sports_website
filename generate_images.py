import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
images_dir = os.path.join(os.path.dirname(__file__), 'app', 'static', 'images')
os.makedirs(images_dir, exist_ok=True)

# Kombai-style athletic gradients and styling
categories = {
    'cricket': ('#d4ff00', '#10b981', '🏏', 'CRICKET PRO GEAR', 'English Willow Bats • SG & SS Club Editions'),
    'badminton': ('#00f0ff', '#0072ff', '🏸', 'BADMINTON ELITE', 'Yonex Astrox • Mavis 350 Shuttles • High-Tension'),
    'football': ('#ff007a', '#7928ca', '⚽', 'FOOTBALL PRECISION', 'Match Balls • Turf Studs • Nivia & Cosco'),
    'gym-equipment': ('#ff4d00', '#ff9900', '🏋️', 'AB STRONG GYM', 'Cast-Iron Dumbbells • Olympic Barbells • Benches'),
    'fitness-supplements': ('#f59e0b', '#d97706', '💊', 'FARAN SUPPLEMENTS', '100% Genuine Whey • Mass Gainers • Importer Tagged'),
    'running': ('#00dfd8', '#007cf0', '🏃', 'RUNNING & FITNESS', 'Cloud Cushion Shoes • Nike & Adidas Trainers'),
    'table-tennis': ('#7928ca', '#ff0080', '🏓', 'TABLE TENNIS PRO', 'ITTF Approved Tables • Stag & Stiga Rackets')
}

def make_kombai_svg(slug, color1, color2, emoji, title, subtitle):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="100%" height="100%">
  <defs>
    <radialGradient id="rg_{slug}" cx="50%" cy="40%" r="65%">
      <stop offset="0%" stop-color="{color1}" stop-opacity="0.25" />
      <stop offset="60%" stop-color="{color2}" stop-opacity="0.08" />
      <stop offset="100%" stop-color="#0a0a0c" stop-opacity="0" />
    </radialGradient>
    <linearGradient id="g_{slug}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{color1}" />
      <stop offset="100%" stop-color="{color2}" />
    </linearGradient>
    <pattern id="grid_{slug}" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="rgba(255,255,255,0.03)" stroke-width="1"/>
    </pattern>
  </defs>
  
  <!-- Base Background -->
  <rect width="100%" height="100%" fill="#0e0f12" />
  <rect width="100%" height="100%" fill="url(#grid_{slug})" />
  <rect width="100%" height="100%" fill="url(#rg_{slug})" />
  
  <!-- Outer Glow Ring -->
  <circle cx="300" cy="240" r="130" fill="none" stroke="url(#g_{slug})" stroke-width="1.5" stroke-opacity="0.3" stroke-dasharray="8 6" />
  
  <!-- Floating Glass Circle -->
  <circle cx="300" cy="240" r="105" fill="#14161b" stroke="rgba(255,255,255,0.12)" stroke-width="1.5" />
  <circle cx="300" cy="240" r="85" fill="url(#g_{slug})" opacity="0.12" />
  
  <!-- Main Sport Icon -->
  <text x="300" y="255" font-size="80" text-anchor="middle" dominant-baseline="central">{emoji}</text>
  
  <!-- Floating Spec Pill -->
  <rect x="180" y="375" width="240" height="30" rx="15" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.12)" stroke-width="1" />
  <circle cx="198" cy="390" r="4" fill="{color1}" />
  <text x="305" y="395" font-family="'Outfit', sans-serif" font-weight="700" font-size="11" fill="{color1}" letter-spacing="2" text-anchor="middle">FARAN PRO SERIES</text>
  
  <!-- Headline Typography -->
  <text x="300" y="445" font-family="'Outfit', sans-serif" font-weight="800" font-size="22" fill="#ffffff" letter-spacing="1" text-anchor="middle">{title}</text>
  <text x="300" y="480" font-family="'Inter', sans-serif" font-size="13" fill="#8e95a5" text-anchor="middle">{subtitle}</text>
  
  <!-- Bottom Accent Line -->
  <line x1="240" y1="515" x2="360" y2="515" stroke="url(#g_{slug})" stroke-width="2.5" stroke-linecap="round" />
</svg>"""

for slug, (c1, c2, em, tit, sub) in categories.items():
    svg_data = make_kombai_svg(slug, c1, c2, em, tit, sub)
    with open(os.path.join(images_dir, f"{slug}.jpg"), "w", encoding="utf-8") as f:
        f.write(svg_data)
    with open(os.path.join(images_dir, f"{slug}.svg"), "w", encoding="utf-8") as f:
        f.write(svg_data)

placeholder = make_kombai_svg("default", "#d4ff00", "#10b981", "⚡", "FARAN SPORTS", "Kanpur Showroom • WhatsApp: 8840185575")
with open(os.path.join(images_dir, "placeholder.svg"), "w", encoding="utf-8") as f:
    f.write(placeholder)

# Generate specific product cards
try:
    from models import PRODUCTS
    for p in PRODUCTS:
        img_name = p['image_placeholder']
        cat = p['category']
        c1, c2, em, _, _ = categories.get(cat, ('#d4ff00', '#10b981', '🏆', '', ''))
        clean_name = p['name'][:32].replace('&', '&amp;')
        brand_name = p['brand'].upper()
        p_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="100%" height="100%">
  <defs>
    <radialGradient id="prg_{p['id']}" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="{c1}" stop-opacity="0.22" />
      <stop offset="100%" stop-color="#0f1013" stop-opacity="0" />
    </radialGradient>
    <linearGradient id="pg_{p['id']}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{c1}" />
      <stop offset="100%" stop-color="{c2}" />
    </linearGradient>
  </defs>
  
  <rect width="100%" height="100%" fill="#111216" />
  <rect width="100%" height="100%" fill="url(#prg_{p['id']})" />
  
  <!-- Subtle border & inner corner highlight -->
  <rect x="15" y="15" width="570" height="570" rx="20" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="1.5" />
  
  <!-- Centered Floating Visual -->
  <circle cx="300" cy="225" r="110" fill="#17181e" stroke="rgba(255,255,255,0.08)" stroke-width="1.5" />
  <circle cx="300" cy="225" r="95" fill="url(#pg_{p['id']})" opacity="0.12" />
  <text x="300" y="240" font-size="80" text-anchor="middle" dominant-baseline="central">{em}</text>
  
  <!-- Brand Tag Badge -->
  <rect x="170" y="360" width="260" height="28" rx="14" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.12)" stroke-width="1" />
  <text x="300" y="379" font-family="'Outfit', sans-serif" font-weight="700" font-size="11" fill="{c1}" letter-spacing="2" text-anchor="middle">{brand_name} AUTHENTIC</text>
  
  <!-- Product Name & Price -->
  <text x="300" y="435" font-family="'Outfit', sans-serif" font-weight="800" font-size="19" fill="#ffffff" text-anchor="middle">{clean_name}</text>
  <text x="300" y="475" font-family="'Inter', sans-serif" font-size="17" fill="{c1}" font-weight="800" text-anchor="middle">₹{p['price']:,} <tspan fill="#64748b" font-size="13" font-weight="400" text-decoration="line-through">₹{p['mrp']:,}</tspan></text>
</svg>"""
        with open(os.path.join(images_dir, img_name), "w", encoding="utf-8") as f:
            f.write(p_svg)
except Exception as e:
    print(f"Error: {e}")

print("Kombai-grade SVG visuals generated!")
