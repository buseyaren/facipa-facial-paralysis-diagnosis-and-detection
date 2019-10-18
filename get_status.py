import requests
import json

url="http://127.0.0.1:5000"   #sunucu url
r=requests.get(url)    #sayfa içeriğini r değişkenine at
durum=r.text   #r nin dondurdugu icerigi durum degiskenine at
print("Durum degeri: \t",durum)
durum=json.loads(durum)

print("durum['status'] degeri:\t",durum['status'])