import re 

dinheiro = 'R$ 49,00 , R$ 129,00 , R$200 reais'
money = re.findall(r'\d+)',dinheiro)
print(money)