# 📸 Passport Photo Generator (A4 Print Ready)

A Streamlit-based web application that takes a single photo, automatically converts it into passport-size format, and generates a print-ready A4 sheet containing multiple copies for easy printing.

---

## 🚀 Project Overview

This application solves a common real-world problem:

Instead of manually resizing and arranging passport photos in Word or visiting a studio, users can:

- Upload a single image
- Automatically crop to passport aspect ratio
- Resize to standard passport dimensions
- Generate multiple copies on an A4 sheet
- Download a high-resolution print-ready image

The output includes correct DPI metadata for accurate physical printing.

---

## ✅ Current Features

- 📤 Upload photo via Streamlit UI
- ✂️ Automatic aspect-ratio-based center cropping
- 📐 Resize to passport dimensions (e.g., 35mm × 45mm)
- 🖨 Generate A4 layout at 300 DPI
- 🧱 Grid-based placement with configurable margin and spacing
- 🎨 Optional grayscale (black & white) conversion
- 💾 Download final image as high-resolution JPEG
- 📏 Correct DPI metadata for accurate printing

---

## 🧠 Technical Concepts Used

- Pixel-based image processing (Pillow)
- Aspect ratio correction before resizing
- mm → inch → pixel conversion using DPI
- Grid coordinate calculation for layout
- In-memory image export using `BytesIO`
- Print-resolution metadata handling

---

## 🛠 Tech Stack

- Python
- Streamlit
- Pillow (PIL)

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/passport-photo-generator.git
cd passport-photo-generator
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the app

```bash
streamlit run photoapp.py
```

---

## 📂 Project Structure

```
passport-photo-generator/
│
├── photoapp.py
├── requirements.txt
├── README.md
```

---

## 🔮 Future Improvements

Planned enhancements:

- 🤖 Face detection using OpenCV or MediaPipe
- 👁 Automatic eye alignment based on passport standards
- 🌍 Country-specific passport size presets
- 🎚 Adjustable head-size percentage validation
- 📄 Export as PDF option
- 🎨 Background whitening / removal
- 🖼 Live preview crop adjustment tool
- ☁️ Deploy on Streamlit Cloud

---

## 📌 Why This Project

This project demonstrates:

- End-to-end image processing workflow
- Understanding of digital vs physical print dimensions
- Clean UI integration with backend logic
- Practical real-world problem solving
- Proper Git and repository management

---

## 📜 License

This project is for educational and personal use.
