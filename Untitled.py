import cv2
import numpy as np
# Создали переменные для ползунка
value = 1
value3 = 1
# Функция усиления RGB цветов


def max_rgb_filter(image):
    (B, G, R) = cv2.split(image)
    M = np.maximum(np.maximum(R, G), B)
    R[R < M] = 0
    G[G < M] = 0
    B[B < M] = 0
    return cv2.merge([B, G, R])


# Создали функцию для определения четных и нечетных чисел


def nothing(x):
    global value, value3
    print(x)
    value = x
    if x % 2 != 0:
        value3 = x


# Для trackbar создаем окно с иминем
cv2.namedWindow('main')
# Подключаем камеры
cap = cv2.VideoCapture(0)
# Создаем ползунок, максимальное значение в котором будет 300
cv2.createTrackbar('lower', 'main', 1, 300, nothing)
#img2 = cv2.imread('logo.jpg')
# При изменении значения ползунка выполняем преобразование изображения
while(1):
    cap.read()
    # Делаем снимок
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    frame = cv2.resize(frame, (80, 40))
    frame = cv2.resize(frame, (1200, 600))

    #gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # max = max_rgb_filter(frame)
    # cv2.imshow('max', max)
    # median = cv2.medianBlur(frame, value3)
    # blur = cv2.blur(frame, (value3, value3))
    #
    # cv2.imshow('median', median)
    # cv2.imshow('Blur', blur)
    #
    # #применение фильтра подавляющего шумы
    #denoised_gray = cv2.fastNlMeansDenoising(gray_image, None, value, value*2)
    #cv2.imshow('fastNlMeansDenoising', denoised_gray)
    ##
    #bilateralFilter = cv2.bilateralFilter(frame, value, value, value/2)
    #cv2.imshow('bilateralFilter', bilateralFilter)
    #
    # kernel = np.ones((value3, value3), np.uint8)
    # erosion = cv2.erode(frame, kernel, iterations=1)
    # cv2.imshow('erosion', erosion)
    #
    # dilation = cv2.dilate(frame, kernel, iterations=1)
    # cv2.imshow('dilation', dilation)
    #
    #gradient = cv2.morphologyEx(frame, cv2.MORPH_GRADIENT, kernel)
    # cv2.imshow('gradient', gradient)
    #
    _, threshold = cv2.threshold(frame, value, value*2, cv2.THRESH_TOZERO)
    _, threshold = cv2.threshold(frame, value, value*2, cv2.THRESH_BINARY_INV)
    _, threshold = cv2.threshold(frame, value, value*2, cv2.THRESH_BINARY)
    cv2.imshow('threshold', threshold)

    k = cv2.waitKey(1)
    if k == 27:   # выход по клавише Esc
        break

cv2.destroyAllWindows()