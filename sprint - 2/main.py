class Avaliacao:
    def __init__(self, localizacao, descricao, nota):
        self.localizacao = localizacao
        self.descricao = descricao
        self.nota = nota

    def exibir_informacoes(self):
        print('Exibindo informações...')
        print('Localização: ', self.localizacao)
        print('Descrição: ', self.descricao)
        print('Nota: ', self.nota)


def exibir_menu():
    print('===== MENU =====')
    print('1. Adicionar uma avaliação')
    print('2. Listar todas as avaliações')
    print('3. Sair')


def adicionar_avaliacao(avaliacoes):
    localizacao = input('Informe a localização da avaliação: ')
    descricao = input('Descreva a avaliação: ')
    nota = float(input('Digite a nota (0-10): '))

    avaliacao = Avaliacao(localizacao, descricao, nota)
    avaliacoes.append(avaliacao)

    print('Avaliação adicionada com sucesso!')


def listar_avaliacoes(avaliacoes):
    if not avaliacoes:
        print('Nenhuma avaliação registrada.')
    else:
        for avaliacao in avaliacoes:
            avaliacao.exibir_informacoes()
            print()


# Função principal
def main():
    avaliacoes = []

    while True:
        exibir_menu()

        opcao = input('Escolha uma opção (1-3): ')

        match opcao:
            case '1':
                adicionar_avaliacao(avaliacoes)
            case '2':
                listar_avaliacoes(avaliacoes)
            case '3':
                print('Programa encerrado.')
                break
            case _:
                print('Opção inválida. Tente novamente.')

        print()


# Iniciar o programa
main()
