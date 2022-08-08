from dynamikontrol_toolkit import Camera

camera = Camera()

while camera.is_opened():  #카메라가 열려있을 때 무한반복
    frame = camera.get_frame()

    face = camera.detect_face(frame)   # 얼굴 탐지

    if face:
        if face.is_located_left():
            print('left')
        elif face.is_located_right():
            print('right')


    camera.show(frame)  # 촬영한 것을 보여준다