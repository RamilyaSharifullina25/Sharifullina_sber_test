
import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
import io
from flask import Flask, redirect, request, render_template, jsonify

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

model = models.densenet121(pretrained=True)
model.eval()

def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    return y_hat

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        img_bytes = file.read()
        class_id, class_name = get_prediction(image_bytes=img_bytes)
        return jsonify({'class_id': class_id, 'class_name': class_name})

if __name__ == '__main__':
    app.run(debug=True)

