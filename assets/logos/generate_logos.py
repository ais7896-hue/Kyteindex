# -*- coding: utf-8 -*-
"""
Kyte Suite Logo Generator
Generates SVG and transparent PNGs (512x512 & 1024x1024) for:
- Kyte Suite (Master Logo)
- KyteView
- KyteShelf
- KyteRename
Both App Icon (with squircle) and Symbol Only (without container) variants.
"""

import os
from pathlib import Path

# Paths
BASE_DIR = Path(r"d:\Noah\Antigravity專案程式專用\Kyteindex\assets\logos")
SVG_DIR = BASE_DIR / "svg"
PNG_512_DIR = BASE_DIR / "png-512"
PNG_1024_DIR = BASE_DIR / "png-1024"

for d in [SVG_DIR, PNG_512_DIR, PNG_1024_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------
# 1. Kyte Suite Master Logo
# -------------------------------------------------------------

FEATHER_PATH = (
    "M278.5 215.6L23 471c-9.4 9.4-9.4 24.6 0 33.9s24.6 9.4 33.9 0l74.8-74.8"
    "c7.4 4.6 15.3 8.2 23.8 10.5C200.3 452.8 270 454.5 338 409.4c12.2-8.1 5.8-25.4-8.8-25.4"
    "l-16.1 0c-5.1 0-9.2-4.1-9.2-9.2c0-4.1 2.7-7.6 6.5-8.8l97.7-29.3c3.4-1 6.4-3.1 8.4-6.1"
    "c4.4-6.4 8.6-12.9 12.6-19.6c6.2-10.3-1.5-23-13.5-23l-38.6 0c-5.1 0-9.2-4.1-9.2-9.2"
    "c0-4.1 2.7-7.6 6.5-8.8l80.9-24.3c4.6-1.4 8.4-4.8 10.2-9.3C494.5 163 507.8 86.1 511.9 36.8"
    "c.8-9.9-3-19.6-10-26.6s-16.7-10.8-26.6-10C391.5 7 228.5 40.5 137.4 131.6"
    "C57.3 211.7 56.7 302.3 71.3 356.4c2.1 7.9 12 9.6 17.8 3.8L253.6 195.8"
    "c6.2-6.2 16.4-6.2 22.6 0c5.4 5.4 6.1 13.6 2.2 19.8z"
)

KYTESUITE_ICON_SVG = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <linearGradient id="suiteGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f46e5" />
      <stop offset="50%" stop-color="#0ea5e9" />
      <stop offset="100%" stop-color="#2563eb" />
    </linearGradient>
    <linearGradient id="glassGloss" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.35" />
      <stop offset="35%" stop-color="#ffffff" stop-opacity="0.08" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
    </linearGradient>
    <filter id="featherShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="16" stdDeviation="24" flood-color="#0f172a" flood-opacity="0.38" />
    </filter>
    <filter id="squircleShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="24" stdDeviation="32" flood-color="#312e81" flood-opacity="0.32" />
    </filter>
  </defs>

  <!-- Squircle Base -->
  <rect x="96" y="96" width="832" height="832" rx="210" ry="210" fill="url(#suiteGrad)" filter="url(#squircleShadow)" />
  
  <!-- Glass Top Reflection -->
  <rect x="96" y="96" width="832" height="416" rx="210" ry="210" fill="url(#glassGloss)" />
  
  <!-- Subtle Border Highlight -->
  <rect x="96" y="96" width="832" height="832" rx="210" ry="210" fill="none" stroke="#ffffff" stroke-opacity="0.28" stroke-width="4" />

  <!-- Central Feather (FontAwesome 6 feather-pointed) -->
  <g transform="translate(256, 256) scale(1.0)" filter="url(#featherShadow)">
    <path d="{FEATHER_PATH}" fill="#ffffff" />
  </g>
</svg>
'''

KYTESUITE_SYMBOL_SVG = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <linearGradient id="featherSymbolGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f46e5" />
      <stop offset="48%" stop-color="#0ea5e9" />
      <stop offset="100%" stop-color="#2563eb" />
    </linearGradient>
    <filter id="symbolShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="20" stdDeviation="28" flood-color="#0284c7" flood-opacity="0.3" />
    </filter>
  </defs>

  <g transform="translate(102, 102) scale(1.6)" filter="url(#symbolShadow)">
    <path d="{FEATHER_PATH}" fill="url(#featherSymbolGrad)" />
  </g>
</svg>
'''

# -------------------------------------------------------------
# 2. KyteView (極速預覽)
# -------------------------------------------------------------

# Diamond Prism Aperture geometric construct
KYTEVIEW_SYMBOL_CONTENT = '''
  <defs>
    <linearGradient id="viewCyanIndigo" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#818cf8" />
      <stop offset="100%" stop-color="#c084fc" />
    </linearGradient>
    <linearGradient id="viewFacetTop" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.85" />
      <stop offset="100%" stop-color="#6366f1" stop-opacity="0.4" />
    </linearGradient>
    <linearGradient id="viewFacetRight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#818cf8" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#c084fc" stop-opacity="0.85" />
    </linearGradient>
    <linearGradient id="viewFacetBottom" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#6366f1" stop-opacity="0.5" />
      <stop offset="100%" stop-color="#a855f7" stop-opacity="0.9" />
    </linearGradient>
    <linearGradient id="viewFacetLeft" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.5" />
    </linearGradient>
    <filter id="neonGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="12" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <g id="diamondAperture" filter="url(#neonGlow)" transform="rotate(-18 512 512)">
    <!-- Outer Rhombus / Diamond Prism Shell -->
    <!-- Top-Left Facet -->
    <polygon points="512,140 370,330 512,300" fill="url(#viewFacetTop)" stroke="#38bdf8" stroke-width="10" stroke-linejoin="round" />
    <polygon points="512,140 370,330 210,512" fill="url(#viewFacetLeft)" stroke="#38bdf8" stroke-width="10" stroke-linejoin="round" />
    
    <!-- Top-Right Facet -->
    <polygon points="512,140 654,330 512,300" fill="url(#viewFacetTop)" stroke="#818cf8" stroke-width="10" stroke-linejoin="round" />
    <polygon points="512,140 654,330 814,512" fill="url(#viewFacetRight)" stroke="#c084fc" stroke-width="10" stroke-linejoin="round" />

    <!-- Bottom-Left Facet -->
    <polygon points="210,512 370,694 512,724" fill="url(#viewFacetLeft)" stroke="#38bdf8" stroke-width="10" stroke-linejoin="round" />
    <polygon points="210,512 370,694 512,884" fill="url(#viewFacetBottom)" stroke="#818cf8" stroke-width="10" stroke-linejoin="round" />

    <!-- Bottom-Right Facet -->
    <polygon points="814,512 654,694 512,724" fill="url(#viewFacetRight)" stroke="#c084fc" stroke-width="10" stroke-linejoin="round" />
    <polygon points="814,512 654,694 512,884" fill="url(#viewFacetBottom)" stroke="#a855f7" stroke-width="10" stroke-linejoin="round" />

    <!-- Outer Hex-Prism Ribs -->
    <polygon points="370,330 654,330 814,512 654,694 370,694 210,512" fill="none" stroke="#60a5fa" stroke-width="8" opacity="0.6" />

    <!-- Outer Aperture Ring -->
    <circle cx="512" cy="512" r="195" fill="none" stroke="url(#viewCyanIndigo)" stroke-width="14" />
    <circle cx="512" cy="512" r="165" fill="#0f172a" fill-opacity="0.88" stroke="url(#viewCyanIndigo)" stroke-width="8" />

    <!-- 6 Camera Shutter Blades (Aperture Iris) -->
    <!-- Blade 1 -->
    <path d="M512 347 A 165 165 0 0 1 655 430 L 555 490 A 65 65 0 0 0 490 447 Z" fill="#38bdf8" fill-opacity="0.92" stroke="#e0f2fe" stroke-width="4" />
    <!-- Blade 2 -->
    <path d="M655 430 A 165 165 0 0 1 655 594 L 540 550 A 65 65 0 0 0 555 490 Z" fill="#60a5fa" fill-opacity="0.92" stroke="#e0f2fe" stroke-width="4" />
    <!-- Blade 3 -->
    <path d="M655 594 A 165 165 0 0 1 512 677 L 470 565 A 65 65 0 0 0 540 550 Z" fill="#818cf8" fill-opacity="0.92" stroke="#e0f2fe" stroke-width="4" />
    <!-- Blade 4 -->
    <path d="M512 677 A 165 165 0 0 1 369 594 L 470 535 A 65 65 0 0 0 470 565 Z" fill="#a855f7" fill-opacity="0.92" stroke="#f3e8ff" stroke-width="4" />
    <!-- Blade 5 -->
    <path d="M369 594 A 165 165 0 0 1 369 430 L 485 475 A 65 65 0 0 0 470 535 Z" fill="#c084fc" fill-opacity="0.92" stroke="#f3e8ff" stroke-width="4" />
    <!-- Blade 6 -->
    <path d="M369 430 A 165 165 0 0 1 512 347 L 555 460 A 65 65 0 0 0 485 475 Z" fill="#38bdf8" fill-opacity="0.92" stroke="#e0f2fe" stroke-width="4" />

    <!-- Dark Pupil Aperture Center -->
    <circle cx="512" cy="512" r="54" fill="#030712" stroke="#38bdf8" stroke-width="6" />
  </g>
'''

KYTEVIEW_ICON_SVG = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <linearGradient id="darkGlass" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e1b4b" />
      <stop offset="45%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
    <linearGradient id="specularGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.25" />
      <stop offset="30%" stop-color="#818cf8" stop-opacity="0.1" />
      <stop offset="100%" stop-color="#000000" stop-opacity="0" />
    </linearGradient>
    <filter id="iconShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="24" stdDeviation="32" flood-color="#020617" flood-opacity="0.75" />
    </filter>
  </defs>

  <!-- Dark Mica Squircle -->
  <rect x="96" y="96" width="832" height="832" rx="210" ry="210" fill="url(#darkGlass)" filter="url(#iconShadow)" />
  <rect x="96" y="96" width="832" height="832" rx="210" ry="210" fill="url(#specularGlow)" />
  <rect x="96" y="96" width="832" height="832" rx="210" ry="210" fill="none" stroke="#ffffff" stroke-opacity="0.18" stroke-width="4" />

  <!-- Core Diamond Aperture Symbol -->
  {KYTEVIEW_SYMBOL_CONTENT}
</svg>
'''

KYTEVIEW_SYMBOL_SVG = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  {KYTEVIEW_SYMBOL_CONTENT}
</svg>
'''

# -------------------------------------------------------------
# 3. KyteShelf (懸浮置物架)
# -------------------------------------------------------------

KYTESHELF_SYMBOL_CONTENT = '''
  <defs>
    <linearGradient id="shelfGlassGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#bae6fd" stop-opacity="0.9" />
      <stop offset="50%" stop-color="#7dd3fc" stop-opacity="0.65" />
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.85" />
    </linearGradient>
    <linearGradient id="shelfBaseGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="100%" stop-color="#e2e8f0" />
    </linearGradient>
    <linearGradient id="docGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="100%" stop-color="#f8fafc" />
    </linearGradient>
    <filter id="shelfShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="18" stdDeviation="22" flood-color="#0284c7" flood-opacity="0.25" />
    </filter>
  </defs>

  <g id="shelfCore" filter="url(#shelfShadow)">
    <!-- Base White Rounded Plinth / Pedestal -->
    <path d="M260 670 L512 790 L764 670 L764 740 L512 860 L260 740 Z" fill="#cbd5e1" opacity="0.6" />
    <path d="M260 670 Q240 660 260 650 L490 540 Q512 530 534 540 L764 650 Q784 660 764 670 L534 780 Q512 790 490 780 Z" fill="url(#shelfBaseGrad)" stroke="#ffffff" stroke-width="4" />

    <!-- Lower Glass Tray -->
    <path d="M270 520 Q250 510 270 500 L490 395 Q512 385 534 395 L754 500 Q774 510 754 520 L534 625 Q512 635 490 625 Z" fill="url(#shelfGlassGrad)" stroke="#e0f2fe" stroke-width="8" />
    <path d="M270 520 L270 550 Q250 560 270 570 L490 675 Q512 685 534 675 L754 570 Q774 560 754 550 L754 520 L534 625 Q512 635 490 625 Z" fill="#0284c7" fill-opacity="0.4" stroke="#38bdf8" stroke-width="4" />

    <!-- Upper Glass Shelf / Partition Frame -->
    <path d="M270 360 Q250 350 270 340 L490 235 Q512 225 534 235 L754 340 Q774 350 754 360 L534 465 Q512 475 490 465 Z" fill="url(#shelfGlassGrad)" stroke="#ffffff" stroke-width="8" />
    <path d="M270 360 L270 390 L512 505 L754 390 L754 360 L512 475 Z" fill="#0369a1" fill-opacity="0.35" stroke="#bae6fd" stroke-width="4" />

    <!-- Vertical Glass Pillars / Sidewalls -->
    <path d="M270 350 Q250 360 270 510" fill="none" stroke="#bae6fd" stroke-width="12" stroke-linecap="round" />
    <path d="M754 350 Q774 360 754 510" fill="none" stroke="#bae6fd" stroke-width="12" stroke-linecap="round" />

    <!-- Staging File / Document with Folded Corner -->
    <g id="stagingDoc" transform="translate(427, 210)">
      <!-- Document Body -->
      <path d="M 0 35 Q 0 0 35 0 L 110 0 L 170 60 L 170 205 Q 170 240 135 240 L 35 240 Q 0 240 0 205 Z" fill="url(#docGrad)" stroke="#bae6fd" stroke-width="5" />
      <!-- Folded Corner -->
      <path d="M 110 0 L 110 50 Q 110 60 120 60 L 170 60 Z" fill="#e2e8f0" stroke="#bae6fd" stroke-width="4" />
      <!-- Downward Arrow (Drop / Stash Action) -->
      <path d="M 85 95 L 85 160 M 60 140 L 85 165 L 110 140" fill="none" stroke="#0284c7" stroke-width="14" stroke-linecap="round" stroke-linejoin="round" />
    </g>
  </g>
'''

KYTESHELF_ICON_SVG = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <linearGradient id="shelfTileGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e0f2fe" />
      <stop offset="40%" stop-color="#bae6fd" />
      <stop offset="100%" stop-color="#7dd3fc" />
    </linearGradient>
    <linearGradient id="shelfGloss" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.8" />
      <stop offset="30%" stop-color="#ffffff" stop-opacity="0.1" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
    </linearGradient>
    <filter id="shelfTileShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="24" stdDeviation="32" flood-color="#0369a1" flood-opacity="0.25" />
    </filter>
  </defs>

  <!-- Ice Glass Squircle -->
  <rect x="96" y="96" width="832" height="832" rx="210" ry="210" fill="url(#shelfTileGrad)" filter="url(#shelfTileShadow)" />
  <rect x="96" y="96" width="832" height="416" rx="210" ry="210" fill="url(#shelfGloss)" />
  <rect x="96" y="96" width="832" height="832" rx="210" ry="210" fill="none" stroke="#ffffff" stroke-width="6" />

  <!-- Core Shelf & Staging Document -->
  {KYTESHELF_SYMBOL_CONTENT}
</svg>
'''

KYTESHELF_SYMBOL_SVG = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  {KYTESHELF_SYMBOL_CONTENT}
</svg>
'''

# -------------------------------------------------------------
# 4. KyteRename (批次更名)
# -------------------------------------------------------------

# Modern Precision Bold R with 3D drop shadow
KYTERENAME_R_PATH = "M340 230 L550 230 C660 230 730 290 730 400 C730 495 670 550 580 570 L740 790 L600 790 L460 590 L440 590 L440 790 L340 790 Z M440 330 L440 500 L530 500 C600 500 635 470 635 415 C635 360 600 330 530 330 Z"

KYTERENAME_ICON_SVG = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <linearGradient id="renameBlueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6" />
      <stop offset="60%" stop-color="#1d4ed8" />
      <stop offset="100%" stop-color="#1e40af" />
    </linearGradient>
    <linearGradient id="renameGloss" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.3" />
      <stop offset="40%" stop-color="#ffffff" stop-opacity="0.05" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
    </linearGradient>
    <filter id="rShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="12" dy="20" stdDeviation="16" flood-color="#0f172a" flood-opacity="0.35" />
    </filter>
    <filter id="tileShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="24" stdDeviation="32" flood-color="#1e3a8a" flood-opacity="0.35" />
    </filter>
  </defs>

  <!-- Blue Squircle Base -->
  <rect x="96" y="96" width="832" height="832" rx="210" ry="210" fill="url(#renameBlueGrad)" filter="url(#tileShadow)" />
  <rect x="96" y="96" width="832" height="416" rx="210" ry="210" fill="url(#renameGloss)" />
  
  <!-- Outer subtle hairline -->
  <rect x="96" y="96" width="832" height="832" rx="210" ry="210" fill="none" stroke="#60a5fa" stroke-width="4" stroke-opacity="0.5" />
  
  <!-- Inset Double Line (macOS / Fluent aesthetic) -->
  <rect x="136" y="136" width="752" height="752" rx="175" ry="175" fill="none" stroke="#ffffff" stroke-width="6" stroke-opacity="0.75" />

  <!-- Bold Central R with Drop Shadow -->
  <g filter="url(#rShadow)">
    <path d="{KYTERENAME_R_PATH}" fill="#ffffff" />
  </g>
</svg>
'''

KYTERENAME_SYMBOL_SVG = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <linearGradient id="rSymbolGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6" />
      <stop offset="100%" stop-color="#1d4ed8" />
    </linearGradient>
    <filter id="rSymbolShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="18" stdDeviation="24" flood-color="#1d4ed8" flood-opacity="0.35" />
    </filter>
  </defs>

  <g transform="translate(512, 512) scale(1.15) translate(-535, -510)" filter="url(#rSymbolShadow)">
    <path d="{KYTERENAME_R_PATH}" fill="url(#rSymbolGrad)" />
  </g>
</svg>
'''

# Dictionary of all SVGs
SVGS = {
    "kytesuite_icon.svg": KYTESUITE_ICON_SVG,
    "kytesuite_symbol.svg": KYTESUITE_SYMBOL_SVG,
    "kyteview_icon.svg": KYTEVIEW_ICON_SVG,
    "kyteview_symbol.svg": KYTEVIEW_SYMBOL_SVG,
    "kyteshelf_icon.svg": KYTESHELF_ICON_SVG,
    "kyteshelf_symbol.svg": KYTESHELF_SYMBOL_SVG,
    "kyterename_icon.svg": KYTERENAME_ICON_SVG,
    "kyterename_symbol.svg": KYTERENAME_SYMBOL_SVG,
}

print(f"Generated {len(SVGS)} SVG files definitions.")

# Save all SVGs
for filename, content in SVGS.items():
    filepath = SVG_DIR / filename
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Saved: {filepath}")
