# 📊 Previsão de Estoque Inteligente na AWS com [SageMaker Canvas](https://aws.amazon.com/pt/sagemaker/canvas/)

A analise de dados passou a ser uma área importante para as empresas, auxiliando as empresas para realizar decisões precisas, trazendo uma gestão orientada a dados de modo que traga melhorias em setores de marketing, aumento nas vendas e melhor atendimento ao cliente. Porém este processo pode ser demorado inúmeras vezes e como solução tem sido aplicados modelos de aprendizado de máquina, com o objetivo de reduzir o tempo de análise e trazer uma maior precisão.
Assim como a analise de dados e conceitos de machine learning, tem tido um grande aumento em ferramentas no–code, onde temos a possibilidade de criar aplicações sem utilizar código. Um exemplo é a ferramenta disponibilizada pela AWS, o SageMaker Canvas que possibilita o treinamento de modelos de machine learning sem utilizar códigos.
Durante os dias 15/07 a 01/08 a DIO trouxe em parceria com a Nexa um bootcamp ensinando a utilizar e as principais ferramentas do SageMaker e como desafio foi proposto a criação de um modelo de estoque inteligente na qual irei abordar os resultados do treinamento.


## 🎯 Objetivos Deste Desafio de Projeto (Lab)

O objetivo principal é testar os conhecimentos fornecidos durante o bootcamp e criando um modelo de previsão de estoque inteligente fornecendo informações sobre os produtos das empresas fictícia.


### 1. Selecionar Dataset

Para criação de uma base de dados foi utilizado um script em Python utilizando as bibliotecas panda para criação do arquivo csv e utilização da biblioteca Random para gerar números pseudoaleatório para venda e estoque disponível. Também foi utilizado a biblioteca datatime e timedelta pra manipular as datas em um certo período. Foi utilizado 25 produtos em estoque por dia e analisado durante um período de 120 dias com variação de preços e flag de promoção.
![image](https://github.com/user-attachments/assets/469b4c2c-aff7-4818-8270-9572ec03e383)


Foi realizado a importação do arquivo do arquivo csv e tratado pelo próprio SageMaker após a importação e criado a base de dados para treinamento, verificando a ocorrência de valores duplicados e a interferência no modelo 
![image](https://github.com/user-attachments/assets/52be607d-c029-4f27-a7ff-7f3e693a95f8)

Após a ferramenta validar os dados, foi importado o dataset para criação do modelo.

MODELO UTILIZADO
O SageMaker Canvas trás três opções de modelo para treinamento, modelos baseados em textos, modelos utilizando imagens e modelos de predição de séries temporais. Considerando como objetivo a previsão da quantidade de estoque e vendas durante um período de tempo, foi utilizado o modelo de treinamento de predição de séries temporais.
 ![image](https://github.com/user-attachments/assets/d9d7e485-b8d0-4a2d-be9d-b5c2d4dc9a53)

VÁRIAVEL TARGET 
Antes de selecionar a variável target, a ferramenta disponibiliza a visualização dos diferentes modelos. Considerando como problema a quantidade de estoque durante um período de tempo, a variável target foi a quantidade de estoque.
![image](https://github.com/user-attachments/assets/d5401853-7953-4450-ba0b-1de782d7d7a2)
 
A ferramenta traz sugestões de tipos de modelo, devido a escolha da quantidade no estoque como variável target, o modelo sugerido e aplicado foi de predição de séries temporais podendo ser aplicado também modelos numéricos. Escolhi usar o modelo de predição de séries temporais devido a métricas como P10, P50 e P90 abordadas futuramente para análise de caso.
![image](https://github.com/user-attachments/assets/c9a5afbf-5a47-4e72-9ad4-f58624462a44)
 
Após a definição da variável target, foi definido como item ID o próprio ID de cada produto com base nos dias apresentados e sendo analisado a interferência de feriados nacionais na quantidade de produtos.
![image](https://github.com/user-attachments/assets/cc63016d-625e-46b3-bca0-b1737e96b044)

 
A ferramenta nos possibilita dois treinamentos, Quick Build sendo um treinamento com duração curta, mas afetando na precisão da análise dependendo da quantidade de dados fornecidos. A segunda opção é Standard build com duração de 2 a 4 horas, mas com maior precisão. Considerando a quantidade de dados e tempo, utilizei Quick build para treinamento do modelo.
ANÁLISE
Após a análise, o SageMaker Canvas traz a interferência de cada coluna sobre a quantidade de eventos, no modelo apresentado a coluna que apresentou maior interferência na quantidade presente no estoque foi os feriados nacionais com 6,54% de impacto sobre ele, seguido de preço com 0,5% de interferência e nenhum impacto causado pela flag de promoção.
 ![image](https://github.com/user-attachments/assets/a96b607e-c3c6-4344-b6d6-398c893b334d)

Outras métricas trazidas pela ferramenta são:
Perda Quantidade Média Ponderada (wQL): calcula a média de precisão nos quantis P10 (considera o pior caso), P50 (caso comum) e P90 (demonstra o melhor cenário) de cada um dos produtos em estoque
Erro Percentual absoluto ponderado (WAPE): mede o desvio geral dos valores previstos dos valores observados sendo considerado valores próximos a zero um modelo com menor erros.
Room Mean Square Error (RMSE): calcula a diferença média entre os valores previstos e os valores reais trazendo a raiz quadrada dos erros. Valores menores demonstram estar mais próximos a valores reais.
Erro Escalado Médio absoluto (MASE): compara o erro de previsão com um modelo simples sendo valores menores que 1 considerados mais precisos.
Erro Percentual Médio Absoluto (MAPE): calcula a média de todos os pontos temporais, ou seja, os erros de previsão em relação aos valores reais.
No modelo treinado, houve indicio de valores considerados relativamente distantes de valores reais com 28,16% de RMSE e 1,5% em relação ao MAPE mas as métricas seguintes mostram menor erro entre os valores.
![image](https://github.com/user-attachments/assets/948bc60f-e2a8-4752-a8e5-2cf48b4dc977)
 
Após o treinamento, foi realizado a predição simples dos produtos disponíveis tendo diversos casos como o apresentado abaixo onde o produto 7 tem seu caso comum de vendas próximo ao valor de melhor caso, indicando uma quantidade alta no estoque.
Produto 7
 ![image](https://github.com/user-attachments/assets/35889353-3de3-4824-bf16-7cee1a01b160)

Do mesmo modo alguns produtos apresentaram seu caso comum mais próximo ao menor caso podendo indicar venda sem reposição, como o caso do produto 17.

Produto 17
 ![image](https://github.com/user-attachments/assets/07bd1aff-da68-4a19-a4d5-ab039c7a0d53)


Já outros casos como o produto 6 apresentam um valor intermediário em seu caso comum podendo indicar um produto com pouca saída e reposição.
 ![image](https://github.com/user-attachments/assets/534aecd2-24db-4d15-a55d-194c064150d9)

CONCLUSÃO
O modelo apresentou valores que podem estar relativamente distantes de valores reais mas que ainda podem ser utilizados para analise demonstrando a quantidade de vendas de cada produto e fornecendo a ideia da situação de cada produto disponível em estoque.






