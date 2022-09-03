from dynamikontrol_toolkit import Camera
from dynamikontrol import Module

camera = Camera()
module = Module()

angle = 0

while camera.is_opened():  #카메라가 열려있을 때 무한반복
    frame = camera.get_frame()
    face = camera.detect_face(frame)   # 얼굴 탐지

    if face:
        if face.is_located_left():
            angle = angle + 2   # 움직임을 부드럽게 해주기 위해서 
            module.motor.angle(angle)
        elif face.is_located_right():
            angle = angle - 2
            module.motor.angle(angle)


    camera.show(frame)  # 촬영한 것을 보여준다
