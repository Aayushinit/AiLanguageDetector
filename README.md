# 🤖 AI Background Subtractor

> **Real-time background subtraction app using OpenCV and Flask. Watch your camera feed detect motion, shadows, and foreground objects with color-coded visualizations!**

---

## 🌟 Overview

**AI Background Subtractor** is a lightweight Flask-based web application that applies advanced background subtraction techniques (KNN and MOG2) to live camera feeds using **OpenCV**.

The app displays real-time results, showing the original and processed frames side-by-side, where:

* 🟩 **Green** areas represent detected foreground
* 🟥 **Red** areas represent shadows

---

## 🧠 Key Features

### 🎥 Live Camera Feed

* Uses OpenCV to capture webcam input
* Streams results in real-time to a Flask web interface

### 🧪 Background Subtraction Algorithms

* Toggle between:

  * `KNN` — K-Nearest Neighbors
  * `MOG2` — Gaussian Mixture-based
* Optionally display `GMG` (UI placeholder included)

### 🌈 Visual Legend

* Green for foreground (moving subjects)
* Red for shadows

### 💻 Modern Web UI

* Built with Tailwind CSS and FontAwesome
* Responsive layout with animation effects
* Easy toggle buttons to switch between detection algorithms

---

## 🛠️ Technologies Used

| Category        | Tech Stack                           |
| --------------- | ------------------------------------ |
| Backend         | Flask (Python)                       |
| Computer Vision | OpenCV (cv2)                         |
| Frontend        | HTML, Tailwind CSS, FontAwesome      |
| Streaming       | MJPEG over HTTP (`video_feed` route) |

---

## 📂 Project Structure

```
AiBackgroundSubtractor
├── templates
│   └── index.html         # Frontend UI
└── app.py                 # Flask + OpenCV backend
```

---

## 🔌 Flask Endpoints

| Route                    | Description                                   |
| ------------------------ | --------------------------------------------- |
| `/`                      | Home page with video UI                       |
| `/video_feed`            | Live video stream with background subtraction |
| `/set_subtractor/<name>` | Switch between `KNN` and `MOG2` algorithms    |

---

## 🚀 Getting Started

1. **Clone the Repo**

```bash
git clone https://github.com/Aayushinit/AiBackgroundSubtractor.git
cd AiBackgroundSubtractor
```

2. **Install Dependencies**

```bash
pip install flask opencv-python numpy
```

3. **Run the App**

```bash
python app.py
```

4. **Open in Browser**
   Visit [http://localhost:5000](http://localhost:5000)

---

## 🧩 How It Works

* Reads frames from your webcam
* Applies chosen background subtractor (KNN or MOG2)
* Highlights foreground and shadows with colored masks
* Combines original and masked frames side-by-side
* Streams the result to browser via MJPEG

---

## 🧠 Future Enhancements

* Add GMG and CNT subtractors
* Allow uploading of videos instead of just webcam
* Save snapshots or record processed output
* Add sliders to tweak algorithm parameters (sensitivity, learning rate)

---

## 👨‍💻 Author

**Aayush Kadam** — Final Year AI & ML Student | Passionate about AI + CV + Web

> "Turning cameras into intelligent observers using just Python and Flask."

[LinkedIn](https://www.linkedin.com/in/aayush-kadam-a3454a2b8) · [GitHub](https://github.com/Aayushinit)

---

## ⭐️ Show Your Support

If you found this project helpful or inspiring, please ⭐ the repo!

---

## 📜 License

Licensed under the [MIT License](LICENSE).

> All UI and logic created for demonstration and learning purposes.
