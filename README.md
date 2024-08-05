# Group40_FINALPROJECT_Image-Detection

Growing up, no one ever dreams of being a waste sorter as a full-time career. It is regarded an unpleasant and unhygienic job. But it does not have to be.

With the current advancements in technology, thanks to Artificial Intelligence, automated waste segregation can become a reality. The aim of this project is to fine-tune an object detection model to identify and classify the two most-recycled wastes in Ghana - plastic and metal. Eventually, the hope is that this model would be deployed on a robotic arm replete with a camera and appropriate jaws to enable it sort waste.

The YOLOv8 Object Detection model was fine-tuned with a custom dataset that is an amalgamation of waste datasets obtained from Kaggle and pictures we took ourselves and with the help of family and friends (much gratituede to everyone who helped!). As much as possible, we tried to make the dataset reflect the form and kinds of waste commonly found in Ghana, to ensure the robot is able to tackle waste when placed in the Ghanaian setting. The model was fine-tuned to detect whether a presented image is plastic, metal or other waste. The model can be tested here: https://group40finalprojectimage-detection-7kycesz7rdjbthskgqeott.streamlit.app/

This repository contains  the notebook for fine-tuning the model, the fine-tuned model, the deployment code and the requirements document.

## Acknowledgements
Kaggle Datasets:
