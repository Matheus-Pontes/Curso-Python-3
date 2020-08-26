#   MENU DE UMA LOJA

from time import sleep

valor1 = int(input(" Primeiro valor: "))
valor2 = int(input(" Segundo valor: "))
opçao = 0
maior = valor1

while opçao != 5:
    print('''\n[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    
    opçao = int(input("Informe sua opção: "))
    print('=-='*10)
    print("Calculando...")
    sleep(1)

    if opçao == 1:
        soma = valor1 + valor2
        print("A soma vale {}".format(soma))

    elif opçao == 2:
        mult = valor1 * valor2
        print("A multiplicação vale {}".format(mult))

    elif opçao == 3:
        if valor2 > valor1:
            maior = valor2
            print("O maior é {}".format(maior))

    elif opçao == 4:
        print("Informe novos números:")
        valor1 = int(input("Primeiro valor: "))
        valor2 = int(input("Segundo valor: "))

    elif opçao == 5:
        print("Finalizando ...")
        sleep(1)
    
    else: 
        print("[ERROR] Tente novamente.")
print("Fim do programa.Volte sempre !!!")
