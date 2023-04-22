import os
import socket
import time

def sendFile(packet):
    sizeOfPacket = bytearray(len(b).to_bytes(4, byteorder='big'))
    packet = sizeOfPacket + packet
    for lines in range(0, len(packet), bufferLen):
        packetPart = packet[lines:lines+bufferLen]
        sock.send(packetPart)
        print(f"part {lines} sent...")
        time.sleep(0.001/1000) # wait 1 us for the data to be sent
    print(f"file with size {len(packet)} sent to server")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = ("192.168.0.30", 1234)
sock.connect(serverAddress)
bufferLen = 65535

with open("Red_Apple.jpg", "rb") as image:
    f = image.read()
    b = bytearray(f)
    sendFile(b)

with open("output.txt", "wb") as file:
    file.write(f)

sock.close()

