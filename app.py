import os
import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
import io
from flask import Flask, redirect, request, render_template, jsonify
from werkzeug.utils import secure_filename

MODEL_PATH = 'resnet_pretrained.pt'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

def transform_image(image_bytes):
    my_transforms = transforms.Compose([transforms.Resize(255),
					transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)

model = models.resnet18(weights = True)
model.eval()

def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model(tensor)
    _, y_hat = outputs.max(1)
    return y_hat

@app.route('/predict', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		f = request.files['file']
		basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        out = transform_image(file_path)
        return str(out)
	return None 


if __name__ == '__main__':
    app.run(debug=True)

