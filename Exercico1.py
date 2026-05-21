import re

texto = "Painho pai pai "

padrão = re.sub(r'/s+' , "", texto)
print(padrão)

