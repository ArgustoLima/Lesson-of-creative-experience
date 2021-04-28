import json


def ler_registro(file_name):
    data = ler_json(file_name)
    registro = None

    while True:

        identificador = input('\nEntre com o ID: ')

        if identificador in data.keys():

            registro = data[identificador]
            print(f'\nRegistro = {registro}')
            break

        else:

            print('\nID sem registro!')
            resposta = input('\nDeseja buscar outro ID? (s/n) ').lower()

            if 'n' in resposta:
                break

    return registro, identificador


def escrever_json(data, file_name):
    with open(file_name + '.json', 'w') as file:
        json.dump(data, file, indent=4)
        file.close()


def ler_json(file_name):
    data = {}

    try:

        with open(file_name + '.json', 'r') as arquivo:

            data = json.load(arquivo)
            arquivo.close()
            return data

    except FileNotFoundError:

        escrever_json(data, file_name)
        return data


def buscar_por_coluna(file_name):
    data = ler_json(file_name)
    print(f'\nBusca de {file_name}:')

    if len(data) == 0:
        print('Base vazia!')

    else:

        while True:

            resultados = {}
            texto = input('\nEntre com o termo que deseja buscar: ').lower()

            for identificador, registro in data.items():

                for coluna, valor in registro.items():

                    if texto in valor.lower():
                        resultados[identificador] = registro
                        continue

            print('\n', resultados)
            refazer = input('\nDeseja buscar por outro termo? (s/n) ').lower()

            if 's' not in refazer:
                break


def atualizar_registro(file_name):
    data = ler_json(file_name)
    print(f'\nAtualização de {file_name}:')
    registro, identificador = ler_registro(file_name)

    if registro is None:
        print('\nO ID do registro não pode ser nulo!')

    colunas = eval(file_name)

    for coluna in colunas:
        registro[coluna] = input(f'\nInforme {coluna}: ')

    data[identificador] = registro
    escrever_json(data, file_name)
    print(f'\nRegistro {identificador} alterado!')


def listar_registro(file_name):
    data = ler_json(file_name)
    print(f'\nListagem de {file_name}:')

    if len(data) == 0:
        print('Base vazia!')

    else:
        for key in data.keys():
            print(f'{data[key]}')

    input('Tecle uma tecla para continuar ...')


def remover_registro(file_name):
    data = ler_json(file_name)
    print(f'\nExclusão de {file_name}:')
    registro, identificador = ler_registro(file_name)

    if registro is None or identificador is None:
        print('\nO ID do registro não pode ser nulo!')

    else:
        print('OBS: Essa operação não pode ser desfeita!')
        confirma = input(f'Confirma a remoção do ID: {identificador}? (s/n)').lower()

        if 's' in confirma:

            data.pop(identificador)
            escrever_json(data, file_name)
            print(f'\nRegistro {identificador} removido!')

        else:
            print(f'\nA remoção do registro: {identificador} foi cancelada!')


def criar_novo_registro(file_name):
    data = ler_json(file_name)
    novo = {}
    keys = [int(k) for k in data.keys()]

    if len(keys) != 0:
        key = str(max(keys) + 1)

    else:
        key = '1'

    colunas = eval(file_name)
    print(f'\nInclusão de {file_name}:')

    for coluna in colunas:
        novo[coluna] = input(f'\nInforme {coluna}: ')

    data[key] = novo
    escrever_json(data, file_name)


def operacao(tabela):
    opcoes = ['1', '2', '3', '4', '5', '9']

    while True:

        print(f'\nO que você deseja fazer na base {tabela}:\n\n'
              '(1) Criar novo registro.\n'
              '(2) Remover um registro.\n'
              '(3) Atualizar um registro.\n'
              '(4) Buscar Registro.\n'
              '(5) Listar Registro.\n'
              '(9) Voltar menu.\n')
        opcao = input('Faça sua escolha: ')

        if opcao not in opcoes:
            input('\nOpção inválida! Tente novamente ...')

        else:

            if opcao == '1':
                criar_novo_registro(tabela)

            elif opcao == '2':
                remover_registro(tabela)

            elif opcao == '3':
                atualizar_registro(tabela)

            elif opcao == '4':
                buscar_por_coluna(tabela)

            elif opcao == '5':
                listar_registro(tabela)

            else:
                break


def menu():
    opcoes = ['1', '2', '3', '4', '5', '9']

    while True:
        opcao = input('Selecione a opção desejada:\n\n'
                      '(1) Gerenciar estudantes.\n'
                      '(2) Gerenciar professores.\n'
                      '(3) Gerenciar disciplinas.\n'
                      '(4) Gerenciar turmas.\n'
                      '(5) Gerenciar matriculas.\n'
                      '(9) Sair.\n\n'
                      'Faça sua escolha: ')
        print('\n' * 15)

        if opcao in opcoes:

            if opcao == '1':
                tabela_de_estudantes = 'estudantes'
                operacao(tabela_de_estudantes)

            elif opcao == '2':
                tabela_de_professores = 'professores'
                operacao(tabela_de_professores)

            elif opcao == '3':
                tabela_de_disciplinas = 'disciplinas'
                operacao(tabela_de_disciplinas)
            elif opcao == '4':
                tabela_de_turmas = 'turmas'
                operacao(tabela_de_turmas)

            elif opcao == '5':
                tabela_de_matriculas = 'matriculas'
                operacao(tabela_de_matriculas)

            elif opcao == '9':
                break

            else:
                print('\nOpção inválida! Tente novamente.')

    print('Finalizando o programa...')
    exit(0)


if __name__ == '__main__':
    estudantes = ['matrícula', 'nome', 'sobrenome']
    professores = ['codigo_professor', 'nome_professor', 'sobrenome_professor']
    disciplinas = ['codigo_disciplina', 'nome_disciplina']
    turmas = ['codigo_turma', 'cod_professor', 'cod_disciplina']
    matriculas = ['codigo_turma', 'codigo_estudante']
    menu()
