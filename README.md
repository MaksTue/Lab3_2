# YOLOv8 Object Detection with BentoML & Streamlit

Этот проект реализует микросервис на **BentoML** для детекции объектов с помощью **YOLOv8** и веб-интерфейс на **Streamlit**.


1. **Клонируем репозиторий:**
   ```bash
   git clone https://github.com/ТВОЙ_ГИТХАБ_USERNAME/yolo-object-detection.git
   cd yolo-object-detection
   ```

2. **Создаем и активируем виртуальное окружение (рекомендуется):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # для macOS/Linux
   venv\Scripts\activate  # для Windows
   ```

3. **Устанавливаем зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Запуск сервиса BentoML

1. **Запускаем BentoML сервис:**
   ```bash
   bentoml serve bentoml_yolo_service.py:svc
   ```


## 🌍 Запуск Streamlit интерфейса

1. **Запускаем Streamlit:**
   ```bash
   streamlit run streamlit_app.py
   ```


## 📂 Структура проекта
```
📁 yolo-object-detection/
├── bentoml_yolo_service.py   # Сервис BentoML
├── streamlit_app.py          # Веб-интерфейс Streamlit
├── best.pt                   # Обученная модель YOLOv8 (может отсутствовать)
├── requirements.txt          # Список зависимостей
├── README.md                 # Описание проекта
└── .gitignore                # Игнорируемые файлы
```


