import streamlit as st
from PIL import Image
import io

st.title("📸 Passport Photo Sheet Generator")

# --- Upload ---
uploaded_file = st.file_uploader("Upload your photo", type=["jpg", "png", "jpeg"])

# --- Controls ---
col1, col2 = st.columns(2)# --- Photo settings menu columns--- 

with col1:
    width_mm = st.number_input("Photo Width (mm)", value=35)
    height_mm = st.number_input("Photo Height (mm)", value=45)
    dpi = st.number_input("DPI", value=300)

with col2:
    rows = st.number_input("Rows", value=3)
    cols = st.number_input("Columns", value=2)
    margin = st.number_input("Margin (px)", value=200)
    gap = st.number_input("Gap Between Photos (px)", value=100)

generate = st.button("Generate Sheet")

if uploaded_file and generate:

    # --- Convert mm to pixels ---
    width_px = int((width_mm / 25.4) * dpi)# 1 inch = 25.4 mm, so we convert mm to inches and then multiply by dpi to get pixels
    height_px = int((height_mm / 25.4) * dpi)

    # --- A4 size in pixels ---
    a4_width = int((210 / 25.4) * dpi)
    a4_height = int((297 / 25.4) * dpi)

    img = Image.open(uploaded_file)

    # --- Center crop ---
    img_ratio = img.width / img.height #this is in pixels, not mm, but it doesn't matter since we only care about the ratio
    target_ratio = width_px / height_px

    if img_ratio > target_ratio:# too wide → crop sides 
        new_width = int(img.height * target_ratio)
        left = (img.width - new_width) // 2 
        img = img.crop((left, 0, left + new_width, img.height))
    else:
        new_height = int(img.width / target_ratio)
        top = (img.height - new_height) // 2
        img = img.crop((0, top, img.width, top + new_height))

    passport = img.resize((width_px, height_px))

    # --- Create canvas ---
    canvas = Image.new("RGB", (a4_width, a4_height), "white")

    # --- Paste photos ---
    for r in range(rows):
        for c in range(cols):
            x = margin + c * (width_px + gap)
            y = margin + r * (height_px + gap)
            canvas.paste(passport, (x, y))

    # --- Show preview ---
    st.image(canvas, caption="Preview", use_container_width=True)

    # --- Download button ---
    buf = io.BytesIO()
    canvas.save(buf, format="JPEG", dpi=(dpi, dpi))
    st.download_button(
        "Download Printable Sheet",
        buf.getvalue(),
        file_name="passport_sheet.jpg",
        mime="image/jpeg"
    )