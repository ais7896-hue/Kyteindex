# -*- coding: utf-8 -*-
"""
Render SVG to 512x512 and 1024x1024 Transparent PNGs using PySide6
And process original icons to transparent squircle PNGs.
"""

import sys
from pathlib import Path
from PIL import Image

from PySide6.QtGui import QImage, QPainter, QColor
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtCore import QSize, Qt, QRectF

BASE_DIR = Path(r"d:\Noah\Antigravity專案程式專用\Kyteindex\assets\logos")
SVG_DIR = BASE_DIR / "svg"
PNG_512_DIR = BASE_DIR / "png-512"
PNG_1024_DIR = BASE_DIR / "png-1024"

def render_svg_to_png(svg_path: Path, output_path: Path, size: int):
    renderer = QSvgRenderer(str(svg_path))
    if not renderer.isValid():
        print(f"Error: Invalid SVG: {svg_path}")
        return False

    image = QImage(size, size, QImage.Format.Format_ARGB32)
    image.fill(Qt.GlobalColor.transparent)

    painter = QPainter(image)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
    painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform, True)
    
    renderer.render(painter, QRectF(0, 0, size, size))
    painter.end()

    image.save(str(output_path), "PNG")
    print(f"Rendered: {output_path} ({size}x{size})")
    return True

# 1. Render all SVGs
svg_files = list(SVG_DIR.glob("*.svg"))
for svg_file in svg_files:
    base_name = svg_file.stem
    # 512
    p512 = PNG_512_DIR / f"{base_name}_512.png"
    render_svg_to_png(svg_file, p512, 512)
    # 1024
    p1024 = PNG_1024_DIR / f"{base_name}_1024.png"
    render_svg_to_png(svg_file, p1024, 1024)

# 2. Also extract and refine the original high-detail app icons as additional high-res versions:
ASSETS_DIR = Path(r"d:\Noah\Antigravity專案程式專用\Kyteindex\assets")
from PIL import ImageDraw

# A. KyteShelf original artwork: Extract squircle with precision rounded mask
shelf_orig_path = ASSETS_DIR / "kyteshelf.png"
if shelf_orig_path.exists():
    im = Image.open(shelf_orig_path).convert("RGBA")
    # Exact squircle bounds in kyteshelf.png: (45, 41, 211, 219)
    crop_box = (45, 41, 211, 219)
    cropped = im.crop(crop_box)
    cw, ch = cropped.size
    
    # Pad to square
    sq_size = max(cw, ch)
    square_img = Image.new("RGBA", (sq_size, sq_size), (0, 0, 0, 0))
    offset_x = (sq_size - cw) // 2
    offset_y = (sq_size - ch) // 2
    square_img.paste(cropped, (offset_x, offset_y))
    
    # Antialiased rounded squircle mask (draw at 4x and downsample)
    super_size = sq_size * 4
    super_mask = Image.new("L", (super_size, super_size), 0)
    draw = ImageDraw.Draw(super_mask)
    draw.rounded_rectangle([offset_x * 4, offset_y * 4, (offset_x + cw) * 4, (offset_y + ch) * 4], radius=int(cw * 4 * 0.22), fill=255)
    mask = super_mask.resize((sq_size, sq_size), Image.Resampling.LANCZOS)
    square_img.putalpha(mask)
    
    im_512 = square_img.resize((512, 512), Image.Resampling.LANCZOS)
    im_1024 = square_img.resize((1024, 1024), Image.Resampling.LANCZOS)
    im_512.save(PNG_512_DIR / "kyteshelf_glass3d_icon_512.png")
    im_1024.save(PNG_1024_DIR / "kyteshelf_glass3d_icon_1024.png")
    print("Processed kyteshelf original 3D icon with perfect rounded transparent mask.")

# B. KyteView original artwork: Extract dark glass squircle with precision rounded mask
view_orig_path = ASSETS_DIR / "kyteview.png"
if view_orig_path.exists():
    im = Image.open(view_orig_path).convert("RGBA")
    # Squircle bounds in kyteview.png: (34, 34, 222, 222)
    crop_box = (34, 34, 222, 222)
    cropped = im.crop(crop_box)
    cw, ch = cropped.size
    
    # Antialiased rounded mask
    super_size = cw * 4
    super_mask = Image.new("L", (super_size, super_size), 0)
    draw = ImageDraw.Draw(super_mask)
    draw.rounded_rectangle([0, 0, super_size, super_size], radius=int(super_size * 0.23), fill=255)
    mask = super_mask.resize((cw, ch), Image.Resampling.LANCZOS)
    cropped.putalpha(mask)
    
    v_512 = cropped.resize((512, 512), Image.Resampling.LANCZOS)
    v_1024 = cropped.resize((1024, 1024), Image.Resampling.LANCZOS)
    v_512.save(PNG_512_DIR / "kyteview_prism3d_icon_512.png")
    v_1024.save(PNG_1024_DIR / "kyteview_prism3d_icon_1024.png")
    print("Processed kyteview original 3D icon with perfect rounded transparent mask.")

# C. KyteRename original artwork: Already transparent, upscale to 512 and 1024
rename_orig_path = ASSETS_DIR / "kyterename.png"
if rename_orig_path.exists():
    im = Image.open(rename_orig_path).convert("RGBA")
    r_512 = im.resize((512, 512), Image.Resampling.LANCZOS)
    r_1024 = im.resize((1024, 1024), Image.Resampling.LANCZOS)
    r_512.save(PNG_512_DIR / "kyterename_classic_icon_512.png")
    r_1024.save(PNG_1024_DIR / "kyterename_classic_icon_1024.png")
    print("Processed kyterename original icon to 512 and 1024.")

print("All PNG generations completed successfully!")
