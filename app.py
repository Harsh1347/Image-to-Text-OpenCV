import streamlit as st
from PIL import Image
import numpy as np
import cv2
import os
from helper import img2txt

st.set_page_config(layout='wide')

page = st.sidebar.selectbox(
    "Menu", ['Home', 'Methodology', 'Model', 'Results', 'Limitations'])

st.title("Image to Text Using OpenCV and Alphabet Recognition")
_, _, made = st.beta_columns([2, 2, 1])
made.markdown("Made by [Harsh Gupta](https://github.com/Harsh1347/)")


if page == 'Home':

    st.write("The program uses OpenCV to identify the position of letters in the image and using a CNN Model predicts the letter. These predicted letters are combined to form words and sentences.")

    st.info("""
    The model currently only supports single line texts. \n\n
    Letters and words should be properly spaced. For reference check the results section.
    """)

    img_file_buffer = st.file_uploader("Upload the image here.")

    if img_file_buffer is not None:
        image = Image.open(img_file_buffer)
        img_array = np.array(image)
        img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
        pred_word, himg = img2txt(img_array)
        st.write(f"Predicted: {pred_word}")
        st.image(
            himg,
            use_column_width=True,
        )


if page == 'Methodology':
    st.header(page)
    st.markdown("""
    The flow is as follow:
    - The image is eroded to join the possible discontinuity while writing the letters. This makes sure that the letters are identified as a whole. The image below shows an example for the same.
    """)
    st.image(os.path.join("./results/", "split.png"))
    st.markdown("""
    - Corresponding bounding box for each contour is found. Based on this, image is cropped for each contour, resized to 28x28 and fed to the ML model. We need to ignore smaller contour which might be due to noise therefore a simple filter is added. This filter checks for the area of contour and if it is less than threshold area, it is ignored.

    - The predicted letter by model is saved as well as the x coordinate is stored. Location is saved to arrange the letters as contours can be found in any order. Once all the letters are predicted, they are sorted in the ascending order of x coordinate.

    - The distance between each consecutive letter is found and average distance between each letter is calculated. If the distance between two letters is more than 1.25 times the average the distance, a space is added between the letters. This is how the beginning of new word is identified.

    - Finally all the arranged words along with spaces are joined together to return the final input.

        """)
if page == 'Model':
    st.header(page)
    st.markdown("""
    CNN model was trained on A-Z Dataset. The model takes an image of size 28x28 and predicts the output as 0 - 25, each corresponding to one of the 26 alphabets.
    The Models folder  contains 5 different models. Each saved model has been trained on different number of training images and therefore performance varies from model to model.
The model specifications are mentioned below
    """)
    st.image(
        os.path.join("./results/", "model.png"))
if page == 'Results':
    res = st.sidebar.radio("Select", ["Single Letter",
                                      "Single Word", "Multiple Words", "Sentence"])
    st.header(f"{page} for {res}")

    if res == "Single Letter":
        st.image(os.path.join("./results/", "File_005.jpeg"))
        st.image(os.path.join("./results/", "File_006.jpeg"))

    if res == "Single Word":
        st.image(os.path.join("./results/", "File_002.jpeg"))
        st.image(os.path.join("./results/", "File_010.jpg"))

    if res == "Multiple Words":
        st.image(os.path.join("./results/", "File_007.jpeg"))
        st.image(os.path.join("./results/", "File_009.jpeg"))
        st.image(os.path.join("./results/", "File_000.jpeg"))
        st.image(os.path.join("./results/", "File_001.jpeg"))

    if res == "Sentence":
        st.image(os.path.join("./results/", "File_003.jpeg"))
        st.image(os.path.join("./results/", "File_004.jpeg"))


if page == 'Limitations':
    st.header(page)

    st.markdown("""
    - Only single line text can be detected.
    - Letters should not be connected and must be properly spaced.
    - ML model doesn't recognize any numbers or any special characters.

    The image below shows some of the limitations.    
        """)
    st.image(os.path.join("./results/", "File_008.jpg"))

    st.markdown("""
    - Spacing between the words is not enough.
    - Because of discontinuity while writing the letter, one character is being treated as two.
        """)


st.sidebar.markdown(
    ":arrow_right: [Github Project Link](https://github.com/Harsh1347/Image-to-Text-OpenCV)")
