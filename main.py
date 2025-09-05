# Inicializa o app Streamlit'

from outputs import exibir_menu

from utils import (obter_moedas, 
                   obter_opcao,
                   consumir_cotacao_tempo_real, 
                   consumir_cotacao_dias_anteriores, 
                   consumir_cotacao_periodo_especifico)
from inputs import perguntar_sobre_encerramento 

def main() -> None:
    """
    Função principal do programa de consulta de cotações de moedas.

    Esta função exibe um menu interativo para o usuário, permitindo:
    1. Consultar a cotação em tempo real de moedas específicas.
    2. Consultar a cotação de dias anteriores.
    3. Consultar a cotação em um período específico.

    Após cada consulta, o programa pergunta ao usuário se deseja encerrar.
    Caso o usuário confirme, o programa é finalizado; caso contrário, o menu é exibido novamente.

    Não recebe parâmetros e não retorna nenhum valor.
    """

    while True: 

        exibir_menu()
        moedas = obter_moedas()
        opcao = obter_opcao()
        
        if opcao == 1:
            cotacao = consumir_cotacao_tempo_real(moedas)
            print(cotacao)
        elif opcao == 2:
            cotacao = consumir_cotacao_dias_anteriores(moedas)
            print(cotacao)
        elif opcao == 3:
            cotacao = consumir_cotacao_periodo_especifico(moedas)
            print(cotacao)

        encerrar_programa = perguntar_sobre_encerramento().upper().strip()

        if encerrar_programa == 'S':
            print('Programa encerrador. Obrigado por utilizar!')
            break
        else:
            continue

main()
