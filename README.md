# Image to Text Using OpenCV and Alphabet Recognition
The program uses OpenCV to identify the position of letters in the image and using a CNN Model predicts the letter. These predicted letters are combined to form words and sentences.

## Methodology
The flow is as follow:
- The image is eroded to join the possible discontinuity while writing the letters. This makes sure that the letters are identified as a whole. The image below shows an example for the same.
![discontinuity](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/split.png)

- Corresponding bounding box for each contour is found. Based on this, image is cropped for each contour, resized to 28x28 and fed to the ML model. We need to ignore smaller contour which might be due to noise therefore a simple filter is added. This filter checks for the area of contour and if it is less than threshold area, it is ignored.

- The predicted letter by model is saved as well as the x coordinate is stored. Location is saved to arrange the letters as contours can be found in any order. Once all the letters are predicted, they are sorted in the ascending order of x coordinate.

- The distance between each consecutive letter is found and average distance between each letter is calculated. If the distance between two letters is more than 1.25 times the average the distance, a space is added between the letters. This is how the beginning of new word is identified.

- Finally all the arranged words along with spaces are joined together to return the final input.

## Model

## Results
Here are some of the results on:

- **Single Letter**
![B](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/File_005.jpeg)
![G](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/File_006.jpeg)

- **Single Word**
![MOUSE](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/File_002.jpeg)

- **Multiple Words**
![BLUE PEN](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/File_007.jpeg)
![BLUE BRICKS](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/File_000.jpeg)
![PRAVIN KUMAR](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/File_001.jpeg)

- **Sentence**
![I AM WORKING TODAY](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/File_003.jpeg)
![THIS IS TESTING IMAGE](https://github.com/Harsh1347/Image-to-Text-OpenCV/blob/main/results/File_004.jpeg)

## Limitations