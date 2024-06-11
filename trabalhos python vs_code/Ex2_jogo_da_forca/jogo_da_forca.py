import random
from palavras import lista_de_palavras


def escolher_palavra():
    palavra = random.choice(lista_de_palavras)
    return palavra.upper()


def jogar(palavra):
    estagios_palavra = "_" * len(palavra)
    advinhado = False
    letras_advinhadas = []
    palavras_advinhadas = []
    tentativas = 6
    print("""                                            
 ░░█ █▀█ █▀▀ █▀█    █▀▄ ▄▀█    █▀▀ █▀█ █▀█ █▀▀ ▄▀█
 █▄█ █▄█ █▄█ █▄█    █▄▀ █▀█    █▀░ █▄█ █▀▄ █▄▄ █▀█
""")
    print(estagios_forca(tentativas))
    print(estagios_palavra)
    print("\n")
    while not advinhado and tentativas > 0:
        chute = input("Advinhe uma letra ou palavra: ").upper()
        if len(chute) == 1 and chute.isalpha():
            if chute in letras_advinhadas:
                print("Você já chutou a letra", chute)
            elif chute not in palavra:
                print("Não existe", chute,"na palavra")
                tentativas -= 1
                letras_advinhadas.append(chute)
            else:
                print("Boa!", chute,"existe na palavra")
                letras_advinhadas.append(chute)
                palavra_em_lista = list(estagios_palavra)
                indices = [i for i, letter in enumerate(palavra) if letter == chute]
                for indice in indices:
                    palavra_em_lista[indice] = chute
                estagios_palavra = "".join(palavra_em_lista)
                if "_" not in estagios_palavra:
                    advinhado = True
        elif len(chute) == len(palavra) and chute.isalpha():
            if chute in palavras_advinhadas:
                print("Você já chutou a palavra", chute)
            elif chute != palavra:
                print(chute,"não é a palavra correta")
                tentativas -= 1
                palavras_advinhadas.append(chute)
            else:
                advinhado = True
                estagios_palavra = palavra
        else:
            print("Seu chute não é valido.")
        print(estagios_forca(tentativas))
        print(estagios_palavra)
        print("\n")
    if advinhado:
        print("Parabéns, você acertou a palavra, você venceu!")
    else:
        print("Acabou as tentativas. A palavra era " + palavra + ". mais sorte da próxima vez.")


def estagios_forca(tentativas):
    estagios = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return estagios[tentativas]


def main():
    palavra = escolher_palavra()
    jogar(palavra)
    while input("Jogar novamente? ( S | N )").upper() == "S":
        palavra = escolher_palavra()
        jogar(palavra)


if __name__ == "__main__":
    main()