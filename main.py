dias = ["segunda", "terça", "quarta", "quinta", "sexta"]
horarios = [8, 9, 10, 11, 12, 13, 14, 15]
agenda = [["LIVRE" for coluna in range(8)] for linha in range(5)]

def valida_opcao(max, texto):
    opcao = input(texto)
    if not opcao.isdigit() or int(opcao) not in range(1,max +1):
        print(f"\nOpção invalida! Insira um numero de 1 a {max}! Tente novamente")
        return False
    return int(opcao)

def mostrar_agenda(agenda):
    print(f"\n              08h       09h       10h       11h       12h       13h       14h       15h")
    for dia in range(len(agenda)):
        print(f"{dias[dia]:>8}", end=" ")
        for hora in range(len(agenda[dia])):
            print(f"{agenda[dia][hora]:>9}", end=" ")
        print()
    input("\n                                  Aperte ENTER para voltar")

def mostar_menu():
    while True:
        print("\n ---------------------------- ")
        print("1. Mostrar agenda completa\n2. Consultar disponibilidade\n3. Fazer reserva\n4. Cancelar reserva\n5. Relatórios\n6. Sair")
        print(" ----------------------- ")
        n = valida_opcao(6, "Escolha uma opção (1-6): ")
        if not n:
            continue
        elif n == 1:
            mostrar_agenda(agenda)
        elif n == 2:
            print()
        elif n == 3:
            print()
        elif n == 4:
            print()
        elif n == 5:
            print()
        else:
            break

mostar_menu()