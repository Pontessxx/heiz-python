import matplotlib.pyplot as plt

dados_pH = []
dados_temperatura = []
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ags', 'Set', 'Out', 'Nov', 'Dez']
count = 0
opcao = 0

def exibir_menu():
    print('_______________')
    print('-  Hortotech  -')
    print('_______________')
    print('\nAQUI ESTA NOSSO CODIGO EM VERSÃO PITHON')
    print('\nUTILIZAMOS FERRAMENTAS VISTAS EM AULA')
    print('\nEscolha uma opção:')
    print('(1) Inserir dados - mensais')
    print('(2) Ver gráfico')
    print('(0) Sair do código')

def calcular_pH_descricao(pH):
    if pH < 7:
        return 'Ácido'
    elif pH > 7:
        return 'Básico'
    else:
        return 'Neutro'

def calcular_temperatura_descricao(media_temp):
    if media_temp < 20:
        return 'Fria'
    elif media_temp > 30:
        return 'Quente'
    else:
        return 'Mediana'

def plotar_grafico():
    plt.plot(dados_pH, color='darkcyan', label='pH da água')
    plt.plot(dados_temperatura, color='orange', label='Temperatura')
    plt.title('Qualidade do ar - Anual')
    plt.xlabel('Meses')
    plt.ylabel('Valor')
    plt.xticks(range(12), meses)
    plt.legend()
    plt.show()

while True:
    exibir_menu()
    opcao = input('Opção: ')

    match opcao:
        case '1':
            for i in range(12):
                mes = meses[i]
                try:
                    pH_agua = float(input(f'________{mes}_______:\nDigite o valor do pH da água: '))
                    temperatura = float(input(f'Digite a temperatura em {mes}: '))
                except ValueError:
                    print('Valor inválido. Por favor, digite um número.')

                descricao_pH = calcular_pH_descricao(pH_agua)
                print(f'O pH da água é: {descricao_pH}')

                dados_pH.append(pH_agua)
                dados_temperatura.append(temperatura)
                count += 1

                if count == 12:
                    break

        case '2':
            if not dados_pH or not dados_temperatura:
                print('Nenhum dado inserido. Por favor, insira os dados primeiro.')
            else:
                try:
                    media_temperatura = sum(dados_temperatura) / len(dados_temperatura)
                    descricao_temperatura = calcular_temperatura_descricao(media_temperatura)
                    print(f'A média de temperatura é: {media_temperatura}°C ({descricao_temperatura})')
                except ZeroDivisionError:
                    print('Nenhum dado de temperatura inserido.')

                try:
                    media_pH = sum(dados_pH) / len(dados_pH)
                    print(f'A média do pH da água é: {round(media_pH, 1)}')
                except ZeroDivisionError:
                    print('Nenhum dado de pH da água inserido.')

                print('\nGráfico:')
                plotar_grafico()

        case '0':
            print('Saindo do programa...')
            break

        case _:
            print('Opção inválida. Por favor, escolha novamente.')
 