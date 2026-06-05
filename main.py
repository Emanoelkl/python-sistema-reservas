dias = ["segunda", "terça", "quarta", "quinta", "sexta"]
horarios = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00']
agenda = [["LIVRE" for coluna in range(8)] for linha in range(5)]
historico = []

def valida_opcao(max, texto):
    opcao = input(texto)
    if not opcao.isdigit() or int(opcao) not in range(1,max +1):
        print(f"\nOpção invalida! Insira um numero de 1 a {max}! Tente novamente")
        return False
    return int(opcao)

def valida_confirmacao(texto):
    while True:
        opcao = input(texto).lower()
        if opcao not in ["s","n"]:
            print("\nResposta invalida! digite sim ou nao (S/N)")
        else:
            return opcao

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
    dia = dia - 1
    hora = hora - 1
    if agenda[dia][hora] == "LIVRE":
        print("\nA sala esta LIVRE!")
        return dia, hora, "LIVRE"
    else:
        print(f"\nA sala foi RESERVADA!\nResponsavel: {agenda[dia][hora].split("-")[0]}\nMotivo: {agenda[dia][hora].split("-")[1].strip()}")
        return dia, hora, "RESERVADO"

def reservar(agenda, historico):
    dia, hora, disp = consultar(agenda)
    if disp == "LIVRE":
        while True:
            nome = input("\nInsira o nome do responsavel (max 9 caracteres): ")
            if len(nome) > 9 or not nome:
                print("Nome invalido! maximo 9 caracteres e minimo 1")
            else:
                break
        motivo = input("Insira o motivo da reserva: ")
        reserva = nome + " - " + motivo
        agenda[dia][hora] = reserva
        print("\nReserva feita com sucesso!")
        historico.append(f"Reserva criada: {dias[dia]}, {horarios[hora]}, {reserva}")
    else:
        confirma = valida_confirmacao("\nDeseja escolher outra data? (S/N): ")
        if confirma == "s":
            reservar(agenda, historico)

def cancelar(agenda, historico):
    dia, hora, disp = consultar(agenda)
    if disp ==  "RESERVADO":
        confirma = valida_confirmacao("\nDeseja cancelar essa reserva? (S/N): ")
        if confirma == "s":
            historico.append(f"Reserva cancelada: {dias[dia]}, {horarios[hora]}, {agenda[dia][hora]}")
            agenda[dia][hora] = "LIVRE"
            print("\nReserva cancelada com sucesso!")
    else:
        print("Não há o que cancelar!")

def mostrar_historico(historico):
    if not historico:
        print("\nhistorico vazio!")
        return
    while True:
        n = valida_opcao(len(historico), f"\nInsira o numero de operações a serem exibidas (1-{len(historico)}): ")
        if not n:
            continue
        else:
            ultimos = historico[-n:]
            print("\n ----------------------------------")
            for i in ultimos:
                print(i)
            print(" --------------------------------------")
            break
def total(agenda):
    livre = 0
    reservado = 0
    for dia in range(len(agenda)):
        for hora in range(len(agenda[dia])):
            if agenda[dia][hora] == "LIVRE":
                livre += 1
            else:
                reservado += 1
    print(f"\nEssa semana {reservado} horarios ja estão reservados e {livre} estão livres")

def maior_dia(agenda):
    maior = [0, 0]
    for dia in range(len(agenda)):
        reservado = 0
        for hora in range(len(agenda[dia])):
            if agenda[dia][hora] != "LIVRE":
                reservado += 1
        if reservado > maior[0]:
            maior[0] = reservado
            maior[1] = dia
    if maior[0] > 0:
        print(f"\nO dia com mais reservas é {dias[maior[1]]}")
    else:
        print("\nNenhuma reserva encontrada")

def maior_hora(agenda):
    maior = [0, 0]
    for hora in range(len(agenda[0])):
        reservado = 0
        for dia in range(len(agenda)):
            if agenda[dia][hora] != "LIVRE":
                reservado += 1
        if reservado > maior[0]:
            maior[0] = reservado
            maior[1] = hora
    if maior[0] > 0:
        print(f"\nA hora com mais reservas é {horarios[maior[1]]}")
    else:
        print("\nNenhuma reserva encontrada")
    
def buscar_nome(agenda):
    busca = input("\nInsira o nome para busca: ")
    print()
    c = 0
    for dia in range(len(agenda)):
        for hora in range(len(agenda[dia])):
            nome = agenda[dia][hora].split("-")[0].strip()
            if nome == busca:
                c += 1
                print(f"{nome} tem reserva na {dias[dia]} as {horarios[hora]}")
    if c == 0:
        print("Nenhuma reserva com esse nome")

def resetar(agenda, historico):
    confirma = valida_confirmacao("\nTem certeza que quer resetar a agenda? (S/N): ")
    if confirma == "s":
        for dia in range(len(agenda)):
            for hora in range(len(agenda[dia])):
                agenda[dia][hora] = "LIVRE"
        print("\nAgenda resetada com sucesso!")
        historico.append("Agenda resetada")

def exportar(agenda):
    with open("agenda.txt", "w", encoding='utf-8') as arquivo:
        arquivo.write(f"             08:00     09:00     10:00     11:00     12:00     13:00     14:00     15:00\n")
        for dia in range(len(agenda)):
            arquivo.write(f"{dias[dia]:>8}")
            for hora in range(len(agenda[dia])):
                nome = agenda[dia][hora].split("-")[0].strip()
                arquivo.write(f"{nome:>10}")
            arquivo.write("\n")

def relatorios(agenda, historico):
    while True:
        print("\n -------- Relatórios -------- ")
        print("1. Total de horários livres e reservados na semana\n2. Dia com mais reservas\n3. Horário mais reservado\n4. Buscar reservas por nome\n5. Exibir Histórico\n6. Voltar ao Menu")
        print(" ----------------------- ")
        n = valida_opcao(6, "Escolha uma opção (1-6): ")
        if not n:
            continue
        elif n == 1:
            total(agenda)
        elif n == 2:
            maior_dia(agenda)
        elif n == 3:
            maior_hora(agenda)
        elif n == 4:
            buscar_nome(agenda)
        elif n == 5:
            mostrar_historico(historico)
        else:
            break

def mostar_menu():
    while True:
        print("\n ----------- Menu ----------- ")
        print("1. Mostrar agenda completa\n2. Consultar disponibilidade\n3. Fazer reserva\n4. Cancelar reserva\n5. Relatórios\n6. Resetar agenda\n7. Exportar agenda\n8. Sair")
        print(" ----------------------- ")
        n = valida_opcao(8, "Escolha uma opção (1-8): ")
        if not n:
            continue
        elif n == 1:
            mostrar_agenda(agenda)
        elif n == 2:
            consultar(agenda)
        elif n == 3:
            reservar(agenda, historico)
        elif n == 4:
            cancelar(agenda, historico)
        elif n == 5:
            relatorios(agenda, historico)
        elif n == 6:
            resetar(agenda, historico)
        elif n == 7:
            exportar(agenda)
        else:
            break

mostar_menu()