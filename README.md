# Group40_FINALPROJECT_Image-Detection

Growing up, no one ever dreams of being a waste sorter as a full-time career. It is regarded an unpleasant and unhygienic job. But it does not have to be.

With the current advancements in technology, thanks to Artificial Intelligence, automated waste segregation can become a reality. The aim of this project is to fine-tune an object detection model to identify and classify the two most-recycled wastes in Ghana - plastic and metal. Eventually, the hope is that this model would be deployed on a robotic arm replete with a camera and appropriate jaws to enable it sort waste.

YOU CAN VIEW A DEMO OF OUR WORK HERE: https://www.youtube.com/watch?v=XpqooOO5SP8

We experimented both the YOLOv8 and vit_tiny_patch16_224 models. The YOLOv8 model gave us higher accuracies and functionalities overall. The YOLOv8 Object Detection model was thus fine-tuned with a custom dataset that is an amalgamation of waste datasets obtained from Kaggle and pictures we took ourselves and with the help of family and friends (much gratitude to everyone who helped!). As much as possible, we tried to make the dataset reflect the form and kinds of waste commonly found in Ghana, to ensure the robot is able to tackle waste when placed in the Ghanaian setting. We used roboflow to annotate our images and create our final datset. The model was fine-tuned to detect whether a presented image is plastic, metal or other waste. The model can be tested here: https://group40finalprojectimage-detection-7kycesz7rdjbthskgqeott.streamlit.app/
The app allows a user to take a picture of waste and outputs the type of waste (and the confidence as a decimal). The waste type is then passed to Arduino through the serial monitor to influence where the robotic arm drops the waste.

This repository contains the notebook for fine-tuning the model, the fine-tuned model, the deployment code, our aduino code, our final dataset and the requirements document.

## Deployment
The model was deployed using Streamlit. The Streamlit app can be accessed here: https://group40finalprojectimage-detection-7kycesz7rdjbthskgqeott.streamlit.app/
 
To deploy the app using Streamlit online, you can follow these steps:

1. Use the python file named `deployment.py` in our github repository.

2. Go to streamlit online which can be accessed with this link: https://streamlit.io/

3. Type in the path of our github repository. then type in the name `deployment.py` which is the file that contains the streamlit deployment code.

4. Don't worry about a requirements text file. To simplify the deployment process, we have already created a `requirements.txt` file in our GitHub repository. You can simply pull the file from the repository to install the necessary dependencies.

Once deployed, users can access the app through the provided URL and upload images to classify the waste. The waste type and confidence level will be displayed, and the waste type can be passed to Arduino for further actions.

To simplify the deployment process, we have already created a `requirements.txt` file in our GitHub repository. You can simply pull the file from the repository to install the necessary dependencies.

Once deployed, users can access the app through the provided URL and upload images to classify the waste. The waste type and confidence level will be displayed, and the waste type can be passed to Arduino for further actions.

## Acknowledgements
Waste Datasets: https://github.com/garythung/trashnet
Annotations: https://universe.roboflow.com/
