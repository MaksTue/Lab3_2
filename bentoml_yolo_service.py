import bentoml
from bentoml.io import Image, JSON
from ultralytics import YOLO
import numpy as np
from PIL import Image as PILImage

# Загружаем обученную модель YOLOv8
model = YOLO("best.pt")  # Убедись, что модель находится в этой папке

# Определяем сервис BentoML
svc = bentoml.Service("yolo_service")

# Классы (изменил порядок для уникальности)
CLASS_NAMES = ["Toothbrush", "Soap", "Toothpaste"]

@svc.api(input=Image(), output=JSON())
def detect(image: PILImage):
    image = np.array(image)

    results = model.predict(image)

    if results is None or len(results) == 0 or len(results[0].boxes) == 0:
        return []

    detection_list = []

    for result in results[0].boxes:
        class_id = int(result.cls)
        class_name = CLASS_NAMES[class_id] if class_id < len(CLASS_NAMES) else "Unknown"

        box = {
            "class": class_id,
            "class_name": class_name,
            "confidence": float(result.conf),
            "x1": float(result.xyxy[0][0]),
            "y1": float(result.xyxy[0][1]),
            "x2": float(result.xyxy[0][2]),
            "y2": float(result.xyxy[0][3]),
        }
        detection_list.append(box)

        # Логирование
        print(f"Обнаружен {class_name} с вероятностью {box['confidence']:.2f}")

    return detection_list
