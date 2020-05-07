from collections import OrderedDict
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
import json

#costruct the argument parser and parse tha arguments
#ap=argparse.ArgumentParser()
#ap.add_argument("-p","--shape-predictor", required=True,
 #                   help="path to facial landmark predictor")
#ap.add_argument("-i", "--image", required=True,
#                    help="path to input image")
#args=vars(ap.parse_args())
#shape_predictor = args["shape_predictor"]
#imageP = args["image"]
imageP = "face.jpg"
shape_predictor="shape_predictor_68_face_landmarks.dat"

FACIAL_LANDMARKS_IDXS = OrderedDict([
	("mouth", (48, 68)),
	("right_eyebrow", (17, 22)),
	("left_eyebrow", (22, 27)),
	("right_eye", (36, 42)),
	("left_eye", (42, 48)),
	("nose", (27, 36)),
	("jaw", (0, 17))
])

def rect_to_bb(rect):
        # take a bounding predicted by dlib and convert it
        # to the format (x, y, w, h) as we would normally do
        # with OpenCV
        x = rect.left()
        y = rect.top()
        w = rect.right() - x
        h = rect.bottom() - y
        # return a tuple of (x, y, w, h)
        return (x, y, w, h)



def shape_to_np(shape, dtype="int"):
	coords = np.zeros((68, 2), dtype=dtype)
	for i in range(0, 68):
		coords[i] = (shape.part(i).x, shape.part(i).y)
	# return the list of (x, y)-coordinates
	return coords

def resim_analiz(imageP, shape_predictor):

    #initialize dlib's face detector(HoG-based) and then create
    #the facial landmarks predictor
    sayac = 0 #nokta sayısı
    sum=0 #kayma olan bölge sayısı


    durum = dict()
    durum["status"] = False # status=False

    corarray=[]
    detector=dlib.get_frontal_face_detector()
    predictor=dlib.shape_predictor(shape_predictor)

    #load the input image, redize it, and convet it grayscale
    image=cv2.imread(imageP)
    image=imutils.resize(image, width=500)
    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #detect faces in the grayscale image
    rects=detector(gray,1)

    #loop over the face detections
    for(i, rect) in enumerate(rects):
        print(rects)
        #determine the facial landmarks for the face region, then
        #convert the facial landmarks(x,y)-coordinates to a Numpy
        #array
        shape=predictor(gray,rect)
        shape=face_utils.shape_to_np(shape)

        #convert slib's rectangle to a OpenCv-style bounding box
        #[i.e., (x,y,w,h)] then draw the face bounding box
        (x,y,w,h)=face_utils.rect_to_bb(rect)
        cv2.rectangle(image, (x,y),(x+w,y+h), (0,255,0),2)
        #show the face number
        cv2.putText(image, "Face #{}".format(i+1),(x-10, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
        #loop over the(x,y)-cordinates for the facial landmarks
        #and draw them on the image
        for (x,y) in shape:

            corarray.append(y)
            print(sayac,x,y)
            sayac = sayac + 1
            cv2.circle(image,(x,y),3,(0,255,0),-1)

    #show the output image with the face detections+facial labdmarks
    eyebrowri=corarray[21] #22.noktanın y değeri
    eyebrowrj=corarray[17] #18.noktanın y değeri
    eyebrowli=corarray[22] #23.noktanın y değeri
    eyebrowlj=corarray[26] #27.noktanın y değeri
    farkeyebrowi=abs(eyebrowri-eyebrowli) #kaş kayma miktari(i)
    farkeyebrowj=abs(eyebrowrj-eyebrowlj) #kaş kayma miktari(j)
    print(eyebrowri, eyebrowrj, eyebrowli, eyebrowlj, farkeyebrowi, farkeyebrowj)

    eyeri=corarray[39] #40.noktanın y değeri
    eyerj=corarray[36] #37.noktanın y değeri
    eyeli=corarray[42] #43.noktanın y değeri
    eyelj=corarray[45] #46.noktanın y değeri
    farkeyei=abs(eyeri-eyeli) #göz kayma miktari(i)
    farkeyej=abs(eyerj-eyelj) #göz kayma miktari(j)
    print(eyeri, eyerj, eyeli, eyelj, farkeyei, farkeyej)

    noser=corarray[31] #32.noktanın y değeri
    nosel=corarray[35] #36.noktanın y değeri
    farknose=abs(nosel-noser) #burun kayma miktari(i)
    print(noser, nosel, farknose)
    lipr=corarray[48] #49.noktanın y değeri
    lipl=corarray[54] #55.noktanın y değeri
    farklip=abs(lipl-lipr) #burun kayma miktari(i)
    print(lipr, lipl, farklip)

    if (farkeyebrowi >= 15):
        sum = sum + 1
    if (farkeyebrowj):
        sum = sum + 1
    if (farkeyei >= 15):
        sum = sum + 1
    if (farkeyebrowj >= 15):
        sum = sum + 1
    if (farknose >= 13):
        sum = sum + 1
    if (farklip >= 10):
        sum = sum + 1
    if (sum >= 2):
        durum["status"] = True

    print("Felç Durumu: ", durum["status"])

    cv2.imshow("Output",image)
    cv2.waitKey(0)
    return durum


if __name__ == "__main__":
    durum = resim_analiz(imageP, shape_predictor)
    with open("durum.json", "w") as f:
        json.dump(durum, f)