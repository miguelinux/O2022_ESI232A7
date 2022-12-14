import cv2 as cv

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

while True:
    # Leemos la imagen de l camara
    ret, imagen = camara.read()

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break

    canny = cv.Canny(imagen, 50, 100)
    cv.imshow("Lineas", canny)

    # Al oprimir ESC salimos del programa
    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()
