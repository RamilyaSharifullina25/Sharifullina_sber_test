import os
import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
import io
from flask import Flask, redirect, request, render_template, jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/uploads/')
ALLOWED_EXTENTIONS = {'png', 'jpg', 'jpeg'} 
MODEL_PATH = 'resnet_20_epochs.pt'
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

classes = ['Australian terrier', 'Border terrier', 'Samoyed', 'Beagle', 'Shih-Tzu', 'English foxhound', 'Rhodesian ridgeback', 'Dingo', 'Golden retriever', 'Old English sheepdog']
classes_dict = dict(zip(list(range(0,10)), classes))

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

def transform_image(image):
	my_transforms = transforms.Compose([transforms.CenterCrop(256),
                                transforms.ToTensor(),
                                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
                                ])
	img = Image.open(image).convert('RGB')
	return my_transforms(img).unsqueeze(0)

def get_prediction(image, model):
	tensor = transform_image(image=image)
	outputs = model(tensor)
	_, y_hat = outputs.max(1)
	return y_hat

#
model = models.resnet18(weights = True)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, len(classes))
model.load_state_dict(torch.load(MODEL_PATH, map_location='cpu'))
model.eval()

@app.route('/predict', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		f = request.files['file']
		file_path = os.path.join(app.config['UPLOAD_FOLDER'],  secure_filename(f.filename))
		f.save(file_path)
		output = get_prediction(file_path, model = model)
		result = classes_dict[output.item()]
		return result
	return None

if __name__ == '__main__':
    app.run(debug=True)

