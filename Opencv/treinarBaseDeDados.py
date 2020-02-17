import cv2
import numpy as np
import os
import sys,time

def salvaFacesDetectadas(nome):
    face_cascade = cv2.CascadeClassifier('haars/haarcascade_frontalface_default.xml')
    camera = cv2.VideoCapture(0)
    framesObtidos=0

    framesDefinidos=int(input("Quantos frames você quer gravar na base de dados?\nrecomendado entre 300 e 1000 frames!\n"))

    while(framesObtidos<framesDefinidos+1):
        ret,img=camera.read()

        #frame não Obtido
        if(ret==False):
            print("Não foi possível acessar a câmera")
            return

        gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces= face_cascade.detectMultiScale(gray,1.3,5)

        #se nao achar continua..
        if not np.any(faces):
            continue

        for(x,y,w,h) in faces:
             imagemRosto = img[y:y+h, x:x+w]

        #imagem pequenas seráo descartadas
        larg,alt, _ = imagemRosto.shape
        if(larg*alt<=20*20):
            continue

        #salvando a imagem
        image_path = '\\'.join(['Banco-de-Faces',nome,nome+ str(framesObtidos) + '.png'])
        imagemRosto= cv2.resize(imagemRosto,(240,240))
        cv2.imwrite(image_path,imagemRosto)
        framesObtidos+=1
    cv2.destroyAllWindows()
    return

def criarPastaComNome(nome):
    try:
        os.mkdir("Banco-de-Faces/"+nome)
        return True
    except OSError:
        return False

def animation(nome):
    animation = "|/-\\"
    for i in range(30):
        time.sleep(0.1)
        sys.stdout.write("\r"+"Criando pasta"+animation[i%len(animation)])
        sys.stdout.flush()
    if(criarPastaComNome(nome)==True):
        print("\nPasta Criada!")
    else:
        print("\nA pasta já foi criada ;) ")

def pegarNomePessoa():
    return input("Escreva o nome da pessoa a ser analisada!\n")

# Função principal da aplicação!
def main():
    nome=pegarNomePessoa()
    animation(nome)
    time.sleep(0.5)
    salvaFacesDetectadas(nome)
    os.system('cls')
    print("base de dados cadastrada com sucesso!!")

if __name__=="__main__":
    main()
