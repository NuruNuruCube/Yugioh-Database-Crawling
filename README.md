# Yu-Gi-Oh! Card Scraper
 
This Python tool fetches and processes Yu-Gi-Oh! card data from the **[YGOProDeck API](https://db.ygoprodeck.com/api-guide/)**.  
It cleans and structures the raw data into a CSV-friendly format — including card categories, icons, monster attributes, and effect text.
 
---
 
## Features
 
- **Data Source:** Fetches all card data directly from the **YGOProDeck API**
- **Category Detection:** Determines if a card is a `Monster`, `Spell`, or `Trap` using `humanReadableCardType`
- **Effect Separation:** Extracts both **Pendulum** and **Monster** effects into separate fields
- **Type Flags:** Automatically detects and sets mechanic flags such as  
  `is_fusion`, `is_synchro`, `is_xyz`, `is_pendulum`, `is_link`, and more
- **Monster Attributes:** Includes detailed monster information such as  
  `type`, `attribute`, `atk`, `def`, `level`, `link`, and `link_arrows`
- **Smart Field Handling:**  
  - Only assigns `type` (race) and `attribute` if the card is a **Monster**  
  - Converts `linkmarkers` into simplified directions (e.g., `T-BL-TR`)
- **Icon Extraction:** Identifies the correct **icon type** for Spell and Trap cards  
  (`Continuous`, `Quick-Play`, `Field`, `Counter`, etc.)
- **Export Ready:** Outputs structured, human-readable data in CSV format — perfect for databases, analytics, or web apps
 
---
 
## Data Fields
 
| ID   | Field               | Description                                                                                           |
|------|---------------------|-------------------------------------------------------------------------------------------------------|
| `01` | `passcode`          | Card passcode (unique identifier)                                                                     |
| `02` | `name`              | Card name                                                                                             |
| `03` | `category`          | Card category — `"Monster"`, `"Spell"`, or `"Trap"`                                                   |
| `04` | `type`              | Monster type (e.g. `"Spellcaster"`, `"Dragon"`) — only for monsters                                   |
| `05` | `attribute`         | Monster attribute (e.g. `"Earth"`, `"Fire"`, `"Water"`, `"Wind"`, `"Dark"`) — only for monsters       |
| `06` | `atk`               | Monster ATK value                                                                                     |
| `07` | `def`               | Monster DEF value                                                                                     |
| `08` | `level`             | Monster level or rank                                                                                 |
| `09` | `link`              | Monster Link rating                                                                                   |
| `10` | `link_arrows`       | Monster Link arrows (e.g. `T`, `L`, `R`, `B`, `BL`, `BR`, `TL`, `TR`)                                 |
| `11` | `description`       | Monster or card effect description                                                                    |
| `12` | `pendulum_effect`   | Pendulum effect text (only for Pendulum Monsters)                                                     |
| `13` | `pendulum_scale`    | Pendulum scale value                                                                                  |
| `14` | `is_normal`         | Boolean flag — Normal Monster                                                                         |
| `15` | `is_effect`         | Boolean flag — Effect Monster                                                                         |
| `16` | `is_fusion`         | Boolean flag — Fusion Monster                                                                         |
| `17` | `is_ritual`         | Boolean flag — Ritual Monster                                                                         |
| `18` | `is_synchro`        | Boolean flag — Synchro Monster                                                                        |
| `19` | `is_xyz`            | Boolean flag — Xyz Monster                                                                            |
| `20` | `is_pendulum`       | Boolean flag — Pendulum Monster                                                                       |
| `21` | `is_link`           | Boolean flag — Link Monster                                                                           |
| `22` | `is_flip`           | Boolean flag — Flip effect                                                                            |
| `23` | `is_gemini`         | Boolean flag — Gemini Monster                                                                         |
| `24` | `is_spirit`         | Boolean flag — Spirit Monster                                                                         |
| `25` | `is_toon`           | Boolean flag — Toon Monster                                                                           |
| `26` | `is_tuner`          | Boolean flag — Tuner Monster                                                                          |
| `27` | `is_union`          | Boolean flag — Union Monster                                                                          |
| `28` | `icon`              | Card icon (e.g. `"Continuous"`, `"Quick-Play"`, `"Field"`, `"Counter"`) — only for Spells or Traps    |

## How to use
1. add input.csv
2. run main.py