# counter = 1
# while counter <= 5:
#     print('No se detiene')
#     counter+=1
# else:
#     print('Terminamos')

response = ''
while response.lower() != 'bye':
    response = input('Escribe bye para salir: ')
else:
    print('Terminamos')