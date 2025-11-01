import requests
import csv
import time
import urllib.parse
import os
import re
 
INPUT_CSV = "Input.csv"
OUTPUT_CSV = "yugioh_cards.csv"
 
HEADERS = [
    "id",
    "passcode",
    "name",
    "category",
    "attribute",
    "type",
    "level",
    "atk",
    "def",
    "link",
    "pendulum_scale",
    "description",
    "pendulum_effect",
    "link_arrows",
    "is_normal",
    "is_effect",
    "is_fusion",
    "is_ritual",
    "is_synchro",
    "is_xyz",
    "is_pendulum",
    "is_link",
    "is_flip",
    "is_gemini",
    "is_spirit",
    "is_toon",
    "is_tuner",
    "is_union",
    "icon",
]
 
def scrape_card(card_name,id):
    """
    Fetch card data from the YGOPRODeck API.
    Example: https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Dark%20Magician
    """
    url = f"https://db.ygoprodeck.com/api/v7/cardinfo.php?name={card_name}"
 
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        card_json = res.json()
    except Exception as e:
        print(f"⚠️ {card_name} failed: {e}")
        return None
 
    # Some cards have multiple results (alternate arts, etc.)
    card = card_json["data"][0]
 
    data = {h: "" for h in HEADERS}
 
    # --- Simple INFO ---
    data["id"] = id
    data["name"] = card.get("name", "")
    data["passcode"] = str(card.get("id", ""))
    data["link"] = card.get("linkval", -1)
    data["atk"] = card.get("atk", -1)
    data["def"] = card.get("def", -1)
    data["level"] = card.get("level", -1)
    data["pendulum_scale"] = card.get("scale", -1)
    data["attribute"] = card.get("attribute", "")
 
    # --- DESCRIPTION & PENDULUM EFFECT ---
    pendulum_effect = card.get("pend_desc", "").strip()
    monster_effect = card.get("monster_desc", "").strip()
    base_desc = card.get("desc", "").strip()

    # Save pendulum effect separately
    data["pendulum_effect"] = pendulum_effect

    # Description logic:
    # 1️⃣ If pendulum effect exists → description = monster_desc
    # 2️⃣ Else → description = desc
    if pendulum_effect:
        data["description"] = monster_effect
    else:
        data["description"] = base_desc
    # --- CATEGORY + TYPE + ICON FLAGS (using 'humanReadableCardType') ---
    card_type = (card.get("humanReadableCardType") or "").lower()
 
    # --- Category ---
    if "spell" in card_type:
        data["category"] = "Spell"
    elif "trap" in card_type:
        data["category"] = "Trap"
    elif "monster" in card_type:
        data["category"] = "Monster"
        data["type"] = card.get("race", "")
 
    # --- Icon --- Apply For spell/trap card set icon as normal if card don't have specific icon
    if data["category"] in ["Spell", "Trap"]:
        if "continuous" in card_type:
            data["icon"] = "Continuous"
        elif "quick-play" in card_type:
            data["icon"] = "Quick-Play"
        elif "equip" in card_type:
            data["icon"] = "Equip"
        elif "field" in card_type:
            data["icon"] = "Field"
        elif "ritual" in card_type:
            data["icon"] = "Ritual"
        elif "counter" in card_type:
            data["icon"] = "Counter"
        else:
            data["icon"] = "Nornal"
 
    # --- Type flags --- Apply For monster card
    flags = [
        "normal", "effect", "fusion", "ritual", "synchro", "xyz",
        "pendulum", "link", "flip", "gemini", "spirit",
        "toon", "tuner", "union"
    ]
 
    for f in flags:
        data[f"is_{f}"] = "1" if f in card_type else "0"
 
    # --- LINK ARROWS (if present) ---
    link_map = {
        "top": "T",
        "bottom": "B",
        "left": "L",
        "right": "R",
        "top-left": "TL",
        "top-right": "TR",
        "bottom-left": "BL",
        "bottom-right": "BR",
    }
 
    if "linkmarkers" in card:
        if isinstance(card["linkmarkers"], str):
            raw_markers = [m.strip().lower() for m in card["linkmarkers"].split(",")]
        elif isinstance(card["linkmarkers"], list):
            raw_markers = [str(m).strip().lower() for m in card["linkmarkers"]]
        else:
            raw_markers = []
 
        # Map to short letter codes
        converted = [link_map.get(m, "") for m in raw_markers if m in link_map]
 
        # Join with hyphens
        data["link_arrows"] = "-".join(converted)
    else:
        data["link_arrows"] = ""
 
    # Fallbacks for missing numeric values
    for key in ["atk", "def", "level", "link", "pendulum_scale"]:
        if data[key] in ["", None]:
            data[key] = -1
 
    return data
 
 
def save_to_csv(card_data):
    file_exists = os.path.exists(OUTPUT_CSV)
    with open(OUTPUT_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        if not file_exists:
            writer.writeheader()
        writer.writerow(card_data)
 
def main():
    if not os.path.exists(INPUT_CSV):
        print("Please upload 'Input.csv' (must have column 'name')")
        return
 
    with open(INPUT_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get("name", "").strip()
            id = row.get("id", "").strip()
            if not name:
                continue
 
            url = urllib.parse.quote(name)
            print(f"🔍 Scraping {name}...")
            data = scrape_card(url, id)
            if data:
                save_to_csv(data)
                print(f"✅ Saved {data['name']}")
            else:
                print(f"❌ Failed {name}")
            time.sleep(1)
 
    print("\n🎉 Done! Check 'yugioh_cards.csv' in right panel (Files).")
 
main()