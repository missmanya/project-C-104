import cv2 
img=cv2.imread("solar-system.jpg")
print(img)
cv2.putText(img,
"sun",
(20,300),
 cv2.FONT_HERSHEY_COMPLEX,
 0.5,
 (255,255,255)
 )

cv2.putText(img,
"Mercury",
(120,190),
 cv2.FONT_HERSHEY_COMPLEX,
 0.5,
 (255,255,255)
 )

cv2.putText(img,
"Venus",
(200,260),
 cv2.FONT_HERSHEY_COMPLEX,
 0.5,
 (255,255,255)
 )

cv2.putText(img,
"Earth",
(290,260),
 cv2.FONT_HERSHEY_COMPLEX,
 0.5,
 (255,255,255)
 )

cv2.putText(img,
"Mars",
(380,250),
 cv2.FONT_HERSHEY_COMPLEX,
 0.5,
 (255,255,255)
 )

cv2.putText(img,
"Jupiter",
(580,100),
 cv2.FONT_HERSHEY_COMPLEX,
 0.5,
 (255,255,255)
 )

cv2.putText(img,
"Saturn",
(760,300),
 cv2.FONT_HERSHEY_COMPLEX,
 0.5,
 (255,255,255)
 )

cv2.putText(img,
"Uranus",
(980,300),
 cv2.FONT_HERSHEY_COMPLEX,
 0.5,
 (255,255,255)
 )

cv2.putText(img,
"Neptune",
(1110,300),
 cv2.FONT_HERSHEY_COMPLEX,
 0.5,
 (255,255,255)
 )


cv2.imshow("part1",img)
cv2.waitKey(0)