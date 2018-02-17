#imported required modules
from random import randint
import cv2
import sys
import os

#given path haarcascade algorith files for face detection
CASCADE = "haarcascade_frontalface_default.xml" and "haarcascade_frontalface_alt2.xml"
FACE_CASCADE = cv2.CascadeClassifier(CASCADE)
#read the image with cv module and image is converted in to gray scale
def detect_faces(image_path):
    image = cv2.imread(image_path)
    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#it detects the faces in an image
    faces = FACE_CASCADE.detectMultiScale(image_grey, scaleFactor=1.14,minNeighbors=5)
# faces are itterated and save in a .png format on the extracted folder
    for x, y, w, h in faces:
   #image ration is decreased by 10%
        sub_img = image[y-10:y+h+10,x-10:x + w+10]
        os.chdir("Extracted")
        #images are saved with different random numbers on the given range
        cv2.imwrite(str(randint(0, 10000)) + ".png", sub_img)
        os.chdir("../")
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
# it shows the faces found in an image
    cv2.imshow("Faces Found", image)
    #here we use keyword argument to close the output image by the q or Q button
    if (cv2.waitKey(0) & 0xFF == ord('q')) or (cv2.waitKey(0) & 0xFF == ord('Q')):
        cv2.destroyAllWindows()

if __name__ == "__main__":

    if not "Extracted" in os.listdir("."):
        os.mkdir("Extracted")

    if len(sys.argv) < 2:
        print ("Usage: python Detect_face.py 'image path'")
        sys.exit()

    detect_faces(sys.argv[1])
