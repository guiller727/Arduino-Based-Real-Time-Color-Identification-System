import serial #pip install pyserial
import time

# ---------------- COLOR DATA ----------------
HTML_COLORS = {
    "Alice Blue": (240, 248, 255),
    "Antique White": (250, 235, 215),
    "Aqua": (0, 255, 255),
    "Aquamarine": (127, 255, 212),
    "Azure": (240, 255, 255),
    "Beige": (245, 245, 220),
    "Bisque": (255, 228, 196),
    "Black": (0, 0, 0),
    "Blanched Almond": (255, 235, 205),
    "Blue": (0, 0, 255),
    "Blue Violet": (138, 43, 226),
    "Brown": (165, 42, 42),
    "Burly Wood": (222, 184, 135),
    "Cadet Blue": (95, 158, 160),
    "Chartreuse": (127, 255, 0),
    "Chocolate": (210, 105, 30),
    "Coral": (255, 127, 80),
    "Cornflower Blue": (100, 149, 237),
    "Cornsilk": (255, 248, 220),
    "Crimson": (220, 20, 60),
    "Cyan": (0, 255, 255),
    "Dark Blue": (0, 0, 139),
    "Dark Cyan": (0, 139, 139),
    "Dark Goldenrod": (184, 134, 11),
    "Dark Gray": (169, 169, 169),
    "Dark Green": (0, 100, 0),
    "Dark Khaki": (189, 183, 107),
    "Dark Magenta": (139, 0, 139),
    "Dark Olive Green": (85, 107, 47),
    "Dark Orange": (255, 140, 0),
    "Dark Orchid": (153, 50, 204),
    "Dark Red": (139, 0, 0),
    "Dark Salmon": (233, 150, 122),
    "Dark Sea Green": (143, 188, 139),
    "Dark Slate Blue": (72, 61, 139),
    "Dark Slate Gray": (47, 79, 79),
    "Dark Turquoise": (0, 206, 209),
    "Dark Violet": (148, 0, 211),
    "Deep Pink": (255, 20, 147),
    "Deep Sky Blue": (0, 191, 255),
    "Dim Gray": (105, 105, 105),
    "Dodger Blue": (30, 144, 255),
    "Fire Brick": (178, 34, 34),
    "Floral White": (255, 250, 240),
    "Forest Green": (34, 139, 34),
    "Fuchsia": (255, 0, 255),
    "Gainsboro": (220, 220, 220),
    "Ghost White": (248, 248, 255),
    "Gold": (255, 215, 0),
    "Goldenrod": (218, 165, 32),
    "Gray": (128, 128, 128),
    "Green": (0, 128, 0),
    "Green Yellow": (173, 255, 47),
    "Honey Dew": (240, 255, 240),
    "Hot Pink": (255, 150, 230),
    "Indian Red": (205, 92, 92),
    "Indigo": (75, 0, 130),
    "Ivory": (255, 255, 240),
    "Khaki": (240, 230, 140),
    "Lavender": (230, 230, 250),
    "Lavender Blush": (255, 240, 245),
    "Lawn Green": (124, 252, 0),
    "Lemon Chiffon": (255, 250, 205),
    "Light Blue": (173, 216, 230),
    "Light Coral": (240, 128, 128),
    "Light Cyan": (224, 255, 255),
    "Light Goldenrod Yellow": (250, 250, 210),
    "Light Gray": (211, 211, 211),
    "Light Green": (144, 238, 144),
    "Light Pink": (255, 182, 193),
    "Light Salmon": (255, 160, 122),
    "Light Sea Green": (32, 178, 170),
    "Light Sky Blue": (135, 206, 250),
    "Light Slate Gray": (119, 136, 153),
    "Light Steel Blue": (176, 196, 222),
    "Light Yellow": (255, 255, 224),
    "Lime": (0, 255, 0),
    "Lime Green": (50, 205, 50),
    "Linen": (250, 240, 230),
    "Magenta": (255, 0, 255),
    "Maroon": (128, 0, 0),
    "Medium Aquamarine": (102, 205, 170),
    "Medium Blue": (0, 0, 205),
    "Medium Orchid": (186, 85, 211),
    "Medium Purple": (147, 112, 219),
    "Medium Sea Green": (60, 179, 113),
    "Medium Slate Blue": (123, 104, 238),
    "Medium Spring Green": (0, 250, 154),
    "Medium Turquoise": (72, 209, 204),
    "Medium Violet Red": (199, 21, 133),
    "Midnight Blue": (25, 25, 112),
    "Mint Cream": (245, 255, 250),
    "Misty Rose": (255, 228, 225),
    "Moccasin": (255, 228, 181),
    "Navajo White": (255, 222, 173),
    "Navy": (0, 0, 128),
    "Old Lace": (253, 245, 230),
    "Olive": (128, 128, 0),
    "Olive Drab": (107, 142, 35),
    "Orange": (255, 165, 0),
    "Orange Red": (255, 69, 0),
    "Orchid": (218, 112, 214),
    "Pale Goldenrod": (238, 232, 170),
    "Pale Green": (152, 251, 152),
    "Pale Turquoise": (175, 238, 238),
    "Pale Violet Red": (219, 112, 147),
    "Papaya Whip": (255, 239, 213),
    "Peach Puff": (255, 218, 185),
    "Peru": (205, 133, 63),
    "Pink": (255, 192, 203),
    "Plum": (221, 160, 221),
    "Powder Blue": (176, 224, 230),
    "Purple": (128, 0, 128),
    "Rebecca Purple": (102, 51, 153),
    "Red": (255, 0, 0),
    "Rosy Brown": (188, 143, 143),
    "Royal Blue": (65, 105, 225),
    "Saddle Brown": (139, 69, 19),
    "Salmon": (250, 128, 114),
    "Sandy Brown": (244, 164, 96),
    "Sea Green": (46, 139, 87),
    "Sea Shell": (255, 245, 238),
    "Sienna": (160, 82, 45),
    "Silver": (192, 192, 192),
    "Sky Blue": (135, 206, 235),
    "Slate Blue": (106, 90, 205),
    "Slate Gray": (112, 128, 144),
    "Snow": (255, 250, 250),
    "Spring Green": (0, 255, 127),
    "Steel Blue": (70, 130, 180),
    "Tan": (210, 180, 140),
    "Teal": (0, 128, 128),
    "Thistle": (216, 191, 216),
    "Tomato": (255, 99, 71),
    "Turquoise": (64, 224, 208),
    "Violet": (238, 130, 238),
    "Wheat": (245, 222, 179),
    "White": (255, 255, 255),
    "White Smoke": (245, 245, 245),
    "Yellow": (255, 255, 0),
    "Yellow Green": (154, 205, 50),
}


