import numpy as np
import torch
import torchvision
from torchvision import transforms
from PIL import Image


# detect if host machine has CUDA GPU available
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

# load trained image classification model
print('Loading classifier...')
model = torch.load('./models/cat_dog.h5').to(device)

# image pre-processing steps
transform_image = transforms.Compose([
    transforms.Resize(255),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])


def load_and_predict(img_path):
    
    '''loads image from path and predicts its class'''

    im = Image.open(img_path)  # load image
    im = transform_image(im).unsqueeze(0)  # model expects [1, 3, 244, 244] image dimension
    im = im.to(device)  # put image onto device
    
    model.eval()
    output = model(im)
    pred = torch.argmax(output, dim=1)

    classes = {0:'cat', 1:'dog'}

    # return predicted class name
    return classes[pred.item()]
