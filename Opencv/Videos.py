import cv2
import numpy
from datetime import *
import os



#camera ou arquivo "arquivoVideo.mp4"
# print(camera.isOpened()) (MOSTRAR SE CONSEGUIU SE CONECTAR COM A CÂMERA!)
camera = cv2.VideoCapture(0) #camera vai ser default=0 , se tiver mais 1-2...

#mostram altura e largura do video nativo
# print(camera.get(3))
# print(camera.get(4))

camera.set(3,1280) #3=largura
camera.set(4,720)  #4=altura

#mostram altura e largura do video apos definirmos um tamanho
# print(camera.get(3))
# print(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

#devemos definir o tamanho da camera, na sua resolucao, para podermos gravar
#tamanhos diferentes da camera vai ocorrer erro na gravacao!

#como vai ser feita a gravacao:

#formato para gravacao
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#Se eu defini um tamanho pra minha camera minha gravacao nao pode ser diferente!
out = cv2.VideoWriter('Videos/nomeArquivo.avi',fourcc,20.0,(1280,720))

while(camera.isOpened()):
    fonte=cv2.FONT_ITALIC
    now=datetime.now()
    today=date.today()

    tamanhoByte=os.path.getsize('Videos/nomeArquivo.avi')
    tamanhoMegaByte=round(tamanhoByte/1000/1000,2)
    hora=now.strftime("%H:%M:%S")
    data=today.strftime("%d/%m/%Y")

    ret,frame = camera.read()

    if ret == True:
        cv2.putText(frame,"Data: "+data,(1030,70),fonte,0.7,(0,0,255))
        cv2.putText(frame,"Hora: "+hora,(1030,40),fonte,0.7,(0,0,255))
        cv2.putText(frame,"Tamanho(MB): "+str(tamanhoMegaByte),(1030,100),fonte,0.7,(0,0,255))

        cv2.imshow('frame',frame)

        #faz a gravacao, tem que estar no while pra ser continuo:
        out.write(frame)



        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
camera.release()
out.release()
cv2.destroyAllWindows()
