import cv2
import face_recognition 

img_org = cv2.imread(r'path_img')

rgb_org = cv2.cvtColor(img_org, cv2.COLOR_BGR2RGB)

wife_code = face_recognition.face_encodings(rgb_org)[0]
pass_wife = [wife_code]
class_img = cv2.imread(r'path_img')
class_img= cv2.resize(class_img,(1200,700))
class_rbg = cv2.cvtColor(class_img, cv2.COLOR_BGR2RGB)
face_position = face_recognition.face_locations(class_rbg)
face_passcode = face_recognition.face_encodings(class_rbg)

for (top,right,bottom,left),key in zip(face_position,face_passcode):
    
    diff = face_recognition.face_distance(pass_wife,key)
    thick = 2
    color = (218,247,166)
    font = cv2.FONT_ITALIC
    if(diff < 0.5):
        class_img = cv2.rectangle(class_img,(left,top),(right,bottom),color,thick)
        class_img = cv2.putText(class_img,'fiancee',(left-10,top-20),font,1,(255,0,0),2)
    else:
        class_img = cv2.rectangle(class_img,(left,top),(right,bottom),color,thick)
        class_img = cv2.putText(class_img,'??',(left-10,top-20),font,1,(255,0,0),2)
   
cv2.imshow('detect',class_img)
cv2.waitKey(0)
