from pathlib import Path

import torch

from models.yolo import Model
from utils.general import check_requirements, set_logging
from utils.google_utils import attempt_download
from utils.torch_utils import select_device

model_path = "C:/Users/gorke/Desktop/YOLO/yolov7/runs/train/exp2/weights/best.pt"
dependencies = ['torch', 'yaml']
check_requirements(Path("/content/yolov7/").parent / 'requirements.txt', exclude=('pycocotools', 'thop'))
set_logging()

def custom(path_or_model=model_path, autoshape=True):
    """custom mode

    Arguments (3 options):
        path_or_model (str): 'path/to/model.pt'
        path_or_model (dict): torch.load('path/to/model.pt')
        path_or_model (nn.Module): torch.load('path/to/model.pt')['model']

    Returns:
        pytorch model
    """
    model = torch.load(path_or_model, map_location=torch.device(0)) if isinstance(path_or_model, str) else path_or_model  # load checkpoint
    if isinstance(model, dict):
        model = model['ema' if model.get('ema') else 'model']  # load model

    hub_model = Model(model.yaml).to(next(model.parameters()).device)  # create
    hub_model.load_state_dict(model.float().state_dict())  # load state_dict
    hub_model.names = model.names  # class names
    if autoshape:
        hub_model = hub_model.autoshape()  # for file/URI/PIL/cv2/np inputs and NMS
    device = select_device('0' if torch.cuda.is_available() else 'cpu')  # default to GPU if available
    return hub_model.to(device)

model = custom(path_or_model='yolov7.pt')  # custom example
# model = create(name='yolov7', pretrained=True, channels=3, classes=80, autoshape=True)  # pretrained example

# Verify inference
import numpy as np
from PIL import Image

imgsDir = "C:/Users/gorke/Desktop/treePhotos"


results = model(imgs)  # batched inference
results.print()
results.save()
df_prediction = results.pandas().xyxy
df_prediction