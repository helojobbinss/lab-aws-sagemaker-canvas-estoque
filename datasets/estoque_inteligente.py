#Bibliotecas utilizadas
import pandas as pd
import numpy
from datetime import datetime, timedelta

#definição
data_inicial = datetime(2023,12,31)
produto_por_dia = 25
dias = 120
estoque_max_inicial = 100
quantidade_vendida_por_dia_max = 10

dados = []

for dia in range(dias):
    data_atual = data_inicial + timedelta(days=dia)
    
    for produto in range(produto_por_dia):
        id_produto = produto +1
        flag_promo = numpy.random.choice([True,False])
        
        if dias == 0:
            quantidade_estoque = numpy.random.randint(1,estoque_max_inicial)
        else:
            registro_anterior = next((item for item in dados if item['ID_PRODUTO']==id_produto and item['DIA']==data_atual - timedelta(days=1)),None)
            preco_produto = numpy.random.uniform(1,100)
            
            if registro_anterior:
                quantidate_vendida = numpy.random.randint(1,quantidade_vendida_por_dia_max)
                quantidade_estoque = max(0,registro_anterior['QUANTIDADE_ESTOQUE'] - quantidate_vendida)
                if flag_promo == 1:
                    preco_produto = registro_anterior["PRECO"] - (registro_anterior["PRECO"]*0.3)
                else:
                    preco_produto = registro_anterior["PRECO"]
            else:
                quantidade_estoque = numpy.random.randint(1,estoque_max_inicial)
        dados.append({
        'ID_PRODUTO':id_produto,
        'DIA':data_atual.strftime('%d-%m-%Y'),
        'FLAG_PROMO':flag_promo,
        'PRECO': round(preco_produto,2),
        'QUANTIDADE_ESTOQUE': quantidade_estoque
        })
        
df = pd.DataFrame(dados)

df.to_csv('dataset_estoque.csv', index=False)