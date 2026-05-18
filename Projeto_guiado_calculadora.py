def calculadora():
    while True:
        print("==== Calculadora Simples ====")
        print()
        print("Opção 1 : SOMA")
        print("Opção 2 : SUBTRAÇÃO")
        print("Opção 3 : MULTIPLICAÇÃO")
        print("Opção 4 : DIVISÃO")
        print("S : SAIR")

        operacao = input("Escolha uma opção ou aperte a tecla 'S' para sair: ")
        if operacao == "s" or operacao == "S":
            print("Obrigado por usara a Calculadora Simples")
            break

        if operacao not in ["1", "2","3","4"]:
            print("Operação inválida! Tente novamente ")
            continue

        numero_1 = float(input("Digite o primeiro número: "))
        numero_2 = float(input("Digite o segundo número: "))

        if operacao == "1":
            resultado = numero_1 + numero_2
            print("O resultado da SOMA é" , resultado)

        elif operacao == "2":
            resultado = numero_1 - numero_2
            print("O resultado da SUBTRAÇÃO é" , resultado)

        elif operacao == "3":
            resultado = numero_1 * numero_2
            print("O resultado da MULTIPLICAÇÃO é" , resultado)

        else:
            if numero_2 == 0:
                print("Divsões por zero são impossíveis, tente novamente")
                continue

            else:
                resultado = numero_1 / numero_2
                print("O resultado da DIVISÃO é", resultado)

calculadora()



