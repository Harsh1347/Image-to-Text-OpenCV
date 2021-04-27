# Image to Text Using OpenCV and Alphabet Recognition 
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/harsh1347/image-to-text-opencv/main/app.py)
The program uses OpenCV to identify the position of letters in the image and using a CNN Model predicts the letter. These predicted letters are combined to form words and sentences.

#### Link to web-app https://share.streamlit.io/harsh1347/image-to-text-opencv/main/app.py


## Methodology
The flow is as follow:
- The image is eroded to join the possible discontinuity while writing the letters. This makes sure that the letters are identified as a whole. The image below shows an example for the same.

![discontinuity](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/split.png)

- Corresponding bounding box for each contour is found. Based on this, image is cropped for each contour, resized to 28x28 and fed to the ML model. We need to ignore smaller contour which might be due to noise therefore a simple filter is added. This filter checks for the area of contour and if it is less than threshold area, it is ignored.

- The predicted letter by model is saved as well as the x coordinate is stored. Location is saved to arrange the letters as contours can be found in any order. Once all the letters are predicted, they are sorted in the ascending order of x coordinate.

- The distance between each consecutive letter is found and average distance between each letter is calculated. If the distance between two letters is more than 1.25 times the average the distance, a space is added between the letters. This is how the beginning of new word is identified.

- Finally all the arranged words along with spaces are joined together to return the final input.

## Model
CNN model was trained on A-Z Dataset. The model takes an image of size 28x28 and predicts the output as 0 - 25, each corresponding to one of the 26 alphabets.
The model specifications are mentioned below 

![Model](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/model.png)

The Models folder  contains 5 different models. Each saved model has been trained on different number of training images and therefore performance varies from model to model. *Model_3* performs the best on the given test data.

## Results
Here are some of the results on:

- **Single Letter**

![B](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/File_005.jpeg)

![G](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/File_006.jpeg)

- **Single Word**

![MOUSE](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/File_002.jpeg)

![PORTABLE](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/File_010.jpg)

- **Multiple Words**

![BLUE PEN](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/File_007.jpeg)

![ASUS LAPTOP](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/File_009.jpeg)

![BLUE BRICKS](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/File_000.jpeg)

![PRAVIN KUMAR](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/File_001.jpeg)

- **Sentence**

![I AM WORKING TODAY](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/File_003.jpeg)


![THIS IS TESTING IMAGE](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/File_004.jpeg)

## Limitations

- Only single line text can be detected.
- Letters should not be connected and must be properly spaced.
- ML model doesn't recognize any numbers or any special characters.

The image below shows some of the limitations.

![THIS IS TESTING IMAGE](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/File_008.jpg)

- Spacing between the words is not enough.
- Because of discontinuity while writing the letter, one character is being treated as two.
