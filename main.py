import json

def ler_registro(file_name):
    data = ler_json(file_name)
    registro = None
    identificador = None
    sim = True
    while sim:
        identificador = input('Entre com o ID:')
        if identificador in data.keys():
            registro = data[identificador]
            print('Registro =', registro)
            sim = False
        else:
            print('ID sem registro!')
            resposta = input('Deseja buscar outro ID? (s/n)').lower()
            if 'n' in resposta:
                sim = False

    return registro, identificador


# função para atualizar um registro em um arquivo json a partir de um ID
def atualizar_registro(file_name):
    data = ler_json(file_name)
    print('ATUALIZAÇÃO', file_name, '\n')
    registro, identificador = ler_registro(file_name)
    if registro is None or identificador is None:
        print('O ID do registro não pode ser nulo!')
    colunas = eval(file_name)
    for coluna in colunas:
        valor = input('Informe {coluna}: ')
        registro[coluna] = valor
    data[identificador] = registro
    escrever_json(data, file_name)
    print('Registro {identificador} alterado!')


# função para remover um novo registro em um arquivo json  a partir de um ID
def remover_registro(file_name):
    data = ler_json(file_name)
    print('EXCLUSÃO', file_name, '\n')
    registro, identificador = ler_registro(file_name)
    if registro is None or identificador is None:
        print('O ID do registro não pode ser nulo!')
    else:
        print('Confirma a remoção do ID:', identificador, '? (s/n)\n'
                                                            'OBS: Essa operação não pode ser desfeita!')
        confirma = input().lower()
        if 's' in confirma:
            data.pop(identificador)
            escrever_json(data, file_name)
            print('Registro', identificador, 'removido!')
        else:
            print('A remoção do registro:', identificador, 'foi cancelada!')


# função para buscar registros em um arquivo json  a partir de um texto
def buscar_por_coluna(file_name):
    data = ler_json(file_name)
    print('BUSCA', file_name, '\n')
    if len(data) == 0:
        print('Base vazia!')
    else:
        while True:
            resultados = {}
            texto = input('Entre com o termo que deseja buscar: ').lower()
            for identificador, registro in data.items():
                for coluna, valor in registro.items():
                    if texto in valor.lower():
                        resultados[identificador] = registro
                        continue
            print(resultados)
            refazer = input('Deseja buscar por outro termo? (s/n)')
            if 's' not in refazer:
                break


def listar_registro(file_name):
    data = ler_json(file_name)
    print('LISTAGEM', file_name, '\n')
    if len(data) == 0:
        print('Base vazia!')
        # função precisa ser complementada
    # else:

    input('Tecle uma tecla para continuar ...')


def escrever_json(data, file_name):

    with open(file_name + '.json', 'w') as file:

        json.dump(data, file, indent = 4)
        file.close()


def ler_json(file_name):

    data = {}

    try:

        with open(file_name + '.json', 'r') as arquivo:

            data = json.load(arquivo)
            print(data)
            arquivo.close()
            return data

    except FileNotFoundError:

        escrever_json(data, file_name)
        return data


def criar_novo_registro(file_name):

    data = ler_json(file_name)
    novo = {}
    id = '1'
    ids = [int(k) for k in data.keys()]

    if len(ids) != 0:
        id += 1

    colunas = file_name
    print('INCLUSÃO', file_name, '\n')

    for coluna in colunas:

        print('Informe', coluna)
        novo[coluna] = input()

    data[id] = novo
    escrever_json(data, file_name)


def operacao(tabela):

    opcoes = ['1', '9']

    while True:

        print('\nO que você deseja fazer na base', tabela, ':\n\n'
                                                          '(1) Criar novo registro.\n'
                                                          '(9) Voltar menu.\n\n'
                                                          'Faça sua escolha: ')
        opcao = input()

        if opcao not in opcoes:
            input('\nOpção inválida! Tente novamente ...')

        else:

            if opcao == '1':
                criar_novo_registro(tabela)

            elif opcao == '9':
                break


def menu(tabela_estudantes):

    opcoes = ['1', '9']

    while True:
        opcao = input('Selecione a opção desejada:\n\n'
                      '(1) Gerenciar estudantes.\n'
                      '(9) Sair.\n\n'
                      'Faça sua escolha: ')

        if opcao in opcoes:

            if opcao == '1':
                operacao(tabela_estudantes)

            elif opcao == '9':
                break

            else:
                print('\nOpção inválida! Tente novamente.')

    print('Finalizando o programa...')
    exit(0)


if __name__ == '__main__':

    estudantes = ['matrícula', 'nome', 'sobrenome']
    tabela_de_estudantes = 'estudantes'

    menu(tabela_de_estudantes)
