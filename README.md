# 🌐 Language Detector Web App

> **Detect the language of any text input instantly using Python, Flask, and LangDetect. Tracks detection history with a clean web UI and smart caching.**

---
<p align = "center" ><img src="Screenshot 2025-07-08 124108.png" width="100%">
</p>
## 📖 Overview

**Language Detector** is a full-stack Flask web application that uses the `langdetect` library to detect the language of any given text. It includes:

* 🧠 **Automatic Language Detection** using `langdetect`
* 💾 **Detection History Tracking** with SQLite (via SQLAlchemy)
* ⚡ **Smart Caching** for faster repeat detection
* 🖥️ **Responsive Web Interface** with recent detection previews

Built for fast prototyping, linguistic demos, and simple multi-language handling.

---

## ⚙️ Features

### 🧠 Instant Language Detection

* Uses `langdetect` to identify the language code (e.g., `en`, `fr`, `de`, `hi`)
* Shows both code and full language name using `pycountry`

### 💾 Recent Detection History

* Displays last 5 detections on home page
* View complete paginated history on `/history` page

### 🚀 Fast Caching

* Avoids repeated detection for same text using a TTL-based cache (5 minutes default)

### 🖥️ Clean Web Interface

* Built with HTML/CSS and modular templates (using Jinja2)
* Includes 404 and 500 error pages

---

## 🛠️ Technologies Used

| Category           | Tech Stack                        |
| ------------------ | --------------------------------- |
| Backend            | Flask (Python)                    |
| Language Detection | langdetect, pycountry             |
| Database           | SQLite + SQLAlchemy               |
| Frontend           | HTML, CSS (custom), JS            |
| Caching            | TTL-based manual Python decorator |

---

---

## 🔌 Flask Endpoints

| Route      | Description                                    |
| ---------- | ---------------------------------------------- |
| `/`        | Home page with text input + recent detections  |
| `/detect`  | API endpoint for POST-based language detection |
| `/history` | Full history page with pagination              |

---

## 🚀 Getting Started

1. **Clone the Repository**

```bash
git clone https://github.com/Aayushinit/LanguageDetectorApp.git
cd LanguageDetectorApp
```

2. **Install Dependencies**

```bash
pip install flask langdetect pycountry flask_sqlalchemy
```

3. **Run the App**

```bash
python app.py
```

4. **Visit in Browser**
   [http://localhost:5000](http://localhost:5000)

---

## 💡 How It Works

* Accepts user text input from the frontend
* `langdetect` attempts to detect language code
* `pycountry` maps language code to human-readable name
* Result is cached and also saved in the database
* History is displayed and paginated with timestamps

---

## 🔮 Future Improvements

* 🔤 Display detection confidence (if supported)
* 🌍 Add language flag icons
* 💬 Translate detected text
* 💽 Export detection history as CSV
* 📱 Mobile-optimized interface with Tailwind CSS

---

## 👨‍💻 Author

**Aayush Kadam** — Final Year AI & ML Student | Python & Web Enthusiast

> "Giving apps the power to understand language—one line at a time."

[LinkedIn](https://www.linkedin.com/in/aayush-kadam-a3454a2b8) · [GitHub](https://github.com/Aayushinit)

---

## ⭐️ Show Your Support

If you find this project helpful, please ⭐ the repo and share with your network!

---

## 📜 License

Licensed under the [MIT License](LICENSE).

> UI and logic were developed for educational and demonstration purposes.
