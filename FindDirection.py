import cv2
import numpy as np

#이미지 read
img = cv2.imread("N.png")
img_copy = img.copy()

#전처리 과정(가우시안 블러, 양방향 필터)
img_copy = cv2.GaussianBlur(img_copy,(9,9),6)
img_copy = cv2.bilateralFilter(img_copy,300,75,75)

#회색조 처리 및 이진화(이진화값 기준은 0,0좌표값을 기준)
img_gray = cv2.cvtColor(img_copy, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(img_gray, 95, 255, cv2.THRESH_BINARY_INV)

#컨투어 검출
kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
img_binary=cv2.morphologyEx(binary,cv2.MORPH_CLOSE,kernel)

contours,hierarchy=cv2.findContours(img_binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img_copy,contours,0,(0,0,225),3)

#convexity defect 검출
for contour in contours:
    Hull=cv2.convexHull(contour,returnPoints=False)

    defects=cv2.convexityDefects(contour,Hull)
    if np.all(defects != None): #defects none값 에러를 방지하기 위한 조건문
        pointNum=0
        P=list()
        for i in range(defects.shape[0]):
            s,e,f,d=defects[i,0]
            start=tuple(contour[s][0])
            end=tuple(contour[e][0])
            far=tuple(contour[f][0])
            
            if d > 1000: #기준 거리값 설정
                cv2.circle(img_copy,far,5,(0,255,0),-1)
                P=P+list(far)
                pointNum=pointNum+1

        if pointNum == 1:
            print('E')
        elif pointNum == 3:
            print("W")
        elif pointNum == 2:
            x=(P[3]-P[1])/(P[2]-P[0])
            if x > 0:
                print("S")
            else:
                print("N")

        

#결과 출력
cv2_imshow(img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
