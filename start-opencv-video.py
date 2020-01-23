import cv2
import numpy

#camera ou arquivo ".... .mp4"
#0-1-2, o 0 é a câmera default

# print(camera.isOpened()) (MOSTRAR SE CONSEGUIU SE CONECTAR COM A CÂMERA!)
camera = cv2.VideoCapture(0)
camera.set(3,1280) #3=largura
camera.set(4,720)  #4=altura
#devemos definir o tamanho da camera, na sua resolucao, para podermos gravar
#tamanhos diferentes da camera vai ocorrer erro na gravacao!

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('nomeArquivo.avi',fourcc,30,(1280,720))

while(camera.isOpened()):
    ret,frame = camera.read()
    if ret == True:
        # print(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        # print(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
camera.release()
out.release()
cv2.destroyAllWindows()
