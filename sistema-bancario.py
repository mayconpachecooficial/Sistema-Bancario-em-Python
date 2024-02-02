saldo = 0
movimentacoes = []

valor = float(input('Digite o valor do depósito:'))
saldo += valor
movimentacoes.append(f'Depósito: R$ {valor:.2f}')
print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')

valor = float(input('Digite o valor do saque: '))
if valor <= 500 and saldo >= valor:
    saldo -= valor
    movimentacoes.append(f'Saque: R$  {valor:.2f}')
    print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
else:
    movimentacoes.append('Não é possível realizar o saque.')
    print('Não é possível realizar o saque.')
    
print('\nExtrato:')
for movimentacao in movimentacoes:
    print(movimentacao)

if not movimentacoes:
    print('Não foram realizadas movimentações.')
    
print(f'Saldo Atual: R$ {saldo:.2f}')