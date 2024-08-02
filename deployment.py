import streamlit as st
import cv2
import torch
import numpy as np
from huggingface_hub import hf_hub_download
from PIL import Image

# Load YOLO model
model_path = hf_hub_download(repo_id="Nhyira-EM/Objectdetection", filename="Imgdetec.pt")
with open(model_path, 'rb') as f:
    final_model = torch.load(f)

def run_inference_and_annotate(image, model, confidence_threshold=0.5):
    # Convert PIL Image to OpenCV format (BGR)
    image = np.array(image)
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Set the model to evaluation mode
    model.eval()

    # Run inference with no gradient calculation
    with torch.no_grad():
        results = model(image_bgr)

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
        cv2.rectangle(image_bgr, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image_bgr, f'{label} {score:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Convert back to PIL Image for Streamlit
    return Image.fromarray(cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB))

# Streamlit application
st.title("Webcam Object Detection with YOLO")

# Button to start the webcam
start_button = st.button("Start Webcam")

if start_button:
    st.write("Webcam is active. Click the 'Stop Webcam' button to end.")
    # Webcam input using Streamlit's camera input
    img = st.camera_input("Capture Image")

    if img:
        # Convert image to PIL format
        image = Image.open(img)

        # Run inference and annotate the image
        annotated_image = run_inference_and_annotate(image, final_model)

        # Display the annotated image
        st.image(annotated_image, caption="Annotated Image")