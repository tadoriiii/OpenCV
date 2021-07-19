import cv2 as cv
img_ori = cv.imread("back.png")
img_gray = cv.cvtColor(img_ori,cv.COLOR_BGR2GRAY)

img_template=cv.imread('target.png',cv.IMREAD_GRAYSCALE)
w,h=img_template.shape[:2]

res=cv.matchTemplate(img_gray, img_template, cv.TM_CCOEFF)
min_val,max_val,min_loc,max_loc=cv.minMaxLoc(res)

top_left=max_loc
bottom_right=(top_left[0]+w,top_left[1]+h)
cv.rectangle(img_ori,top_left,bottom_right,(0,0,225),2)

cv.imshow("target",img_ori)
cv.waitKey(0)
cv.destroyAllWindows()
