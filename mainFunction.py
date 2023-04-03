from myDetectFunc import detect

"""
myDetecFunc'ta bir çok değişiklik var.
conf threshold ve iou thresholdları sabit tuttum. değiştirebilir. orj'ine detect.py dan bak
augment default false

nosave için save_img'yi False yapmak yeterli.


117. satırdaki text dosyasına yazdırılabilir.
s += f"{n} {names[int(c)]}, "
n number, c class name
"""

source = "C:/Users/gorke/Desktop/treePhotos"
weights = "C:/Users/gorke/Desktop/YOLO/yolov7/runs/train/exp2/weights/best.pt"
view_img = False
save_txt = True
imgsz = 1280
trace = False
save_img = True

detect(source, weights, view_img, save_txt, imgsz, trace, save_img);