from myDetectFunc import detect
from models.experimental import attempt_load
from utils.torch_utils import select_device
import socket
import os

import time
"""
nosave için save_img'yi False yapmak yeterli.

myDetecFunc'ta bir çok değişiklik var.
conf threshold ve iou thresholdları sabit tuttum. değiştirebilir. orj'ine detect.py dan bak
augment default false

117. satırdaki text dosyasına yazdırılabilir.
s += f"{n} {names[int(c)]}, "
n number, c class name
######################################
TODO:
*source değişkeni fotoğrafların koyulduğu klasör olacak, while loopta beklenecek, buraya yeni klasör eklendiği zaman (ya da interrupt geldiği zaman)
detect fonk. çalışacak, detect dosyalarını şu anlık 
"C:\\Users\\gorke\\Desktop\\YOLO\\yolov7\\runs\\hub" klasörüne kaydediliyor. bu yol detect fonk. içinden değiştirilebilir.

* txt dosyasındaki line sayısını da tcp den gönder
https://pynative.com/python-count-number-of-lines-in-file/
"""
def sendFile(packet):
    sizeOfPacket = bytearray(len(b).to_bytes(4, byteorder='big'))
    packet = sizeOfPacket + packet
    for lines in range(0, len(packet), bufferLen):
        packetPart = packet[lines:lines+bufferLen]
        sock.send(packetPart)
        time.sleep(0.001/1000) # wait 1 us for the data to be sent
    print(f"File with size {len(packet)} sent to server")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = ("192.168.0.30", 1234)
sock.connect(serverAddress)
bufferLen = 65535




#############################################
source = "C:/Users/gorke/Desktop/treePhotos/k_11200804_apples-on-branch.jpg"
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
    server_input = sock.recv(128)
    print(server_input)
    if server_input == b'bringMeNew':
        print("Detecting new image...")
        path = detect(source, weights, view_img, save_txt, imgsz, trace, device, model, save_img)
        path = "C:\\Users\\gorke\\Desktop\\YOLO\\yolov7\\" + path
        print(path)
        with open(path, "rb") as image:
            f = image.read()
            b = bytearray(f)
            sendFile(b)
    else:
        print("NOTHING...")

