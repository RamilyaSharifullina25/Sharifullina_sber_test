
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler
import cv2
import os
import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
import io
import numpy as np

classes = ['Australian terrier', 'Border terrier', 'Samoyed', 'Beagle', 'Shih-Tzu', 'English foxhound', 'Rhodesian ridgeback', 'Dingo', 'Golden retriever', 'Old English sheepdog']
model = models.resnet18()
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, len(classes))
model.load_state_dict(torch.load('resnet_20_epochs.pt', map_location='cpu'))
model.eval()

classes_dict = dict(zip(list(range(0,10)), classes))

def start(updater, context):
	updater.message.reply_text("Приветики, я бот для классификации картинок собак.")

def help_(updater, context):
	updater.message.reply_text("Просто отправь мне картинку, которую ты бы хотел протестить.")

def message(updater, context):
	msg = updater.message.text
	print(msg)
	updater.message.reply_text(msg)

def image(updater, context):
	photo = updater.message.photo[-1].get_file()
	photo.download("img.jpg")
	img = Image.open("img.jpg")
	my_transforms = transforms.Compose([transforms.CenterCrop(256), transforms.ToTensor(), transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
	tensor = my_transforms(img).unsqueeze(0)
	outputs = model(tensor)
	_, y_hat = outputs.max(1)
	pred = classes_dict[y_hat.item()]
	print(pred)

	updater.message.reply_text(pred)


updater = Updater('5587461965:AAEbygZIyquIamS4q8Z7OK5sqyBgLsEiZSs')
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help_))

dispatcher.add_handler(MessageHandler(Filters.text, message))

dispatcher.add_handler(MessageHandler(Filters.photo, image))


updater.start_polling()
updater.idle()
