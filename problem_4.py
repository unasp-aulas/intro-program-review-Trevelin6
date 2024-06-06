valor_casa = float(input("Qual o valor da casa? "))  # Não alterar
salario = float(input("Qual é o salário? "))  # Não alterar
anos_pagar = int(input("Pagar em quantos anos? "))  # Não alterar
print(emprestimo(valor_casa,salario,anos_pagar))


def emprestimo(valor,salario,anos):
  prestacao = valor/(anos*12)
  if prestacao > (salario*0.3):
    return 'Reprovado'
  else:
    return 'Aprovado'
  