
def exibir_menu() -> None:
    
    print(f'='*15 +' Olá! Seja bem vindo ao Sistema de Cotação de Moedas '+15*'=' )
    print('''\nLista de moedas disponível para cotação:
          
    USD - Dólar Americano
    EUR - Euro
    JPY - Iene Japonês
    GBP - Libra Esterlina
    CHF - Franco Suíço
    CAD - Dólar Canadense
    AUD - Dólar Australiano
    CNY - Yuan Chinês
    BRL - Real Brasileiro
    MXN - Peso Mexicano
    INR - Rupia Indiana
    RUB - Rublo Russo           
          ''')
    
    print('''Opções disponíveis:
          
    1. Em Tempo Real
    2. Dias Anteriores (máx. 360 dias)
    3. Período Específico (máx. 360 dias)
                     ''')
    
    