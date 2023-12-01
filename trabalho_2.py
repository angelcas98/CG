import cv2
import numpy as np
import matplotlib.pyplot as plt

# Função para carregar uma imagem em escala de cinza
def carregar_imagem(nome_arquivo):
    imagem = cv2.imread(nome_arquivo, cv2.IMREAD_GRAYSCALE)
    
    if imagem is None:
        print("Erro ao carregar a imagem.")
        exit(1)
    
    return imagem

# Função para salvar uma imagem em escala de cinza
def salvar_imagem(nome_arquivo, imagem):
    cv2.imwrite(nome_arquivo, imagem, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

# Função para aplicar o filtro de média
def aplicar_filtro_media(imagem_entrada, tamanho_kernel):
    altura, largura = imagem_entrada.shape
    imagem_saida = np.zeros_like(imagem_entrada)

    for i in range(altura):
        for j in range(largura):
            soma = 0
            contador = 0

            for m in range(-tamanho_kernel // 2, tamanho_kernel // 2 + 1):
                for n in range(-tamanho_kernel // 2, tamanho_kernel // 2 + 1):
                    linha = i + m
                    coluna = j + n

                    if 0 <= linha < altura and 0 <= coluna < largura:
                        soma += imagem_entrada[linha, coluna]
                        contador += 1

            imagem_saida[i, j] = soma // contador

    return imagem_saida

# Função para exibir uma imagem 
def mostrar_imagem(imagem, titulo):
    plt.imshow(imagem, cmap='gray')
    plt.title(titulo)
    plt.axis('off')
    plt.show()

def main():
    # Carregar imagem
    imagem_original = carregar_imagem("/home/angel/Área de Trabalho/trabalho2/gatopretogranulado.jpg")

    tamanho_kernel = 3

    # Aplicar filtro de média
    imagem_sem_ruido = aplicar_filtro_media(imagem_original, tamanho_kernel)

    # Salvar imagens em formato JPG
    salvar_imagem("imagem_original.png", imagem_original)
    salvar_imagem("imagem_sem_ruido.png", imagem_sem_ruido)


    mostrar_imagem(imagem_original, "Imagem Original")
    mostrar_imagem(imagem_sem_ruido, "Imagem Sem Ruído")

    print("Processo de remoção de ruído concluído.")


