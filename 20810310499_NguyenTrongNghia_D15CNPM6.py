import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Load and blur image
img = cv.imread('SaltPeper.png')

"""Lọc trung bình là bộ lọc đơn giản nhất. Nó được xây dựng dựa trên ý tưởng
tính giá trị một điểm ảnh bằng trung bình cộng các điểm ảnh xung quanh nó.
Cách lọc này thường được áp dụng cho làm trơn ảnh vẫn muốn giữ lại biên không bị mờ."""

blur1 = cv.blur(img,(5,5)) # Dùng hàm cv.blur trong OpenCv để lọc trung bình

""" phép lọc trung vị, giá trị điểm trung tâm luôn được thay bằng một giá trị điểm ảnh trong bức ảnh đầu vào.
Do vậy, phương pháp lọc này có khả năng loại bỏ nhiễu muối tiêu (salt-and-pepper noise ) khá tốt."""

blur2 = cv.medianBlur(img,5)  # Dùng hàm cv.medianBlur trong OpenCv để lọc trung vị


img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
blur_rgb1 = cv.cvtColor(blur1, cv.COLOR_BGR2RGB)
blur_rgb2 = cv.cvtColor(blur2, cv.COLOR_BGR2RGB)

# Display
plt.subplot(221),plt.imshow(img_rgb),plt.title('Anh goc')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(blur_rgb1),plt.title('Loc trung binh')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(blur_rgb2),plt.title('Loc trung vi')
plt.xticks([]), plt.yticks([])

plt.show()