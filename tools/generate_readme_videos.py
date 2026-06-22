from __future__ import annotations

import csv
import json
import math
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(os.environ.get("ATLAS_ROOT", Path(__file__).resolve().parents[1])).resolve()
W, H = 800, 450
FPS = 8
FRAMES = 64


def safe_path(relative: str) -> Path:
    path = (ROOT / relative).resolve()
    if not str(path).lower().startswith(str(ROOT).lower()):
        raise RuntimeError(f"Refusing to write outside Atlas repo: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def write_text(relative: str, body: str) -> None:
    safe_path(relative).write_text(body.rstrip() + "\n", encoding="utf-8")


def read_csv(relative: str) -> list[dict[str, str]]:
    with safe_path(relative).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


PALETTE = [
    (2, 6, 23),      # 0 bg
    (6, 17, 31),     # 1 bg2
    (15, 23, 42),    # 2 panel
    (17, 28, 49),    # 3 panel2
    (30, 41, 59),    # 4 border
    (71, 85, 105),   # 5 muted
    (148, 163, 184), # 6 slate
    (203, 213, 225), # 7 text2
    (248, 250, 252), # 8 white
    (45, 212, 191),  # 9 teal
    (34, 211, 238),  # 10 cyan
    (96, 165, 250),  # 11 blue
    (167, 139, 250), # 12 violet
    (244, 114, 182), # 13 pink
    (245, 158, 11),  # 14 amber
    (52, 211, 153),  # 15 green
    (251, 113, 133), # 16 rose
    (125, 211, 252), # 17 sky
    (20, 184, 166),  # 18 teal2
    (37, 99, 235),   # 19 blue2
    (124, 58, 237),  # 20 violet2
    (217, 119, 6),   # 21 amber2
    (12, 74, 110),   # 22 deep blue
    (6, 78, 59),     # 23 deep green
    (76, 29, 149),   # 24 deep violet
    (127, 29, 29),   # 25 deep red
    (255, 255, 255), # 26 pure white
    (0, 0, 0),        # 27 black
]
while len(PALETTE) < 64:
    PALETTE.append((0, 0, 0))

C = {
    "bg": 0,
    "bg2": 1,
    "panel": 2,
    "panel2": 3,
    "border": 4,
    "muted": 6,
    "text": 8,
    "soft": 7,
    "teal": 9,
    "cyan": 10,
    "blue": 11,
    "violet": 12,
    "pink": 13,
    "amber": 14,
    "green": 15,
    "rose": 16,
    "sky": 17,
    "teal2": 18,
    "blue2": 19,
    "violet2": 20,
    "amber2": 21,
    "deepblue": 22,
    "deepgreen": 23,
    "deepviolet": 24,
}


FONT = {
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "B": ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    "C": ["01111", "10000", "10000", "10000", "10000", "10000", "01111"],
    "D": ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    "F": ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
    "G": ["01111", "10000", "10000", "10111", "10001", "10001", "01111"],
    "H": ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    "I": ["11111", "00100", "00100", "00100", "00100", "00100", "11111"],
    "J": ["00111", "00010", "00010", "00010", "10010", "10010", "01100"],
    "K": ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    "L": ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    "M": ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    "N": ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
    "O": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    "P": ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    "Q": ["01110", "10001", "10001", "10001", "10101", "10010", "01101"],
    "R": ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    "S": ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    "U": ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    "V": ["10001", "10001", "10001", "10001", "10001", "01010", "00100"],
    "W": ["10001", "10001", "10001", "10101", "10101", "10101", "01010"],
    "X": ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
    "Y": ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
    "Z": ["11111", "00001", "00010", "00100", "01000", "10000", "11111"],
    "0": ["01110", "10001", "10011", "10101", "11001", "10001", "01110"],
    "1": ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
    "2": ["01110", "10001", "00001", "00010", "00100", "01000", "11111"],
    "3": ["11110", "00001", "00001", "01110", "00001", "00001", "11110"],
    "4": ["00010", "00110", "01010", "10010", "11111", "00010", "00010"],
    "5": ["11111", "10000", "10000", "11110", "00001", "00001", "11110"],
    "6": ["01110", "10000", "10000", "11110", "10001", "10001", "01110"],
    "7": ["11111", "00001", "00010", "00100", "01000", "01000", "01000"],
    "8": ["01110", "10001", "10001", "01110", "10001", "10001", "01110"],
    "9": ["01110", "10001", "10001", "01111", "00001", "00001", "01110"],
    " ": ["00000", "00000", "00000", "00000", "00000", "00000", "00000"],
    "-": ["00000", "00000", "00000", "11111", "00000", "00000", "00000"],
    ":": ["00000", "00100", "00100", "00000", "00100", "00100", "00000"],
    ".": ["00000", "00000", "00000", "00000", "00000", "01100", "01100"],
    "/": ["00001", "00010", "00010", "00100", "01000", "01000", "10000"],
    "+": ["00000", "00100", "00100", "11111", "00100", "00100", "00000"],
    "$": ["00100", "01111", "10100", "01110", "00101", "11110", "00100"],
    ">": ["10000", "01000", "00100", "00010", "00100", "01000", "10000"],
    "&": ["01100", "10010", "10100", "01000", "10101", "10010", "01101"],
    "#": ["01010", "11111", "01010", "01010", "11111", "01010", "01010"],
}


class Canvas:
    def __init__(self, w: int = W, h: int = H):
        self.w = w
        self.h = h
        self.p = bytearray([C["bg"]] * (w * h))

    def px(self, x: int, y: int, color: int) -> None:
        if 0 <= x < self.w and 0 <= y < self.h:
            self.p[y * self.w + x] = color

    def rect(self, x: int, y: int, w: int, h: int, color: int, border: int | None = None) -> None:
        x0, y0 = max(0, x), max(0, y)
        x1, y1 = min(self.w, x + w), min(self.h, y + h)
        for yy in range(y0, y1):
            off = yy * self.w
            self.p[off + x0 : off + x1] = bytes([color]) * max(0, x1 - x0)
        if border is not None:
            self.line(x, y, x + w - 1, y, border)
            self.line(x, y + h - 1, x + w - 1, y + h - 1, border)
            self.line(x, y, x, y + h - 1, border)
            self.line(x + w - 1, y, x + w - 1, y + h - 1, border)

    def panel(self, x: int, y: int, w: int, h: int, accent: int | None = None) -> None:
        self.rect(x + 4, y + 5, w, h, C["bg"], None)
        self.rect(x, y, w, h, C["panel"], C["border"])
        if accent is not None:
            self.rect(x, y, 5, h, accent, None)

    def line(self, x0: int, y0: int, x1: int, y1: int, color: int) -> None:
        dx = abs(x1 - x0)
        dy = -abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx + dy
        while True:
            self.px(x0, y0, color)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy

    def circle(self, cx: int, cy: int, r: int, color: int, border: int | None = None) -> None:
        r2 = r * r
        inner = max(0, r - 2) ** 2
        for y in range(cy - r, cy + r + 1):
            for x in range(cx - r, cx + r + 1):
                d = (x - cx) ** 2 + (y - cy) ** 2
                if d <= r2:
                    self.px(x, y, border if border is not None and d >= inner else color)

    def text(self, x: int, y: int, text: str, color: int = C["text"], scale: int = 2, max_width: int | None = None) -> None:
        cx = x
        cy = y
        char_w = 6 * scale
        for ch in text.upper():
            if ch == "\n":
                cx = x
                cy += 9 * scale
                continue
            if max_width and cx + char_w > x + max_width:
                cx = x
                cy += 9 * scale
            glyph = FONT.get(ch, FONT[" "])
            for gy, row in enumerate(glyph):
                for gx, bit in enumerate(row):
                    if bit == "1":
                        self.rect(cx + gx * scale, cy + gy * scale, scale, scale, color)
            cx += char_w


def bg(t: float, title: str, subtitle: str) -> Canvas:
    c = Canvas()
    for y in range(H):
        band = C["bg"] if y < H * 0.55 else C["bg2"]
        c.rect(0, y, W, 1, band)
    for x in range(0, W, 40):
        c.line(x, 0, x, H, C["panel2"])
    for y in range(0, H, 40):
        c.line(0, y, W, y, C["panel2"])
    pulse = int((math.sin(t * math.tau) + 1) * 0.5)
    c.rect(20, 20, W - 40, H - 40, C["bg"], C["border"])
    c.text(36, 34, title, C["text"], 3)
    c.text(38, 68, subtitle, C["muted"], 1)
    c.rect(36, 92, 210 + pulse * 16, 3, C["teal"])
    return c


def node(c: Canvas, x: int, y: int, label: str, color: int, active: bool = False) -> None:
    r = 30 if active else 24
    c.circle(x, y, r + 5, C["panel"], color if active else C["border"])
    c.circle(x, y, r, C["panel2"], color)
    c.text(x - min(54, len(label) * 5), y + r + 12, label, C["text"] if active else C["soft"], 1, 118)
    if active:
        c.circle(x, y, 6, color)


def moving_dot(c: Canvas, x1: int, y1: int, x2: int, y2: int, p: float, color: int) -> None:
    x = int(x1 + (x2 - x1) * p)
    y = int(y1 + (y2 - y1) * p)
    c.circle(x, y, 5, color)


def video_platform_command() -> list[bytearray]:
    labels = [
        ("AGENTS", 185, 160, C["cyan"]),
        ("BUSINESS SPACES", 610, 160, C["teal"]),
        ("AI ROUTE", 650, 315, C["violet"]),
        ("VAULT", 400, 360, C["amber"]),
        ("MARKETPLACE", 150, 315, C["pink"]),
        ("ADMIN", 400, 190, C["blue"]),
    ]
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES
        active = int(t * len(labels)) % len(labels)
        c = bg(t, "ARSENAL PLATFORM VIDEO README", "91 ROUTES / 57 EDGE FUNCTIONS / 28 FEATURE CLUSTERS")
        c.panel(280, 190, 240, 100, C["teal"])
        c.text(330, 218, "ARSENAL OS", C["text"], 3)
        c.text(315, 260, "AI OPERATING SYSTEM", C["soft"], 1)
        for idx, (label, x, y, color) in enumerate(labels):
            c.line(400, 240, x, y, color if idx == active else C["border"])
            moving_dot(c, 400, 240, x, y, (t * 3 + idx / 6) % 1, color)
        for idx, (label, x, y, color) in enumerate(labels):
            node(c, x, y, label, color, idx == active)
        title, _, _, color = labels[active]
        c.panel(548, 78, 210, 70, color)
        c.text(565, 98, "ACTIVE SURFACE", C["soft"], 1)
        c.text(565, 120, title, color, 2, 165)
        frames.append(c.p)
    return frames


def video_business_revenue() -> list[bytearray]:
    steps = [
        ("PAIN", 90, 238, C["rose"]),
        ("PLAN", 190, 150, C["cyan"]),
        ("ROI", 330, 128, C["blue"]),
        ("PROPOSAL", 475, 150, C["violet"]),
        ("SPACE", 610, 238, C["teal"]),
        ("SHIFT", 520, 330, C["amber"]),
        ("VAULT", 380, 350, C["green"]),
        ("PORTAL", 225, 330, C["pink"]),
    ]
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES
        active = int(t * len(steps)) % len(steps)
        c = bg(t, "BUSINESS SPACE REVENUE LOOP", "PAIN TO PLAN TO WORKSPACE TO PROOF TO PAID EXPANSION")
        for idx in range(len(steps)):
            _, x1, y1, _ = steps[idx]
            _, x2, y2, _ = steps[(idx + 1) % len(steps)]
            c.line(x1, y1, x2, y2, C["border"])
            if idx == active:
                moving_dot(c, x1, y1, x2, y2, (t * len(steps)) % 1, C["teal"])
        for idx, (label, x, y, color) in enumerate(steps):
            node(c, x, y, label, color, idx == active)
        c.panel(305, 205, 190, 78, C["green"])
        c.text(335, 226, "SELL THIS", C["soft"], 1)
        c.text(330, 248, "LAUNCH KIT", C["green"], 2)
        meter = int(620 * min(1.0, (i + 1) / FRAMES))
        c.rect(90, 402, 620, 18, C["panel"], C["border"])
        c.rect(91, 403, meter, 16, C["green"])
        c.text(92, 382, "SETUP FEE + MONTHLY TIER + CREDITS + SERVICES", C["soft"], 1)
        frames.append(c.p)
    return frames


def video_ai_routing() -> list[bytearray]:
    frames = []
    providers = [("OPENAI", 610, 145, C["green"]), ("CLOUDFLARE", 630, 235, C["blue"]), ("RUNWAY", 610, 325, C["pink"])]
    controls = [("KEYS", 355, 335, C["amber"]), ("LIMITS", 455, 335, C["cyan"]), ("CREDITS", 555, 335, C["violet"])]
    for i in range(FRAMES):
        t = i / FRAMES
        c = bg(t, "AI ROUTING CONTROL PLANE", "MODEL POLICY / CREDITS / LIMITS / FALLBACKS / MARGIN CONTROL")
        c.panel(55, 170, 150, 100, C["cyan"])
        c.text(78, 195, "FEATURE", C["soft"], 2)
        c.text(76, 230, "CALL", C["cyan"], 3)
        c.panel(310, 160, 180, 125, C["violet"])
        c.text(350, 195, "AI ROUTE", C["text"], 3)
        c.text(340, 238, "SERVER POLICY", C["soft"], 1)
        c.line(205, 220, 310, 220, C["cyan"])
        moving_dot(c, 205, 220, 310, 220, (t * 3) % 1, C["cyan"])
        for idx, (label, x, y, color) in enumerate(providers):
            c.line(490, 220, x, y, color)
            moving_dot(c, 490, 220, x, y, (t * 2 + idx / 3) % 1, color)
            node(c, x, y, label, color, int(t * 3) % 3 == idx)
        for label, x, y, color in controls:
            c.panel(x - 40, y - 22, 82, 44, color)
            c.text(x - 25, y - 5, label, color, 1)
            c.line(x, y - 22, 400, 285, C["border"])
        c.panel(48, 330, 220, 62, C["amber"])
        c.text(66, 352, "SELL: AI COST AUDIT", C["amber"], 2)
        frames.append(c.p)
    return frames


def video_offers() -> list[bytearray]:
    offers = [
        ("BUSINESS SPACE LAUNCH", "$2.5K-$10K SETUP", C["teal"]),
        ("NIGHT SHIFT OPERATOR", "$499-$2.5K/MO", C["amber"]),
        ("AI ROUTING AUDIT", "$1.5K-$7.5K", C["violet"]),
        ("PROOF VAULT PORTAL", "$999-$5K SETUP", C["green"]),
        ("CREATOR STOREFRONT", "COMMISSION + TIER", C["pink"]),
    ]
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES
        active = int(t * len(offers)) % len(offers)
        c = bg(t, "MARKET NOW OFFER BOARD", "PACKAGED OFFERS READY FOR SALES PAGES AND DEMO LOOPS")
        for idx, (name, price, color) in enumerate(offers):
            x = 70 + idx * 142
            y = 150 + (20 if idx != active else 0)
            h = 205 if idx == active else 165
            c.panel(x, y, 125, h, color)
            c.text(x + 16, y + 22, f"#{idx+1}", color, 2)
            c.text(x + 16, y + 58, name, C["text"] if idx == active else C["soft"], 1, 96)
            c.text(x + 16, y + h - 42, price, color, 1, 96)
        c.panel(115, 382, 570, 42, C["teal"])
        c.text(135, 397, "BEST WEDGE: BUSINESS SPACE LAUNCH KIT > PROOF > AUTOMATION > GOVERNANCE", C["soft"], 1)
        frames.append(c.p)
    return frames


def video_proof_pipeline() -> list[bytearray]:
    steps = [
        ("INPUT", C["rose"]),
        ("PLAN", C["cyan"]),
        ("EXECUTE", C["violet"]),
        ("CAPTURE", C["amber"]),
        ("PUBLISH", C["green"]),
        ("CONVERT", C["pink"]),
    ]
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES
        active = int(t * len(steps)) % len(steps)
        c = bg(t, "PROOF TO PITCH PIPELINE", "EVERY AI RUN SHOULD BECOME A SALES ASSET")
        y = 218
        centers = []
        for idx, (label, color) in enumerate(steps):
            x = 80 + idx * 125
            centers.append((x, y))
            c.panel(x - 42, y - 45, 88, 90, color)
            c.text(x - 26, y - 8, label, C["text"] if idx == active else C["soft"], 1, 72)
            if idx < len(steps) - 1:
                c.line(x + 46, y, x + 80, y, C["border"])
        x1, y1 = centers[active]
        x2, y2 = centers[(active + 1) % len(centers)]
        if active == len(centers) - 1:
            c.line(x1 + 46, y1, 760, y1, C["pink"])
            c.line(760, y1, 760, 330, C["pink"])
            c.line(760, 330, 80, 330, C["pink"])
            c.line(80, 330, 80, y2 + 45, C["pink"])
        else:
            moving_dot(c, x1 + 46, y1, x2 - 45, y2, (t * len(steps)) % 1, steps[active][1])
        c.panel(150, 330, 500, 70, C["green"])
        c.text(185, 352, "SOURCE > OUTPUT > REPLAY > VAULT > PORTAL > CASE STUDY", C["green"], 1)
        c.text(185, 376, "THIS IS THE SALES MULTIPLIER", C["text"], 2)
        frames.append(c.p)
    return frames


def lzw_pack(indices: bytearray, min_code_size: int = 6) -> bytes:
    clear = 1 << min_code_size
    end = clear + 1
    table = {bytes([i]): i for i in range(clear)}
    next_code = end + 1
    code_size = min_code_size + 1
    codes: list[tuple[int, int]] = [(clear, code_size)]
    w = bytes([indices[0]])
    for value in indices[1:]:
        k = bytes([value])
        wk = w + k
        if wk in table:
            w = wk
            continue
        codes.append((table[w], code_size))
        if next_code < 4096:
            table[wk] = next_code
            next_code += 1
            if next_code == (1 << code_size) and code_size < 12:
                code_size += 1
        else:
            codes.append((clear, code_size))
            table = {bytes([i]): i for i in range(clear)}
            next_code = end + 1
            code_size = min_code_size + 1
        w = k
    codes.append((table[w], code_size))
    codes.append((end, code_size))

    out = bytearray()
    cur = 0
    bits = 0
    for code, size in codes:
        cur |= code << bits
        bits += size
        while bits >= 8:
            out.append(cur & 0xFF)
            cur >>= 8
            bits -= 8
    if bits:
        out.append(cur & 0xFF)
    return bytes(out)


def gif_blocks(data: bytes) -> bytes:
    out = bytearray()
    for i in range(0, len(data), 255):
        block = data[i : i + 255]
        out.append(len(block))
        out.extend(block)
    out.append(0)
    return bytes(out)


def write_gif(relative: str, frames: list[bytearray], delay_cs: int = 12) -> None:
    path = safe_path(relative)
    out = bytearray()
    out.extend(b"GIF89a")
    out.extend(W.to_bytes(2, "little"))
    out.extend(H.to_bytes(2, "little"))
    out.append(0b11110101)  # global table, 64 colors
    out.append(0)
    out.append(0)
    for r, g, b in PALETTE:
        out.extend(bytes([r, g, b]))
    out.extend(b"!\xff\x0bNETSCAPE2.0\x03\x01\x00\x00\x00")
    for frame in frames:
        out.extend(b"!\xf9\x04")
        out.append(0)
        out.extend(delay_cs.to_bytes(2, "little"))
        out.append(0)
        out.append(0)
        out.append(0x2C)
        out.extend((0).to_bytes(2, "little"))
        out.extend((0).to_bytes(2, "little"))
        out.extend(W.to_bytes(2, "little"))
        out.extend(H.to_bytes(2, "little"))
        out.append(0)
        out.append(6)
        out.extend(gif_blocks(lzw_pack(frame, 6)))
    out.append(0x3B)
    path.write_bytes(bytes(out))


VIDEOS = [
    {
        "file": "visuals/videos/platform-command-tour.gif",
        "title": "Platform Command Tour",
        "description": "A moving map of Arsenal's major platform clusters: agents, Business Spaces, AI Route, Vault, Marketplace, and Admin.",
        "frames": video_platform_command,
    },
    {
        "file": "visuals/videos/business-space-revenue-loop.gif",
        "title": "Business Space Revenue Loop",
        "description": "Shows how a business pain point becomes plan, ROI, proposal, workspace, Night Shift, Vault proof, portal, and paid expansion.",
        "frames": video_business_revenue,
    },
    {
        "file": "visuals/videos/ai-routing-control-plane.gif",
        "title": "AI Routing Control Plane",
        "description": "Explains AI Route as the governance, model routing, credits, limits, fallback, and margin-control layer.",
        "frames": video_ai_routing,
    },
    {
        "file": "visuals/videos/market-now-offers.gif",
        "title": "Market Now Offers",
        "description": "Ranks the most marketable offers: Business Space Launch Kit, Night Shift, AI Routing Audit, Proof Vault, and Creator Storefront.",
        "frames": video_offers,
    },
    {
        "file": "visuals/videos/proof-to-pitch-pipeline.gif",
        "title": "Proof To Pitch Pipeline",
        "description": "Turns AI execution into proof assets, portals, case studies, campaigns, and sales conversion.",
        "frames": video_proof_pipeline,
    },
]


def upsert_section(path: str, heading: str, body: str) -> None:
    target = safe_path(path)
    existing = target.read_text(encoding="utf-8") if target.exists() else ""
    marker = f"\n## {heading}\n"
    if marker in existing:
        before, rest = existing.split(marker, 1)
        next_heading = rest.find("\n## ")
        tail = rest[next_heading:] if next_heading >= 0 else ""
        updated = before.rstrip() + marker + "\n" + body.strip() + "\n" + tail
    else:
        updated = existing.rstrip() + marker + "\n" + body.strip() + "\n"
    write_text(path, updated)


def markdown_video_block(video: dict[str, object], prefix: str = "") -> str:
    rel = str(video["file"])
    return f"""### {video["title"]}

{video["description"]}

![{video["title"]}]({prefix}{rel})
"""


def main() -> None:
    features = read_csv("data/feature-inventory.csv")
    offers = read_csv("data/offer-catalog.csv") if safe_path("data/offer-catalog.csv").exists() else []
    for video in VIDEOS:
        write_gif(str(video["file"]), video["frames"]())

    generator_copy = safe_path("tools/generate_readme_videos.py")
    source = Path(__file__).resolve()
    if source != generator_copy.resolve():
        shutil.copyfile(source, generator_copy)

    video_readme = """# Arsenal Atlas Video README

These are code-generated animated README loops. They are intentionally small, public-safe, and reproducible from `tools/generate_readme_videos.py`.

The goal is to let GitHub visitors understand the platform visually before reading long documentation.

""" + "\n".join(markdown_video_block(v) for v in VIDEOS)
    write_text("visuals/video-readme.md", video_readme)

    founder_video_readme = """# Founder Video Storyboard README

Use these loops as a video-first sales narrative. Each animation is a lightweight asset that can sit inside GitHub, decks, landing pages, campaign briefs, and partner enablement docs.

## Narrative Order

1. Platform Command Tour: Arsenal is an operating system, not a chatbot.
2. Business Space Revenue Loop: the flagship offer moves from pain to paid workspace.
3. AI Routing Control Plane: hidden infrastructure becomes governance and margin.
4. Proof To Pitch Pipeline: every run becomes proof for the next sale.
5. Market Now Offers: the system converts into concrete packages buyers can understand.

## Embed Snippets

```md
![Platform Command Tour](visuals/videos/platform-command-tour.gif)
![Business Space Revenue Loop](visuals/videos/business-space-revenue-loop.gif)
![AI Routing Control Plane](visuals/videos/ai-routing-control-plane.gif)
![Market Now Offers](visuals/videos/market-now-offers.gif)
![Proof To Pitch Pipeline](visuals/videos/proof-to-pitch-pipeline.gif)
```

## Offer Tie-In

- Lead with the AI Business Space Launch Kit.
- Attach Night Shift after the first workspace proof is visible.
- Sell AI Routing Audit to technical buyers with existing AI spend.
- Use Proof Vault as the trust layer for every demo.
- Use Creator Storefront and Partner Growth after the first proof bundle exists.
"""
    write_text("visuals/founder-video-storyboard-readme.md", founder_video_readme)

    video_index = """# README Video Index

This folder contains code-generated animated GIF loops for GitHub README embedding.

| Video | File | Use |
| --- | --- | --- |
""" + "\n".join(
        f"| {v['title']} | `{v['file']}` | {v['description']} |" for v in VIDEOS
    ) + """

## Regenerate

```powershell
python tools/generate_readme_videos.py
```
"""
    write_text("visuals/videos/README.md", video_index)

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "generator": "tools/generate_readme_videos.py",
        "format": "animated GIF",
        "dimensions": {"width": W, "height": H, "fps": FPS, "frames_per_video": FRAMES},
        "source_data": [
            "data/feature-inventory.csv",
            "data/offer-catalog.csv",
            "data/strategic-leverage-index.csv",
        ],
        "counts": {
            "feature_rows_available": len(features),
            "offer_rows_available": len(offers),
            "videos": len(VIDEOS),
        },
        "videos": [
            {
                "title": v["title"],
                "file": v["file"],
                "description": v["description"],
                "bytes": safe_path(str(v["file"])).stat().st_size,
            }
            for v in VIDEOS
        ],
        "public_safety": "Generated from Atlas summaries only. No secrets, customer data, screenshots, or production source copied into media.",
    }
    write_text("exports/readme-video-manifest.json", json.dumps(manifest, indent=2))

    readme_body = """The Atlas now includes code-generated animated GIF loops that render directly inside GitHub markdown:

- [Video README](visuals/video-readme.md)
- [Founder video storyboard README](visuals/founder-video-storyboard-readme.md)
- [Video index](visuals/videos/README.md)

Video loops:

![Platform Command Tour](visuals/videos/platform-command-tour.gif)

![Business Space Revenue Loop](visuals/videos/business-space-revenue-loop.gif)

![AI Routing Control Plane](visuals/videos/ai-routing-control-plane.gif)

![Market Now Offers](visuals/videos/market-now-offers.gif)

![Proof To Pitch Pipeline](visuals/videos/proof-to-pitch-pipeline.gif)

Regenerate them with:

```powershell
python tools/generate_readme_videos.py
```
"""
    upsert_section("README.md", "Code-Generated Video README Layer", readme_body)

    report_body = """Added a reproducible code-generated video layer: five animated GIF README loops, a video README gallery, a founder storyboard README, a video index, a generator script, and a manifest.

The generated loops cover platform architecture, Business Space revenue flow, AI Route governance, market-now offers, and the proof-to-pitch pipeline.

Production repo modified: no
"""
    upsert_section("exports/codex-final-report.md", "Code-Generated Video README Addendum", report_body)

    print(json.dumps(manifest["counts"], indent=2))


if __name__ == "__main__":
    main()
