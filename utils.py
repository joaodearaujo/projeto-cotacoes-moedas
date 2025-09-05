# Funções auxiliares

import re
import requests
import json 

from typing import (Dict,
                    Any,
                    Optional)

from api_handler import (solicitar_cotacao_tempo_real,
                         solicitar_cotacao_dias_anteriores,
                         solicitar_cotacao_periodo_especifico)

from inputs import (selecionar_moedas,
                    selecionar_cotacao, 
                    selecionar_dias_anteriores)


def obter_moedas() -> str:
    """
    Solicita ao usuário que insira as moedas que deseja consultar, no formato 'XXX-XXX'.
    
    A função valida se a entrada:
    - não está vazia;
    - segue o padrão de três letras maiúsculas, um hífen e mais três letras maiúsculas.

    Returns:
        str: Código da moeda no formato 'XXX-XXX'.
    """
    while True:
        moedas = selecionar_moedas().upper().strip()
        if not moedas:
            print("Por favor, insira algum valor para a moeda.")
            continue
        if not re.fullmatch(r'^[A-Z]{3}-[A-Z]{3}$', moedas):
            print('Por favor, insira apenas letras no formato XXX-XXX.')
            continue
        return moedas


def obter_opcao() -> int:
    """
    Solicita ao usuário que selecione uma opção de cotação.

    A função valida se a entrada:
    - é um número;
    - está entre 1 e 3.

    Returns:
        int: Número correspondente à opção selecionada pelo usuário.
    """
    while True:
        try:
            opcao = selecionar_cotacao()
            if not opcao:
                print("Por favor, insira algum valor.")
                continue
            if not 1 <= opcao <= 3:
                print("Por favor, insira um valor entre 1 e 3.")
                continue
        except ValueError:
            print('Por favor, insira apenas números.')
            continue

        return opcao


def consumir_cotacao_tempo_real(moedas: str) -> Optional[Dict[str, Any]]:
    """
    Consome a API de cotação em tempo real para as moedas especificadas, tratando erros.

    Args:
        moedas (str): Código da moeda ou par de moedas no formato 'XXX-XXX'.

    Returns:
        Optional[Dict[str, Any]]: Dicionário com os dados da cotação, ou None em caso de falha.

    Possíveis erros tratados:
        - requests.RequestException: Erro na requisição HTTP.
        - json.JSONDecodeError: Resposta inválida da API (não JSON).
        - Exception: Outros erros inesperados.
    """
    try:
        resposta = solicitar_cotacao_tempo_real(moedas)
        return resposta
    except requests.RequestException as e:
        print(f"Erro na requisição: {e}")
    except json.JSONDecodeError:
        print("Resposta inválida da API.")
    except Exception as e:
        print(f"Erro inesperado: {e}") 
    return None   


def consumir_cotacao_dias_anteriores(moedas: str) -> Optional[Dict[str, Any]]:
    """
    Solicita a cotação das moedas para os últimos N dias, tratando erros e validando a entrada do usuário.

    Args:
        moedas (str): Código da moeda ou par de moedas no formato 'XXX-XXX'.

    Returns:
        Optional[Dict[str, Any]]: Dicionário com os dados da cotação, ou None em caso de falha.

    Possíveis erros tratados:
        - requests.RequestException: Erro na requisição HTTP.
        - json.JSONDecodeError: Resposta inválida da API (não JSON).
        - Exception: Outros erros inesperados.
    """
    while True:
        numero_dias = selecionar_dias_anteriores().strip()
        if not numero_dias:
            print('Por favor, insira algum valor.')
            continue
        if not numero_dias.isdigit():
            print('Por favor, insira apenas números.')
            continue
        break

    try:
        resposta = solicitar_cotacao_dias_anteriores(moedas, numero_dias)
        return resposta
    except requests.RequestException as e:
        print(f"Erro na requisição: {e}")
    except json.JSONDecodeError:
        print("Resposta inválida da API.")
    except Exception as e:
        print(f"Erro inesperado: {e}")    
    return None   


def consumir_cotacao_periodo_especifico(moedas: str) -> Optional[Dict[str, Any]]:
    """
    Solicita a cotação das moedas para um período específico definido pelo usuário, tratando erros.

    Args:
        moedas (str): Código da moeda ou par de moedas no formato 'XXX-XXX'.

    Returns:
        Optional[Dict[str, Any]]: Dicionário com os dados da cotação para o período, ou None em caso de falha.

    Possíveis erros tratados:
        - requests.RequestException: Erro na requisição HTTP.
        - json.JSONDecodeError: Resposta inválida da API (não JSON).
        - Exception: Outros erros inesperados.
    """
    try:
        resposta = solicitar_cotacao_periodo_especifico(moedas)
        return resposta
    except requests.RequestException as e:
        print(f"Erro na requisição: {e}")
    except json.JSONDecodeError:
        print("Resposta inválida da API.")
    except Exception as e:
        print(f"Erro inesperado: {e}")    
    return None
