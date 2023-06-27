import cv2 # Open CV
import mediapipe as mp 

# Iniciando OpenCV e Mediapipe

webcam = cv2.VideoCapture(0)

solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_de_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    # Ler as informações da webcam
    verificador, frame = webcam.read()
    
    if not verificador:
        break

    # Reconhecer os rostos ali dentro
    lista_rostos = reconhecedor_de_rostos.process(frame)
    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            # Desenhar rostos na imagem
            desenho.draw_detection(frame, rosto)

    cv2.imshow("Rostos na Webcam", frame)
    # Quando apertar esc para o Loop
    if cv2.waitKey(5) == 27: # 27 é o numero do teclado referente ao  botão ESC
        break

webcam.release()
