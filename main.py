import json


# função para escrever em um arquivo json (olhar na pasta do seu projeto, será criado um
# arquivo .json com o nome da tabela passada por parÃ¢metro)
def escrever_json(data, file_name):
    with open(file_name + '.json', 'w') as f:
        json.dump(data, f, indent=4)
        f.close()


# funÃ§Ã£o para ler em um arquivo json e colocar em memÃ³ria
def ler_json(file_name):
    data = {}
    try:
        with open(file_name + '.json', 'r') as f:
            data = json.load(f)
            f.close()
            return data
    except FileNotFoundError:
        escrever_json(data, file_name)
        return data


# funÃ§Ã£o para criar um novo registro em um arquivo json
def criar_novo_registro(file_name):
    data = ler_json(file_name)
    novo = {}
    id = '1'
    ids = [int(k) for k in data.keys()]
    if len(ids) != 0:
        id = str(max(ids) + 1)
    colunas = eval(file_name)
    print('INCLUSÃƒO', file_name, '\n')
    for coluna in colunas:
        print('Informe', coluna)
        valor = input()
        novo[coluna] = valor
    data[id] = novo
    escrever_json(data, file_name)


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


# funÃ§Ã£o para atualizar um registro em um arquivo json a partir de um ID
def atualizar_registro(file_name):
    data = ler_json(file_name)
    print('ATUALIZAÃ‡ÃƒO', file_name, '\n')
    registro, identificador = ler_registro(file_name)
    if registro is None or identificador is None:
        print('O ID do registro nÃ£o pode ser nulo!')
        finalizar_programa()
    colunas = eval(file_name)
    for coluna in colunas:
        valor = input('Informe {coluna}: ')
        registro[coluna] = valor
    data[identificador] = registro
    escrever_json(data, file_name)
    print('Registro {identificador} alterado!')


# funÃ§Ã£o para remover um novo registro em um arquivo json  a partir de um ID
def remover_registro(file_name):
    data = ler_json(file_name)
    print('EXCLUSÃƒO', file_name, '\n')
    registro, identificador = ler_registro(file_name)
    if registro is None or identificador is None:
        print('O ID do registro nÃ£o pode ser nulo!')
    else:
        print('Confirma a remoÃ§Ã£o do ID:', identificador, '? (s/n)\n'
                                                            'OBS: Essa operaÃ§Ã£o nÃ£o pode ser desfeita!')
        confirma = input().lower()
        if 's' in confirma:
            data.pop(identificador)
            escrever_json(data, file_name)
            print('Registro', identificador, 'removido!')
        else:
            print('A remoÃ§Ã£o do registro:', identificador, 'foi cancelada!')


# funÃ§Ã£o para buscar registros em um arquivo json  a partir de um texto
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
        # funÃ§Ã£o precisa ser complementada
    # else:

    input('Tecle uma tecla para continuar ...')


def finalizar_programa():
    print('Finalizando o programa...')
    exit(0)


def limpar_tela():
    print('\n' * 100)


def operacao(tabela):
    opcoes = ['1', '9']
    ativo = True
    while ativo:
        limpar_tela()
        print('O que vocÃª deseja fazer na base', tabela, ':\n\n'
                                                          '(1) Criar novo registro.\n'
                                                          '(9) Voltar menu.\n\n'
                                                          'FaÃ§a sua escolha: ')
        opcao = input().lower()

        if opcao not in opcoes:
            input('OpÃ§Ã£o invÃ¡lida! Tente novamente ...')
        else:
            limpar_tela()
            if opcao == '1':
                criar_novo_registro(tabela)
            elif opcao == '9':
                ativo = False


def menu():
    opcoes = ['1', '9']
    ativo = True
    while ativo:
        limpar_tela()
        opcao = input('Selecione a opÃ§Ã£o desejada:\n\n'
                      '(1) Gerenciar estudantes.\n'
                      '(9) Sair.\n\n'
                      'FaÃ§a sua escolha: ').lower()
        if opcao in opcoes:
            if opcao == '1':
                operacao(tabela1)
            elif opcao == '9':
                ativo = False
            else:
                print('OpÃ§Ã£o invÃ¡lida! Tente novamente.')

    finalizar_programa()


if __name__ == '__main__':
    # definindo os nomes das colunas para a tabela estudantes
    estudantes = ['matrÃ­cula', 'nome', 'sobrenome']
    tabela1 = 'estudantes'  # nome da tabela deve ser o mesmo nome da variÃ¡vel

    # Seguindo o mesmo exemplo de criaÃ§Ã£o das tabelas pode-se criar quantas
    # forem necessÃ¡rias

    # chamada principal do programa
    menu()

