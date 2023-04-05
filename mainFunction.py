from myDetectFunc import detect
from models.experimental import attempt_load
from utils.torch_utils import select_device

import time
"""
myDetecFunc'ta bir çok değişiklik var.
conf threshold ve iou thresholdları sabit tuttum. değiştirebilir. orj'ine detect.py dan bak
augment default false

nosave için save_img'yi False yapmak yeterli.


117. satırdaki text dosyasına yazdırılabilir.
s += f"{n} {names[int(c)]}, "
n number, c class name
"""

# t = time.process_time()

source = "C:/Users/gorke/Desktop/treePhotos"
# source = "0"
weights = "C:/Users/gorke/Desktop/YOLO/yolov7/runs/train/exp2/weights/best.pt"
view_img = False
save_txt = True
imgsz = 800
trace = False
save_img = True

model_load_time = time.process_time()
device = select_device('')
model = attempt_load(weights, map_location=device)  # load FP32 model
model_elapsed_time = time.process_time() - model_load_time
print("loading model took", model_elapsed_time, "seconds")

detect_time = time.process_time()
# detect(source, weights, view_img, save_txt, imgsz, trace, device, model, save_img)
detect_elapsed_time = time.process_time() - detect_time
print("detecting single image took", detect_elapsed_time, "seconds")

while True:
    print("wait with 0 enter with 1: ")
    user_input = str(input())
    if user_input == "0":
        print("NOTHING...")
    elif user_input == "1":
        print("Detecting new image...")
        detect(source, weights, view_img, save_txt, imgsz, trace, device, model, save_img)

# elapsed_time = time.process_time() - t
# print("function take seconds")
# print(elapsed_time)