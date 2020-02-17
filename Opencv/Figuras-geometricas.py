import cv2
import numpy as np

#voce pode usar imagens criadas pelo numpy exemplo abaixo:

# imagem= np.zeros([700,700,3],np.uint8)
            #altura,largura.. datatype

imagem= cv2.imread('imagens/vitor-java.jpg',1)

imagem= cv2.line(imagem, (0,0), (255,255),(0,0,0),4)
imagem= cv2.arrowedLine(imagem, (0,255), (255,255),(255,0,0),4)
imagem = cv2.rectangle(imagem, (155,400), (285,580), (0,0,255),0)
imagem= cv2.circle(imagem, (400,350),100,(0,0,0),-1)
font= cv2.FONT_HERSHEY_COMPLEX_SMALL
imagem= cv2.putText(imagem,'OpenCv',(270,700),font, 4, (0,0,255),7,cv2.LINE_4)

cv2.imshow('imagens',imagem)
                                          #blue green red
cv2.waitKey(0)
cv2.destroyAllWindows()
