**FaCiPa: YÜZ FELCİ TEŞHİS ALGORİTMASI (Facial_landmarks 68 coordinates)**

**Uygulamanın Çalıştırılması**
---------------

Python kodlarının çalıştırılabilmesi için PyCharm IDE'sinde kullanılan versiyonlar aşağıda belirtilmiştir.

***Öncelikli Kurulması Gereken Kütüphane ve Paketler***

👉 Pip Package Manager

👉 Python 3.5 version

👉 Gerek duyulursa Flask


✔️ Python version:3.5

✔️ pip:19.1.1

✔️ flask:1.1.1

✔️ cmake:3.15.3

✔️ dlib:19.4.0 || latest version( 19.18.0 )

✔️ opencv-python:4.1.1.26

✔️ imutils:0.5.3

   Projede 68 tane koordinat modeli baz alınarak yüz felci algoritması çalıştırılmaktadır. Algoritmanın ve shape-predictor modelinin yer aldığı kod dosyası facial_landmarks.py, projenin mobil platformda çalışılması için yazılan Flask API kodu ise api_trying.py dosyasında yer almaktadır.
    
   Eğer yalnızca felç algoritması çalıştırılacaksa dosya içerisinde baz alınan imageP değişkeni üzerinden tespit edilmek istenen fotoğraf manuel olarak belirtilmelidir. 
    
    > python facial_landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat \--image face.jpg
    
   Sunucu bazlı çalışılacaksa api_trying dosyasının Run edilmesi yeterlidir.
    
    > python api_trying.py
   
**Pip Kurulumu**

Ubuntu 16.04 PIP Kurulumu

https://www.rosehosting.com/blog/how-to-install-pip-on-ubuntu-16-04/
