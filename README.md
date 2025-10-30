# 🃏 Yu-Gi-Oh! Card Scraper

This Python tool fetches and processes Yu-Gi-Oh! card data from the **FormatLibrary API**.  
It organizes the raw API data into a clean, CSV-friendly format — including category, icons, type flags, and effect text.

---

## ⚙️ Features

- Fetches card data from **https://www.formatlibrary.com/api/cards**
- Determines the card **category** (`Monster`, `Spell`, or `Trap`) using `humanReadableCardType`
- Builds a combined description from **Pendulum** and **Monster** effects
- Detects and sets **type flags** like `is_fusion`, `is_link`, `is_pendulum`, etc.
- Extracts the correct **icon type** (`Continuous`, `Quick-Play`, `Field`, `Counter`, etc.)
- Only assigns the monster **type** (from `race`) if the card is a Monster
- Exports clean data to CSV for easy database import or analysis

---

## 🧩 Data Fields

| Field | Description |
|--------|-------------|
| `id` | Card passcode |
| `name` | Card name |
| `category` | `"Monster"`, `"Spell"`, or `"Trap"` |
| `icon` | Card icon type (e.g. `"Continuous"`, `"Quick-Play"`, `"Field"`, `"Counter"`) |
| `type` | Monster race (e.g. `"Spellcaster"`, `"Dragon"`) — only for monsters |
| `atk` / `def` / `level` | Monster stats |
| `desc` | Combined Pendulum + Monster effect description |
| `is_fusion`, `is_link`, `is_pendulum`, etc. | Boolean flags for mechanics |

---

## 🧠 Description Builder

If a card has both Pendulum and Monster effects:
