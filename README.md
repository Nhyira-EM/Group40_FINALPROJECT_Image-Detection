# Group40_FINALPROJECT_Image-Detection

Growing up, no one ever dreams of being a waste sorter as a full-time career. It is regarded an unpleasant and unhygienic job. But it does not have to be.

With the current advancements in technology, thanks to Artificial Intelligence, automated waste segregation can become a reality. The aim of this project is to fine-tune an object detection model to identify and classify the two most-recycled wastes in Ghana - plastic and metal. Eventually, the hope is that this model would be deployed on a robotic arm replete with a camera and appropriate jaws to enable it sort waste.

We experimented both the YOLOv8 and vit_tiny_patch16_224 models. The YOLOv8 model gave us higher accuracies and functionalities overall. The YOLOv8 Object Detection model was thus fine-tuned with a custom dataset that is an amalgamation of waste datasets obtained from Kaggle and pictures we took ourselves and with the help of family and friends (much gratitude to everyone who helped!). As much as possible, we tried to make the dataset reflect the form and kinds of waste commonly found in Ghana, to ensure the robot is able to tackle waste when placed in the Ghanaian setting. We used roboflow to annotate our images and create our final datset. The model was fine-tuned to detect whether a presented image is plastic, metal or other waste. The model can be tested here: https://group40finalprojectimage-detection-7kycesz7rdjbthskgqeott.streamlit.app/
The app allows a user to take a picture of waste and outputs the type of waste (and the confidence as a decimal). The waste type is then passed to Arduino through the serial monitor to influence where the robotic arm drops the waste.

This repository contains the notebook for fine-tuning the model, the fine-tuned model, the deployment code, our aduino code, our final dataset and the requirements document.

## Acknowledgements
Waste Datasets: https://github.com/garythung/trashnet
Annotations: https://universe.roboflow.com/
