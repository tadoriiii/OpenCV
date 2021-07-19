import numpy as np
import cv2
img_frame = cv2.imread("example.jpg")

height, width = img_frame.shape[:2]
# 이미지의 높이와 너비 불러옴, 가로 [0], 세로[1]
img_hsv = cv2.cvtColor(img_frame, cv2.COLOR_BGR2HSV)
# cvtColor 함수를 이용하여 hsv 색공간으로 변환
lower_Y = (30-20, 110, 130)
# hsv 이미지에서 바이너리 이미지로 생성 , 적당한 값 30
upper_Y = (30+20, 255, 255)
img_mask = cv2.inRange(img_hsv, lower_Y, upper_Y)
# 범위내의 픽셀들은 흰색, 나머지 검은색
# 바이너리 이미지를 마스크로 사용하여 원본이미지에서 범위값에 해당하는 영상부분을 획득
img_result = cv2.bitwise_and(img_frame, img_frame, mask = img_mask)
img = img_result
    # 이미지를 블러처리 합니다.
img_blur = cv2.blur(img,(5,5))
    # 그레이 스케일 이미지로 변환합니다.
img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)
    # 임계값 127을 사용하여 이진화를 합니다.
    # 이진화 타입으로 THRESH_BINARY를 사용하면 # 픽셀값이 127 보다 크면 255, 127 이하이면 0이 됩니다.
    # 이진화 타입으로 THRESH_BINARY_INV를 사용하면 반대로 됩니다.
retval, img_binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
blur2 = cv2.bilateralFilter(img_binary, 9, 75, 75)
img_src = blur2
img_edge = cv2.Canny(img_src, 150, 70)
img_line_res = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2BGR)
linesP = cv2.HoughLinesP(img_edge, 1, np.pi / 180, 50, None, 50, 5)

if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv2.line(img_line_res, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv2.LINE_AA)
            #theta 는 rad 단위
        theta = np.arctan((l[3]-l[1])/(l[2]-l[0]))
cv2.imshow('img_color', img_line_res)
cv2.waitKey(0)
cv2.destroyAllWindows()
