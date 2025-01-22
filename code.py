from xml.dom.minidom import Notation
import cv2
import face_recognition

img = cv2.imread(r"C:\Users\ThinkPad\Desktop\object\image\test.jpg")
img = cv2.resize(img,(400,300))
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
passcodeX = face_recognition.face_encodings(rgb_img)[0]

location = face_recognition.face_locations(rgb_img)

img2 = cv2.imread(r'C:\Users\ThinkPad\Desktop\object\image\wife.jpg')
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
passcodeY = face_recognition.face_encodings(rgb_img2)[0]

result = face_recognition.compare_faces([passcodeX],passcodeY)

id = location[0]
left = id[0]
top = id[1]
right = id[2]
bottom = id[3]
thick = 2
color = (0,128,0)
if (result == False):
    color = (255,0,255)
font = cv2.FONT_ITALIC
img = cv2.rectangle(img,(left,top),(right,bottom),color,thick)
img = cv2.putText(img,'GM',(left,bottom),font,1,(255,0,255),2)
cv2.imshow('test',img)
cv2.waitKey(0)



# type: ignore #tu