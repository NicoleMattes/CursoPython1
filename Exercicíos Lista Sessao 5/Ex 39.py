"""
Uma empresa decide dar um aumento aos seus funcionários, de acordo com uma tabela que considera o salário atual
e o tempo de serviço de cada funcionário. Os funcionários com menor salário terão um aumento proporcionalmente
maior do que os funcionários com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário
irá receber um bônus adicional de salário. Faça um programa que leia:
    * O valor do salário atual do funcionário;
    * O tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa)
Use a tabela a baixo para calcular o salário reajustado deste funcionários e imprima o valor do salario final
reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum aumento.
    - Salario atual: até 500,00 - REajuste 25% - Tempo de serviço: abaixo de 1 ano - Bônus: Sem bônus
    - Salario atual: até 1000,00 - REajuste 20% - Tempo de serviço: de 1 a 3 anos - Bônus: 100,00
    - Salario atual: até 1500,00 - REajuste 15% - Tempo de serviço: de 4 a 6 anos - Bônus: 200,00
    - Salario atual: até 2000,00 - REajuste 10% - Tempo de serviço: de 7 a 10 anos - Bônus: 300,00
    - Salario atual: acima de 2000,00 - REajuste sem reajuste - Tempo de serviço: acima de 10 anos - Bônus: 500,00
"""

salario_atual = float(input("Informe o salário atual do funcionário \n"))
tempo_de_servico = int(input("Informe em meses o tempo de trabalho do funcionário na empresa \n"))
tempo_de_servico = tempo_de_servico / 12

if salario_atual <= 500:
    salario_atual = salario_atual * 1.25
elif salario_atual <= 1000:
    salario_atual = salario_atual * 1.20
elif salario_atual <= 1500:
    salario_atual = salario_atual * 1.15
elif salario_atual <= 2000:
    salario_atual = salario_atual * 1.10

if 0 < tempo_de_servico < 4:
    salario_atual = salario_atual + 100
elif 3 < tempo_de_servico < 7:
    salario_atual = salario_atual + 200
elif 6 < tempo_de_servico < 11:
    salario_atual = salario_atual + 300
elif tempo_de_servico > 10:
    salario_atual = salario_atual + 500
