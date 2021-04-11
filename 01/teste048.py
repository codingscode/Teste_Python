from datetime import datetime


momento = datetime.now()  # momento em greenwhich

print(momento)
print(dir(momento))
print(f'ano: {momento.year}')
print(f'Dia da semana mês dia horario ano :  {momento.ctime()}') # Sun Apr 11 22:28:28 2021
print(f'data: {momento.date()}')
print(f'número do dia: {momento.day}')
print(f'hora do dia: {momento.hour}')
print(f'minuto do dia {momento.minute}')
print(f'segundos: {momento.second}')
print(f'mês do dia: {momento.month}')
print(f'ano-mes-dia hora:min:segundo.milisegundos : {momento.now()}') # ano-mes-dia hora:min:segundo.milisegundos
print(momento.today())
print(f'numero da semana(0-6): {momento.weekday()}') # numero da semana
print(momento.strftime('%A'))

print('----------------------')
