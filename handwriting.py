from tensorflow import keras
import tensorflow as tf
import numpy as np
import cv2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


IMG_PATH = "./test-images/File_009.jpeg"


def predict_letter(img):

    img_final = cv2.resize(img, (28, 28))

    img_final = np.reshape(img_final, (1, 28, 28, 1))

    img_pred = word_dict[np.argmax(new_model.predict(img_final))]
    return img_pred


kernel = np.ones((16, 16), dtype=np.float32)

new_model = tf.keras.models.load_model('./Models/model.h5')

word_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M',
             13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}


img = cv2.imread(IMG_PATH)
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grey_img = cv2.erode(grey_img, kernel, iterations=1)
ret, thresh = cv2.threshold(grey_img, 60, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh,
                                       cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.namedWindow('Contours', cv2.WINDOW_NORMAL)
cv2.imshow('Contours', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

words = []
pos = []
p = 0
for i, c in enumerate(contours):
    x, y, w, h = cv2.boundingRect(c)
    if cv2.contourArea(c) < 3000:
        continue

    pos.append((i, x, p))
    p += 1
    crop = thresh[y-50:y+h+50, x-50:x+w+50]
    words.append(predict_letter(crop))
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

sorted_pos = (sorted(pos, key=lambda x: x[1]))

correct_order_words = []
prev_x = 0

xdiff = [sorted_pos[n][1]-sorted_pos[n-1][1]
         for n in range(1, len(sorted_pos))]

sort_xdiff = sorted(xdiff)
if len(sort_xdiff) > 1:
    val = sum(sort_xdiff[(len(sort_xdiff)//2):]) / \
        len(sort_xdiff[len(sort_xdiff)//2:])


for p, i in enumerate(sorted_pos):
    _, x, loc = i
    if p != 0:
        dis = x - prev_x
        if dis > 400:
            correct_order_words.append(" ")
    correct_order_words.append(words[loc])
    prev_x = x

print(" ".join(correct_order_words))

img = cv2.putText(img, f"Predicted Text : {''.join(correct_order_words)}", (100, 150), cv2.FONT_HERSHEY_SIMPLEX,
                  5, (255, 0, 0), 4, cv2.LINE_AA)

cv2.imwrite(f"./results/{IMG_PATH.split('/')[-1]}", img)

cv2.namedWindow('Contours', cv2.WINDOW_NORMAL)
cv2.imshow('Contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
