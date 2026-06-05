dias = ["segunda", "terça", "quarta", "quinta", "sexta"]
horarios = [8, 9, 10, 11, 12, 13, 14, 15]
agenda = [["LIVRE" for coluna in range(8)] for linha in range(5)]

def mostrar_agenda(agenda):
    print(f"\n              08h       09h       10h       11h       12h       13h       14h       15h")
    for dia in range(len(agenda)):
        print(f"{dias[dia]:>8}", end=" ")
        for hora in range(len(agenda[dia])):
            print(f"{agenda[dia][hora]:>9}", end=" ")
        print()

mostrar_agenda(agenda)