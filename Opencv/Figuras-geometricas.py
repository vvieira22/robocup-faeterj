import cv2
import numpy

imagem= cv2.imread('imagens/vitor-java.jpg',1)

imagem= cv2.line(imagem, (0,0), (255,255),(0,0,0),4)
imagem= cv2.arrowedLine(imagem, (0,255), (255,255),(255,0,0),4)
imagem = cv2.rectangle(imagem, (155,400), (285,580), (0,0,255),0)
imagem= cv2.circle(imagem, (400,350),100,(0,0,0),-1)
font= cv2.FONT_HERSHEY_COMPLEX_SMALL
imagem= cv2.putText(imagem,'OpenCv',(10,700),font, 4, (255,255,255),10,cv2.LINE_4)

cv2.imshow('imagens',imagem)
                                          #blue green red
cv2.waitKey(0)
