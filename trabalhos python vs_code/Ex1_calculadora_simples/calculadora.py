while True:
    print("\n")
    print("-"*80)
    print("""                                                                       
    █▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ █▀▄ █▀█ █▀█ ▄▀█     █▀ █ █▀▄▀█ █▀█ █░░ █▀▀ █▀
    █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ █▄▀ █▄█ █▀▄ █▀█     ▄█ █ █░▀░█ █▀▀ █▄▄ ██▄ ▄█ 
    """)

    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    print("-"*80)
    
    print("\nPara começar forneça 2 numeros para calcular!")
    x = float(input("\nDigite o 1° numero: "))
    y = float(input("Digite o 2° numero: "))
    Operação = int(input("\nQual operação deseja executar?( 1 | 2 | 3 | 4 | 5): "))
    
    if Operação == 1:
        print("\nResultado:")
        print(float(x) + float(y))
            
    
    elif Operação == 2:
        print("\nResultado:")
        print(float(x) - float(y))
    
    elif Operação == 3:
        print("\nResultado:")
        print(float(x) * float(y))
    
    elif Operação == 4:
        if y != 0:
            print("\nResultado:")
            print(float(x) / float(y))
        else:
            print("\nErro: Divisão por zero!")
    elif Operação == 5:
        print("\nfinalizando app, até mais!")
        print("-"*80)
        break    
    else:
        print("\nErro: Opção invalida!")

    Finalizar = input("\nDeseja sair? ( s | n ): ")
    if Finalizar == "s":
        print("\nfinalizando app, até mais!")
        print("-"*80)
        break      
