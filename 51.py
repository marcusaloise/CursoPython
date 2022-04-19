# estudando try
# não realiza o stop no programa 
# mensagem customizada quando encontra um erro

from traceback import print_tb


try:
    letras = ["a", "b", "c"]
    print(letras[3])
except IndexError:
    print("O index não existe")
    