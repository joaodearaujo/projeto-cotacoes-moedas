def selecionar_moedas() -> str:
    """
    Solicita ao usuário que insira as moedas desejadas no formato 'XXX-XXX'.

    Returns:
        str: Código da moeda ou par de moedas no formato 'XXX-XXX'.
    """
    return str(input('Digite as moedas escolhidas no formato XXX-XXX: '))


def selecionar_cotacao() -> int:
    """
    Solicita ao usuário que selecione uma opção de cotação.

    Returns:
        int: Número da opção selecionada pelo usuário.
    """
    return int(input('Selecione uma opção de cotação: '))


def perguntar_sobre_encerramento() -> str:
    """
    Pergunta ao usuário se deseja encerrar o programa.

    Returns:
        str: Resposta do usuário ('S' ou 'N').
    """
    return input('Deseja encerrar o programa? [S/N] ')


def selecionar_dias_anteriores() -> str:
    """
    Solicita ao usuário que informe o número de dias para consultar cotações passadas.

    Returns:
        str: Número de dias informado pelo usuário.
    """
    return input('Informe o número de dias: ')


def selecionar_periodo_especifico() -> tuple[str, str]:
    """
    Solicita ao usuário que informe um período específico para consulta de cotações.

    Returns:
        tuple[str, str]: Tupla contendo:
            - start_date (str): Data de início no formato 'YYYYMMDD'.
            - end_date (str): Data de término no formato 'YYYYMMDD'.
    """
    start_date = input('Informe a data de início (ex: 20230101): ').strip()
    end_date = input('Informe a data de término (ex: 20230131): ').strip()
    return (start_date, end_date)
