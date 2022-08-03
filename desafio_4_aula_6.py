digitado = input('Digite algo:')
print(type(digitado))

print('isalpha?') 
print(digitado.isalpha())

print('isnumber?')
print(digitado.isnumeric())

print('isalnum, alfanumeric?')
print(digitado.isalnum())

print('isupper, uppercase?')
print(digitado.isupper())

print ('isdecimal?')
print(digitado.isdecimal())

# também funciona fazer:
# print('é alfabético?', digitado.isalpha())
# dessa forma a resposta boleana aparece ao lado da pergunta.
