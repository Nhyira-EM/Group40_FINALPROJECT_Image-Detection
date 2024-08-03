import streamlit as st
import torch
import numpy as np
from PIL import Image
from ultralytics import YOLO  # Ensure the correct package is used

# Loading the YOLO model
model_path = model_path = hf_hub_download(repo_id="Nhyira-EM/Objectdetection", filename="Imgdetec.pt")
model = YOLO(model_path)

def run_inference_and_annotate(image, model, confidence_threshold=0.5):
    # Convert BGR to RGB for inference
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Run inference
    results = model(image_rgb)
    
    # Process results
    annotated_boxes = []
    for result in results:
        boxes = result.boxes  # Extract bounding boxes and scores
        for box in boxes:
            bbox = box.xyxy[0].tolist()  # Convert bbox tensor to list
            score = box.conf.item()
            class_id = int(box.cls.item())

            label = 'other'
            if score >= confidence_threshold:
                if class_id == 0:
                    label = 'metal'
                elif class_id == 1:
                    label = 'plastic'

            annotated_boxes.append((bbox, label, score))

    # Annotate the image
    for (bbox, label, score) in annotated_boxes:
        x1, y1, x2, y2 = map(int, bbox)
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, f'{label} {score:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return image

# Streamlit application
st.title("Object Detection with YOLO")
st.write("Group 40: Francine Arthur & Emmanuel Nhyira Freduah-Agyemang")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Open and process the image
    image = Image.open(uploaded_file)
    image = np.array(image)  # Convert to numpy array

    # Run inference and annotate the image
    annotated_image = run_inference_and_annotate(image, model)

    # Convert annotated image back to PIL format for Streamlit
    annotated_image_pil = Image.fromarray(annotated_image)

    # Display the image
    st.image(annotated_image_pil, caption='Annotated Image', use_column_width=True)
