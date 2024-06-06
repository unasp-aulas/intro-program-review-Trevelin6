
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print('Valor inválido')
        else:
            return n


soma = 0
while True:
  n = leiaInt('Digite um número: ')
  if n == 0:
    break
  else:
    soma += n
print(soma)
