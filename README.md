# Sistema de Reservas de Sala: Agenda Semanal

Contexto

Você foi contratado para desenvolver um sistema em Python para gerenciar reservas de uma sala (laboratório/auditório) ao longo de uma semana. O sistema deve permitir cadastrar reservas, consultar disponibilidade, cancelar, e gerar relatórios.
Requisitos obrigatórios (o que deve aparecer no código)

Você deve utilizar:

    funções (obrigatório)
    listas
    matriz (lista de listas) para representar a agenda semanal
    estruturas condicionais (if/elif/else)
    estruturas de repetição (while e for)

    Não é permitido usar bibliotecas externas.
    O programa deve rodar em terminal (console) com input() e print().

Modelagem da Agenda (matriz)

A agenda será uma matriz 5x8:

    5 dias úteis: Seg, Ter, Qua, Qui, Sex
    8 horários: 08, 09, 10, 11, 12, 13, 14, 15 (ou outro bloco definido por você e documentado)

Cada posição da matriz deve guardar:

    "LIVRE" quando estiver disponível, ou
    o nome do responsável pela reserva (ex.: "Ana") ou um texto com mais detalhes (ex.: "Ana - Reunião")

Funcionalidades (menu)

O sistema deve exibir um menu em loop até o usuário sair:

    Mostrar agenda completa
    Consultar disponibilidade (dia e horário)
    Fazer reserva
    Cancelar reserva
    Relatórios
    Sair

Regras de negócio (obrigatórias)

1. Mostrar agenda completa

   Exibir a matriz formatada (linhas = dias, colunas = horários).
   Deve ser legível (com cabeçalho dos horários).

2. Consultar disponibilidade

   Usuário informa dia e horário
   O sistema informa se está LIVRE ou RESERVADO e por quem.

3. Fazer reserva

Entradas mínimas:

    dia (1 a 5)
    horário (1 a 8)
    nome do responsável (texto)
    motivo da reserva (texto simples)

Validações:

    dia/horário devem ser válidos
    não permitir nome vazio
    se já estiver reservado, não sobrescrever: avisar e voltar ao menu

Registro:

    preencher a célula com "Nome - Motivo" (ou estrutura equivalente)

4. Cancelar reserva

   Usuário informa dia e horário
   Se estiver LIVRE, avisar que não há o que cancelar
   Se estiver reservada, pedir confirmação (S/N) e então marcar como "LIVRE"

5. Relatórios

O menu de relatórios deve conter:

a) Total de horários livres e reservados na semana
b) Dia com mais reservas
c) Horário mais reservado (considerando todos os dias)
d) Buscar reservas por nome (mostrar todas as ocorrências)

    Aqui é obrigatório percorrer a matriz com for e fazer contagens/comparações.

Histórico de operações (listas)

Além da matriz, o sistema deve manter um histórico em uma lista, registrando ações como:

    “Reserva criada: Dia X, Horário Y, Nome…”
    “Reserva cancelada: Dia X, Horário Y…”

Ao final (ou em uma opção extra), permitir exibir as últimas N operações.
Funções obrigatórias (mínimo)

Seu código deve ter, no mínimo, as seguintes funções (podem ter outros nomes, mas devem existir):

    mostrar_menu()
    mostrar_agenda(agenda)
    consultar(agenda)
    reservar(agenda, historico)
    cancelar(agenda, historico)
    relatorios(agenda)
    buscar_por_nome(agenda)

Critérios de avaliação (rubrica resumida)

    Organização e uso correto de funções: 20%
    Uso correto de matriz e percursos com for: 25%
    Validações e condicionais: 20%
    Loop do menu e fluxo do programa: 20%
    Relatórios e histórico (listas): 15%

Bônus (opcional)

    Permitir reservar bloco de horários (ex.: 2h seguidas) validando disponibilidade
    Permitir exportar agenda para .txt (sem bibliotecas externas)
    Criar opção “Resetar agenda” com confirmação
