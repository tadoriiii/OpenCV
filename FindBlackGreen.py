import cv2
img_ori = cv2.imread("black_gray.png")
img_color = img_ori.copy()
img_color1 = img_ori.copy()
# 초록색 검출
img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)
lower_Y = (60-10, 30, 30)
upper_Y = (60+10, 255, 255)
img_mask = cv2.inRange(img_hsv, lower_Y, upper_Y)
img_green = cv2.bitwise_and(img_color, img_color, mask=img_mask)
height_g, width_g, depth_g = img_green.shape
cnt = 0
for i in range(0, height_g):
    for j in range(0, width_g):
        for k in range(0, depth_g):
            if img_green[i][j][k] != 0:
                cnt = cnt + 1
if cnt != 0:
    print("green")
    g = 1
else:
    print("not green")
    g=2

# 검정색 검출
img_gray = cv2.cvtColor(img_color1, cv2.COLOR_BGR2GRAY)
retval, img_black = cv2.threshold(img_gray, 20, 255, cv2.THRESH_BINARY)
height, width = img_black.shape
cntNonzero = cv2.countNonZero(img_black) #검은색이 아닌 픽셀 수 세기
size_img = height*width # img_black 의 전체 pixel 수
cnt_black = size_img - cntNonzero # 검은색 pixel 수 세기
if cnt_black >= size_img * 0.1: #검은 pixel이 전체 pixel의 10%이면 검정이라고 인식
    print("black")
    a = 1
else:
    print("no black")
    a = 2
cv2.imshow('orig',img_ori)
cv2.imshow('green',img_green)
cv2.imshow('black', img_black)
cv2.waitKey()
cv2.destroyAllWindows()

