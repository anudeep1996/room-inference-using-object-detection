# Room-inference-using-object-detection
## Introduction:
Scene recognition is one of the primary responsibilities of Computer vision. Computer Vision is described as a field of study which seeks to develop techniques to help computers "see" and understand the content of digital images, such as photographs and videos. The kind of room can be sorted mainly on the items that are present in it. You only look once  (YOLO) is a real-time object detection system that can precisely locate multiple objects in a single frame. It's incredibly fast, according to the official Yolo website, it's 1000x faster than R-CNN and 100x faster than Fast R-CNN.
In this project, we are mainly deciding the kind of room depending on the objects that are most commonly available in it. For instance, a user who is uploading the pictures on the website for a house sale/rent can just upload the pictures, the sorting of the images can be done by detecting the room. Also, it can be used for applications like Airbnb, the people who are uploading the pictures to rent a room can easily upload the pictures and the sorting can be done in the order we want to display on the website.

## Aim: The aim of the project is to identify the key objects in an image and detect the room

## Dataset:

The Dataset consists of 8 categories -- bed, oven, refrigerator, sink, couch, tv, microwave, dining table. 7 classes contains at least 1000 images and  1 class contains 600 
7600 images totally. The size of the data is 1.1GB.
All of the images are in jpeg format.
We have downloaded the data from various websites like open images and coco images datasets.
For the open images dataset, the downloaded images have XML extension documents we need to convert them into text documents.
Source: https://cocodataset.org/#explore
https://storage.googleapis.com/openimages/web/visualizer/index.html?set=train&type=detection&c=%2Fm%2F03dnzn
#### The link for the dataset which I have used are avaliable in the phase-3 under the section data. 
## Planned Framework: 
The overall framework of the scene recognition method is based on the YOLO algorithm.
The objects detected from YOLO are then passed into the rule inference engine which identifies the room. 

## Preparing Dataset:
In this project, I have used LabelImg open-source annotation tool to check the annotation of the image.
Annotations will be saved as XML files in the PASCAL VOC format, which ImageNet uses. Furthermore, it will be supporting the YOLO format.
We must make sure that annotations and images are in the same directory.
We will be generating the train, test, and validation text files with the help of the images.py file which I have given in my Github repository.
I have divided the data into 80%, 10%, and 10% for the training, testing, and validation sets.

## Configure/modify files and directory structure:
To train the YOLOv5 model you will need to perform some steps.
First, we will be starting with the cloning of the repository for YOLOv5. You can clone the repository from here. 
We will be modifying the YAML files to describe our dataset parameters. Please refer following YAML file and modify accordingly as per your need.

## Training:
To train the YOLO v5 model Glenn have proposed 4 versions:
1. yolov5-s which is a small version
2. yolov5-m which is a medium version
3. yolov5-l which is a large version
4. yolov5-x which is an extra-large version

While training I will be passing the YAML file to the above models.
Now everything is configured and we are ready to train our YOLOv5 model!
Move to the directory and use the following command to start training.

## !python train.py --img 640 --batch 16 --epochs 100 --data room.yaml --weights yolov5m.pt 
This command will start the model training immediately. I have decided to train the model for 100 epochs.
- img: size of the input image
- batch: batch size
- epochs: number of epochs
- data: YAML file which was created in step 3
- cfg: model selection YAML file. I have chosen “s” for this tutorial.
- weights: weights file to apply transfer learning, you can find them here.
- device: to select the training device, “0” for GPU, and “cpu” for CPU.

## Training Results for YOLO v5m and v5x models:
RuntimeError: CUDA out of memory. Tried to allocate 126.00 MiB (GPU 0; 14.76 GiB total capacity; 3.71 GiB already allocated; 80.75 MiB free; 3.90 GiB reserved in total by PyTorch) 
I am getting the above error for the v5m and v5x models. 
I will be using the google cloud platform or colab pro for better training of the model and for better results.
I was thinking of using the YOLOv3 since it will be using less complicated architecture
###### The above errors have taken place when we have used the google collab version and when have taken the the professional version we were able to process that 

## Modelling
- Used transfer learning to train the model. Pre-trained weights are publicly available, which are obtained from training  YOLOV5 model on MS-COCO dataset 
- Main inspiration to take COCO pre-trained weights is the COCO dataset consists of 80 general and household classes which overlapped with the key objects used to identity a room
- End layers are modified from 80 to 8 and have experimented with various variants of YOLOv5 (yolov5s, yolov5m, yolov5l and yolov5x) by tuning multiple parameters for the model to train on Colab as the computing power for training is limited.
- Developed an object detection system that can identify the 8 objects from images.
- The identified objects are then passed into a rule inference engine which returns the room.

 ## Problems faced
- Dataset diversity
- When the architecture's backbone is changed, it is hard to accomplish because pre-trained weights are not usable in this architecture.
-More GPUs are required to train the Coco data set on the newly created architecture.
- If I was able to complete what I was trying to achieve, the computation time will be probably half of what we are achieving, and the model will be much lighter.

## Future work
- With enough computation power, model with modified architecture can be trained. The computation time will significantly reduce the inference speed by half of what we are achieving right now, as the proposed model architecture is lighter.
- This can be extended to detect more rooms/objects to make it more robust.

