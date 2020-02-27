import cv2
import uuid

cap = cv2.VideoCapture(0)

leido, frame = cap.read()

if leido == True:
	nombre_foto = str(uuid.uuid4()) + ".png"
	cv2.imwrite(nombre_foto, frame)
	print("Foto tomada correctamente con el nombre {}".format(nombre_foto))
else:
	print("Error al acceder a la cámara")

cap.release()