import cv2
from src.gui.core.absolute_path import AbsolutePath


classificador = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
reconhecidor = cv2.face.LBPHFaceRecognizer_create()
reconhecidor.read(r'C:\Users\Daniel\Code\SalesManagement\src\gui\classifire_lbph\classificadorLBPH.1.0.1.yml')

font = cv2.FONT_HERSHEY_COMPLEX_SMALL
camera = cv2.VideoCapture("http://192.168.43.1:8080/video")
nome = ''
while True:
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetetadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.9, minNeighbors=3)

    for (x, y, l, a) in facesDetetadas:
        imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (100, 100))
        cv2.rectangle(imagem, (x, y), (x+l, y+a), (22, 22, 255), 2)
        # cv2.rectangle(imagem, (x, y), (x + l, y + a), (22, 22, 22), 1)
        id, confianca = reconhecidor.predict(imagemFace)

        if id == 0:
            nome = 'Desconhecido'
        if id == 1:
            nome = 'Daniel'
        if id == 2:
            nome = 'Wagner'
        if id == 3:
            nome = 'Oziel'

        print(id)

        cv2.putText(imagem, nome, (x, y + (a+30)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))

    cv2.imshow("Face", imagem)

    key = cv2.waitKey(3)

    if key == ord('c'):
        cv2.imwrite(f"pessoa.jpg", imagemFace)
        print(f"foto capturada com sucesso")

    if key == 27:
        break

camera.release()
cv2.destroyAllWindows()