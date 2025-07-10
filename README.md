# Emotica

**Emotica** is a small experimental AI-based web application that detects human emotions from text using a pretrained BERT model. It's built using Python, Flask, and HuggingFace Transformers.

> 💡 This is a concept project — not deployed or released publicly.  
> It's a small personal exploration, not a product with commercial or production-level goals.

---

## 🚀 Features

- 🔍 Detects emotions from any text input using AI
- 🤖 Powered by HuggingFace's `nateraw/bert-base-uncased-emotion` model
- 🧠 Flask-based backend with Transformers and Torch
- 🌐 Clean HTML frontend
- 🧪 A standalone **Demo Mode** for simulated emotion detection
- 📄 basic beginner-friendly codebase

---

## 🛠 Tech Stack

- Python 3
- Flask
- Transformers
- Torch
- HTML + CSS (vanilla)

---

## 📦 Installation

### Step 1: Clone or Download
```bash
git clone https://github.com/dhruv11bhandari/emotica.git
cd emotica
```

### Step 2: Install requirements
```bash
pip install -r requirements.txt
```

### Step 3: Run the app
```bash
python app.py
```

Then open `http://localhost:5000` in your browser.

---

## 🧪 Demo Page

A visual-only fake emotion detection page is available at:
```
http://localhost:5000/demo
```

This page does **not use AI** — it simulates results using JavaScript for presentation/demo purposes.

---

## 📂 File Structure

```
emotica/
│
├── app.py                  # Flask backend logic
├── requirements.txt        # Python dependencies
├── README.md               # You're reading it!
│
└── templates/
    |
    └── demo.html           # Black-themed static demo page
```

---

## 🙋 Why This Exists

This is not a deployed product or a commercial tool.  
It's just a small thought-project — an idea brought to life over curiosity and interest in AI + emotions.

Made by **Dhruv Bhandari** for learning, fun, and mainly cause got bored

---
