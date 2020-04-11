import numpy as np
import io
import os
import torch
from PIL import Image
from torchvision import transforms
from app import app


# load trained image classification model
print('Loading classifier...')
model = torch.load(os.path.join(app.config['STATIC_DIR'], 'cat_dog.h5'))
model.eval()

classes = {0: 'Cat', 1: 'Dog'}


def transform_image(image_bytes):
    my_transforms = transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)


def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = y_hat.item()
    return classes[predicted_idx]
