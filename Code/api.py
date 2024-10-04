from flask import Flask, request, jsonify,send_file
from werkzeug.utils import secure_filename
import os
import cv2
import helper
import base64
# import pandas as pd
from datetime import datetime

app = Flask(__name__)


DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S-%f"

model_args = helper.loadModelConfig()

@app.route("/predict", methods=["POST"])
def object_detection():
    image = request.files['img']
    filename = secure_filename(image.filename)

    # Save the image to a temporary location
    temp_path = os.path.join("../Data", filename)
    image.save(temp_path)
    res = helper.inference_image(temp_path,args=model_args)

    img_res='../Output/prediction/'+str(int(datetime.now().timestamp()))+'.png'
    cv2.imwrite(img_res,res)

    return send_file(img_res,mimetype='image/jpeg')



app.run(host="0.0.0.0", port=5000, debug=True)  # debug=True causes Restarting with stat