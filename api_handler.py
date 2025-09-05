 # Funções para consumir a API

import requests
from typing import (Dict,
                    Any)

from api_URLs import URLs
from inputs import selecionar_periodo_especifico

def solicitar_cotacao_tempo_real(moedas: str) -> Dict[str, Any]:
    """
    Solicita a cotação em tempo real para a moeda ou par de moedas especificado.

    Args:
        moedas (str): Código da moeda ou par de moedas no formato 'XXX-XXX'.

    Returns:
        Dict[str, Any]: Dicionário contendo os dados retornados pela API.

    Raises:
        requests.RequestException: Se ocorrer erro na requisição HTTP.
        json.JSONDecodeError: Se a resposta da API não for um JSON válido.
    """
    resposta = requests.get(f"{URLs['url_cotacao_tempo_real']}{moedas}")
    resposta.raise_for_status()
    return resposta.json()


def solicitar_cotacao_dias_anteriores(moedas: str, numero_dias: str) -> Dict[str, Any]:
    """
    Solicita a cotação das moedas para os últimos N dias.

    Args:
        moedas (str): Código da moeda ou par de moedas no formato 'XXX-XXX'.
        numero_dias (str): Número de dias para consulta das cotações.

    Returns:
        Dict[str, Any]: Dicionário contendo os dados retornados pela API.

    Raises:
        requests.RequestException: Se ocorrer erro na requisição HTTP.
        json.JSONDecodeError: Se a resposta da API não for um JSON válido.
    """
    resposta = requests.get(f"{URLs['url_cotacao_dias_anteriores_e_especificos']}{moedas}/{numero_dias}")
    resposta.raise_for_status()
    return resposta.json()


def solicitar_cotacao_periodo_especifico(moedas: list[str]) -> Dict[str, Any]:
    """
    Solicita a cotação das moedas para um período específico definido pelo usuário.

    Args:
        moedas (list[str]): Lista de códigos de moedas no formato 'XXX-XXX'.

    Returns:
        Dict[str, Any]: Dicionário contendo os dados retornados pela API para o período solicitado.

    Raises:
        requests.RequestException: Se ocorrer erro na requisição HTTP.
        json.JSONDecodeError: Se a resposta da API não for um JSON válido.
    """
    periodo_especifico = selecionar_periodo_especifico()
    start_date, end_date = periodo_especifico
    
    resposta = requests.get(
        f"{URLs['url_cotacao_dias_anteriores_e_especificos']}{moedas}/?start_date={start_date}&end_date={end_date}"
    )
    resposta.raise_for_status()
    return resposta.json()
