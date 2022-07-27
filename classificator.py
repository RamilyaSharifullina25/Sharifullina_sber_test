# import tarfile
# import os
import torch 
import torch.nn as nn
from torchvision import models

## Data extraction
# данные модель принимает из датасета imagewoof2, папка val
# file = tarfile.open('imagewoof2.tgz')
# file.extractall('./val')
# file.close()

# Define arguments
classes = ['Australian terrier', 'Border terrier', 'Samoyed', 'Beagle', 'Shih-Tzu', 'English foxhound', 'Rhodesian ridgeback', 'Dingo', 'Golden retriever', 'Old English sheepdog']

# Define the model and extract it's saving
model = models.resnet18(weights = True)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, len(classes))
model.load_state_dict(torch.load('resnet_pretrained.pt', map_location=torch.device('cpu')))
model.eval()