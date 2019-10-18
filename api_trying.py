from flask import Flask, request
from facial_landmarks import *


app = Flask(__name__)


@app.route("/", methods=['POST'])
def felcTespit():
    image = request.form.get('image')

    if not image:
        return json.dumps({"status": 'error', "message": "Image not found"})

    result = resim_analiz(image)
    return json.dumps(result) # durumun degerini json verisi olarak döndürür

if __name__ == "__main__":
    app.run(host="0.0.0.0")


