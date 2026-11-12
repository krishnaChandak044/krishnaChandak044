"""Create a compact, animated dot portrait from the public GitHub avatar."""

import base64
import io
from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "avatar-source.png"
OUTPUT = ROOT / "assets" / "portrait-banner.svg"
SIZE = 158


def portrait():
    image = Image.open(SOURCE).convert("RGB")
    image = ImageOps.fit(image, (460, 460), method=Image.Resampling.LANCZOS)
    image = ImageEnhance.Contrast(ImageOps.autocontrast(image, cutoff=1)).enhance(1.3)
    image = image.filter(ImageFilter.UnsharpMask(radius=2, percent=120))
    image = image.convert("L").resize((SIZE, SIZE), Image.Resampling.LANCZOS)
    mask = Image.new("L", (460, 460), 0)
    draw = ImageDraw.Draw(mask)
    # The source avatar has a blurred background. Trace a generous head-and-shoulders
    # silhouette to keep the dither on the subject without claiming pixel-perfect matting.
    draw.polygon([
        (15, 459), (28, 397), (54, 345), (92, 305), (135, 284),
        (146, 262), (135, 225), (127, 184), (134, 132), (145, 90),
        (171, 61), (209, 48), (255, 49), (288, 65), (294, 99),
        (306, 148), (305, 210), (289, 251), (301, 282), (350, 306),
        (396, 337), (428, 384), (449, 459),
    ], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(4)).resize((SIZE, SIZE), Image.Resampling.LANCZOS)
    return image, mask


def build():
    image, mask = portrait()
    photo = Image.open(SOURCE).convert("RGB")
    photo = ImageOps.fit(photo, (374, 348), method=Image.Resampling.LANCZOS)
    photo = ImageOps.colorize(ImageOps.autocontrast(photo.convert("L")), "#101e32", "#b3a6da")
    photo_bytes = io.BytesIO()
    photo.save(photo_bytes, format="JPEG", quality=84, optimize=True)
    photo_uri = base64.b64encode(photo_bytes.getvalue()).decode("ascii")
    groups = [[] for _ in range(24)]
    for y in range(SIZE):
        for x in range(SIZE):
            if mask.getpixel((x, y)) < 155:
                continue
            value = image.getpixel((x, y))
            # More ink for illuminated pixels; deterministic scattered thresholding.
            darkness = value / 255
            noise = ((x * 73 + y * 151 + x * y * 19) % 101) / 101
            if darkness < 0.16 or noise > min(0.96, darkness * 1.28):
                continue
            px, py = 60 + x * 2.16, 74 + y * 2.16
            radius = 0.68 if darkness < 0.42 else 0.91 if darkness < 0.68 else 1.08
            groups[(x * 31 + y * 47) % len(groups)].append(
                f'M{px:.1f} {py:.1f}h{radius * 2:.1f}v{radius * 2:.1f}h-{radius * 2:.1f}z'
            )
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="470" viewBox="0 0 1180 470" role="img" aria-labelledby="title desc">',
        '<title id="title">Krishna Chandak, backend developer</title>',
        '<desc id="desc">Animated dotted portrait of Krishna beside a concise backend engineering profile.</desc>',
        '<defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#0a101f"/><stop offset="1" stop-color="#142c3b"/></linearGradient><linearGradient id="ink" x2="1"><stop stop-color="#bca5ff"/><stop offset="1" stop-color="#78dcd7"/></linearGradient><clipPath id="photo-clip"><rect x="50" y="80" width="372" height="346" rx="15"/></clipPath></defs>',
        '<style>@media (prefers-reduced-motion: reduce) {.portrait-dot,.pulse{animation:none!important}}.portrait-dot{animation:shimmer 6s ease-in-out infinite;opacity:.22}.pulse{animation:pulse 3s ease-in-out infinite}@keyframes shimmer{0%,100%{opacity:.22}50%{opacity:.08}}@keyframes pulse{0%,100%{opacity:1}50%{opacity:.45}}</style>',
        '<rect width="1180" height="470" rx="22" fill="url(#bg)"/>',
        '<rect x="24" y="24" width="1132" height="422" rx="16" fill="none" stroke="#385368"/>',
        '<text x="53" y="58" fill="#93a9b9" font-family="Arial,Helvetica,sans-serif" font-size="13" letter-spacing="2">PROFILE / KRISHNA-CHANDAK</text>',
        '<circle cx="1105" cy="52" r="5" fill="#72e1c5" class="pulse"/>',
        '<text x="1089" y="57" text-anchor="end" fill="#9fbbca" font-family="Arial,Helvetica,sans-serif" font-size="12">BUILDING</text>',
        '<rect x="49" y="79" width="374" height="348" rx="16" fill="#101d2c" stroke="#315267"/>',
        f'<image x="50" y="80" width="372" height="346" href="data:image/jpeg;base64,{photo_uri}" clip-path="url(#photo-clip)" opacity=".86"/>',
        '<rect x="50" y="80" width="372" height="346" rx="15" fill="#0d1724" opacity=".13"/>',
        '<text x="68" y="104" fill="#7de0cf" font-family="Arial,Helvetica,sans-serif" font-size="11" letter-spacing="2">VISUAL.MAP</text>',
    ]
    for index, group in enumerate(groups):
        if group:
            parts.append(f'<path class="portrait-dot" d="{"".join(group)}" fill="url(#ink)" style="animation-delay:{index * 0.07:.2f}s"/>')
    parts.extend([
        '<text x="453" y="131" fill="#7de0cf" font-family="Arial,Helvetica,sans-serif" font-size="14" letter-spacing="3">HELLO, I AM</text>',
        '<text x="451" y="192" fill="#eff7fb" font-family="Arial,Helvetica,sans-serif" font-size="55" font-weight="700" letter-spacing="-1">Krishna Chandak</text>',
        '<text x="453" y="232" fill="#bca5ff" font-family="Arial,Helvetica,sans-serif" font-size="23" font-weight="600">Backend Developer</text>',
        '<path d="M453 258H1110" stroke="#315267"/>',
        '<text x="453" y="295" fill="#a9bdcb" font-family="Arial,Helvetica,sans-serif" font-size="19">Python · FastAPI · Django · Systems that scale</text>',
        '<text x="453" y="334" fill="#a9bdcb" font-family="Arial,Helvetica,sans-serif" font-size="18">Pune, India  /  Pimpri Chinchwad University</text>',
        '<text x="453" y="389" fill="#74dfc5" font-family="Arial,Helvetica,sans-serif" font-size="16">THOUGHTFUL SYSTEMS  •  DEPENDABLE APIs</text>',
        '</svg>',
    ])
    OUTPUT.write_text("\n".join(parts) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build()