COLOR_FAMILIES = {

    "Red": [
        "Indian Red", "Light Coral", "Salmon", "Dark Salmon",
        "Light Salmon", "Crimson", "Red",
        "Fire Brick", "Dark Red"
    ],

    "Pink": [
        "Pink", "Light Pink", "Hot Pink",
        "Deep Pink", "Medium Violet Red", "Plum",
        "Pale Violet Red", "Lavender Blush", "Misty Rose"
    ],

    "Orange": [
        "Coral", "Tomato", "Orange Red",
        "Dark Orange", "Orange"
    ],

    "Yellow": [
        "Gold", "Yellow", "Light Yellow",
        "Lemon Chiffon", "Light Goldenrod Yellow",
        "Papaya Whip", "Moccasin", "Peach Puff",
        "Pale Goldenrod", "Khaki", "Dark Khaki"
    ],

    "Purple": [
        "Lavender", "Thistle", "Violet",
        "Orchid", "Fuchsia", "Magenta",
        "Medium Orchid", "Medium Purple",
        "Rebecca Purple", "Blue Violet",
        "Dark Violet", "Dark Orchid",
        "Dark Magenta", "Purple", "Indigo",
        "Slate Blue", "Dark Slate Blue",
        "Medium Slate Blue"
    ],

    "Green": [
        "Green Yellow", "Chartreuse", "Lawn Green",
        "Lime", "Lime Green", "Pale Green",
        "Light Green", "Medium Spring Green",
        "Spring Green", "Medium Sea Green",
        "Sea Green", "Forest Green", "Green",
        "Dark Green", "Yellow Green", "Olive Drab",
        "Olive", "Dark Olive Green", "Medium Aquamarine",
        "Dark Sea Green", "Aquamarine"
    ],

    "Cyan": [
        "Light Sea Green", "Dark Cyan", "Teal"
    ],

    "Blue": [
        "Aqua", "Cyan", "Light Cyan",
        "Pale Turquoise",
        "Turquoise", "Medium Turquoise",
        "Dark Turquoise", "Cadet Blue",
        "Steel Blue", "Light Steel Blue",
        "Powder Blue", "Light Blue",
        "Sky Blue", "Light Sky Blue",
        "Deep Sky Blue", "Dodger Blue",
        "Cornflower Blue", "Royal Blue",
        "Blue", "Medium Blue", "Dark Blue",
        "Navy", "Midnight Blue"
    ],

    "Brown": [
        "Cornsilk", "Blanched Almond", "Bisque",
        "Navajo White", "Wheat", "Burly Wood",
        "Tan", "Rosy Brown", "Sandy Brown",
        "Goldenrod", "Dark Goldenrod",
        "Peru", "Chocolate", "Saddle Brown",
        "Sienna", "Brown", "Maroon"
    ],

    "White": [
        "White", "Snow", "Honey Dew", "Mint Cream",
        "Azure", "Alice Blue", "Ghost White",
        "White Smoke", "Sea Shell", "Beige",
        "Old Lace", "Floral White", "Ivory",
        "Antique White", "Linen"
    ],

    "Gray": [
        "Gainsboro", "Light Gray", "Silver",
        "Dark Gray", "Gray", "Dim Gray",
        "Light Slate Gray", "Slate Gray",
        "Dark Slate Gray"
    ],

    "Black": [
        "Black"
    ]
}


