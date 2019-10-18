import facial_landmarks
import os
import time
shape_predictor="shape_predictor_68_face_landmarks.dat"
images = "/opt/lampp/htdocs/api/upload/images"
dataset = "/opt/lampp/htdocs/api/upload/images/dataset"


resim_konum = "/opt/lampp/htdocs/api/upload/images/yuz-teshis.jpg"

while(1):

    veri_sayisi = len(os.listdir(dataset))
    if(os.path.isfile(resim_konum)):
        durum = facial_landmarks.resim_analiz(resim_konum,shape_predictor)
        time.sleep(1) #Uyutma komutu
        os.popen('echo ' + '{ \"status\" :' + str(durum) + '} > ' + images + '/status.json')
        time.sleep(0.5)
        os.popen("mv " + resim_konum + " " + images+"/" + str(veri_sayisi+1) + ".jpg")
        time.sleep(0.5)
        os.popen("mv " + images + "/" + str(veri_sayisi+1) + ".jpg" + " " + dataset)
    else:
        print("Resim Bulunamadı")

