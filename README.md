# Project RBG 🎨

A sleek, interactive command-line application built in Python that allows users to mix digital colors using RGB values. The program dynamically calculates the exact mathematical average of two chosen colors and finds the closest matching color block stored inside an external JSON database.

---

## ✨ Features
* **Dynamic Loading Animation:** Uses terminal ANSI escape sequences to create a smooth, clean loading sequence.
* **RGB Color Previews:** Displays custom color blocks (`█████`) directly inside your terminal using true 24-bit color formatting.
* **Error Prevention:** Robust input handling that ignores accidental spaces or capitalization issues, gently prompting users to re-enter inputs on typos.
* **Mathematical Precision:** Employs an absolute-difference algorithm to map user mixtures to the closest available color in the dataset.

---

## 🛠️ How It Works
1. The script loads an external `colours.json` containing preset color names mapped to their `[R, G, B]` arrays.
2. The user inputs two distinct colors to mix.
3. The program averages the corresponding RGB channels using floor division:
   $$R_{mid} = \lfloor \frac{R_1 + R_2}{2} \rfloor$$
4. It compares the resulting average against every color in the database using a distance calculation to find the closest match.
5. The terminal prints a beautifully formatted result card showcasing the input colors alongside the blended final product.

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3 installed on your machine. You can verify this by running:
```bash
python3 --version
