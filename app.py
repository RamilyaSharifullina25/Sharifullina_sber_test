import os
import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
import io
from flask import Flask, redirect, request, render_template, jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENTIONS = {'png', 'jpg', 'jpeg'} 
MODEL_PATH = 'resnet_pretrained.pt'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

def transform_image(image):
    my_transforms = transforms.Compose([transforms.Resize(255),
					transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    img = Image.open(io.BytesIO(image))
    return my_transforms(img).unsqueeze(0)

def get_prediction(image, model):
    tensor = transform_image(image=image)
    outputs = model(tensor)
    _, y_hat = outputs.max(1)
    return y_hat

resnet = models.resnet18(weights = True)
resnet.eval()

@app.route('/predict', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		f = request.files['file']
		file_path = os.path.join(os.path.dirname(__file__), 'uploads' , secure_filename(f.filename))
		f.save(file_path)
		result = get_prediction(file_path, model = resnet)
		return result
	return None

if __name__ == '__main__':
    app.run(debug=True)

