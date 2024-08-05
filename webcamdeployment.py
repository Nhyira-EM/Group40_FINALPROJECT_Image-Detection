import streamlit as st
import torch
import serial
import serial.tools.list_ports
import numpy as np
import cv2
from PIL import Image
from ultralytics import YOLO
from huggingface_hub import hf_hub_download
import time

# List available COM ports
ports = list(serial.tools.list_ports.comports())
port_names = [port.device for port in ports]

# Streamlit application
st.title("Object Detection with YOLO")
st.write("Group 40: Francine Arthur & Emmanuel Nhyira Freduah-Agyemang")

# Select COM port
selected_port = st.selectbox("Select COM Port", port_names)

# Initialize serial connection with error handling
if selected_port:
    try:
        arduino = serial.Serial(selected_port, 9600)
    except serial.SerialException as e:
        st.error(f"Could not open COM port: {e}")
        arduino = None

# Download and load the YOLO model
model_path = hf_hub_download(repo_id="Nhyira-EM/Objectdetection", filename="Imgdetec.pt")
model = YOLO(model_path)

def run_inference_and_annotate(image, model, confidence_threshold=0.5):
    # Convert BGR to RGB for inference
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Run inference
    results = model(image_rgb)

    # Process results
    annotated_boxes = []
    detected_objects = []
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
            detected_objects.append((label, score))  # Add label and score to detected objects list

    # Annotate the image
    for (bbox, label, score) in annotated_boxes:
        x1, y1, x2, y2 = map(int, bbox)
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, f'{label} {score:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return image, detected_objects

# Use Streamlit's camera input to capture images from the webcam
camera_input = st.camera_input("Capture Image")

if camera_input:
    # Convert the camera input to an image
    image = Image.open(camera_input)
    image = np.array(image)  # Convert to numpy array

    # Run inference and annotate the image
    annotated_image, detected_objects = run_inference_and_annotate(image, model)

    # Convert annotated image back to PIL format for Streamlit
    annotated_image_pil = Image.fromarray(annotated_image)

    # Display the image
    st.image(annotated_image_pil, caption='Annotated Image', use_column_width=True)

    # Display the types of objects detected
    st.write("Objects detected:")
    for obj, score in detected_objects:
        st.write(f"{obj}: {score:.2f}")
        # Send detected object type to Arduino if connection is successful
        if arduino:
            arduino.write(f"{obj}\n".encode())

# Close the serial connection if it was opened
if arduino:
    arduino.close()