dias = ["segunda", "terça", "quarta", "quinta", "sexta"]
horarios = ['8', '9', '10', '11', '12', '13', '14', '15']
agenda = [["LIVRE" for coluna in range(8)] for linha in range(5)]

def valida_opcao(max, texto):
    opcao = input(texto)
    if not opcao.isdigit() or int(opcao) not in range(1,max +1):
        print(f"\nOpção invalida! Insira um numero de 1 a {max}! Tente novamente")
        return False
    return int(opcao)

def mostrar_agenda(agenda):
    print(f"\n             08:00     09:00     10:00     11:00     12:00     13:00     14:00     15:00")
    for dia in range(len(agenda)):
        print(f"{dias[dia]:>8}", end=" ")
        for hora in range(len(agenda[dia])):
            nome = agenda[dia][hora].split("-")[0].strip()
            print(f"{nome:>9}", end=" ")
        print()
    input("\n                                  Aperte ENTER para voltar")
    
def consultar(agenda):
    print("\nConsultando disponibilidade...")
    while True:
        print("\nInforme o Dia:\n ----------------------- ")
        print("1. Segunda   4. Quinta\n2. Terça     5. Sexta\n3. Quarta\n ----------------------- ")
        dia = valida_opcao(5, "Escolha uma opção (1-5): ")
        if not dia:
            continue
        else:
            break
    while True:
        print("\nInforme o Horario:\n ----------------------- ")
        print("1. 08:00    5. 12:00\n2. 09:00    6. 13:00\n3. 10:00    7. 14:00\n4. 11:00    8. 15:00\n ----------------------- ")
        hora = valida_opcao(8, "Escolha uma opção (1-8): ")
        if not hora:
            continue
        else:
            break
    if agenda[dia-1][hora-1] == "LIVRE":
        print("\nA sala esta LIVRE")
    else:
        print(f"\nA sala foi RESERVADA por: {agenda[dia-1][hora-1]}")
    return (dia-1,hora-1)

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
            consultar(agenda)
        elif n == 3:
            print()
        elif n == 4:
            print()
        elif n == 5:
            print()
        else:
            break

mostar_menu()