import streamlit as st
import requests
from PIL import Image, ImageDraw
import io

API_URL = "http://127.0.0.1:3000/detect"

st.title("🔍 YOLOv8 Object Detection")

uploaded_file = st.file_uploader("📤 Загрузите изображение", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Исходное изображение", use_container_width=True)

    if st.button("🚀 Распознать объекты"):
        with st.spinner("Обработка..."):
            try:
                img_byte_arr = io.BytesIO()
                image.save(img_byte_arr, format=image.format)
                img_byte_arr = img_byte_arr.getvalue()

                files = {"image": ("image", img_byte_arr, "image/jpeg")}
                response = requests.post(API_URL, files=files)

                if response.status_code == 200:
                    results = response.json()

                    draw = ImageDraw.Draw(image)
                    for det in results:
                        x1, y1, x2, y2 = det["x1"], det["y1"], det["x2"], det["y2"]
                        confidence = det["confidence"]
                        class_name = det["class_name"]

                        draw.rectangle([(x1, y1), (x2, y2)], outline="red", width=3)
                        draw.text((x1, y1), f"{class_name} ({confidence:.2f})", fill="red")

                    st.image(image, caption=f"🔎 Detected: {class_name}", use_container_width=True)
                else:
                    st.error(f"Ошибка сервиса: {response.status_code}")
                    st.write(response.text)
            except Exception as e:
                st.error(f"Ошибка: {e}")