COLOR_DESCRIPTIONS = {
    "Red": "Dark, strong",
    "Green": "Medium, soft",
    "Blue": "Medium, calm",
    "Yellow": "Very bright",
    "Orange": "Bright, strong",
    "Purple": "Dark, deep",
    "Pink": "Light, soft",
    "Brown": "Dark, dull",
    "White": "Very bright",
    "Gray": "Low contrast",
    "Black": "Very dark",
    "Cyan": "Light, soft"
}


# ---------------- FUNCTIONS ----------------
def closest_html_color(R, G, B):
    best_name = None
    best_dist = float('inf')
    for name, (r, g, b) in HTML_COLORS.items():
        d = (R - r)**2 + (G - g)**2 + (B - b)**2
        if d < best_dist:
            best_dist = d
            best_name = name
    return best_name

def color_family_from_html(name):
    for family, names in COLOR_FAMILIES.items():
        if name in names:
            return family
    return name.split()[0]

# ---------------- SERIAL SETUP ----------------
PORT = "COM3"        # MUST match Arduino IDE
BAUD = 9600

ser = serial.Serial(PORT, BAUD, timeout=2)
time.sleep(2)
ser.reset_input_buffer()
ser.reset_output_buffer()

print("Connected to Arduino on", PORT)


# ---------------- MAIN LOOP ----------------
while True:
    try:
        line = ser.readline().decode(errors="ignore").strip()
        if not line:
            continue

        print("From Arduino:", line)

        # Expecting: RGB:R,G,B
        if not line.startswith("RGB:"):
            continue

        data = line.replace("RGB:", "")
        R, G, B = map(int, data.split(","))

        # ---- COLOR PROCESSING ----
        html_name = closest_html_color(R, G, B)
        family = color_family_from_html(html_name)

        # ---- SEND REPLY ----
        desc = COLOR_DESCRIPTIONS.get(family, "Unknown")
        reply = f"OK|{family}|{html_name}|{desc}\n"
        ser.write(reply.encode())
        ser.flush()

        print(f"Sent to Arduino: {reply.strip()}")

    except Exception as e:
        print("Error:", e)
        time.sleep(0.1)
        break
