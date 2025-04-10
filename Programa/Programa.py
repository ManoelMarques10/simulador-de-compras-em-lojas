#Pograma Básico Que Simula Vendas À Vista, Parcelas E Descontos.

try:
    nome_loja = 'ManoelMarques10'
    print(f'\33[1:32m=~=~=~=~=~{nome_loja}=~=~=~=~=~')
    compras = float(input('\33[33mQual Foi O Valor Das Compras?\nResposta: '))
    print('\33[33mQual Método De Pagamento? ')
    print('\33[34m[1] Para Dinheiro Ou Cheque À Vista. (10% De Desconto).')
    print('[2] Para Cartão De Crédito Até 2X. (Valor Normal)')
    print('[3] Para A Vista No Débito. (5% De Desconto).')
    print('[4] Para De 3 Até 10X No Cartão De Crédito. (20% De Juros).')
    metodo = int(input('\33[33mDigite O Número Do Método Desejado.\nMétodo: '))
    avista = compras - (compras*10/100)
    cartao1x = compras
    cartao2x = compras / 2
    debito = compras - (compras*5/100)
    if metodo == 1:
        print(f'\33[31mO Valor A Ser Pago Com \33[33m10%\33[m\33[31m De Desconto É De \33[32mR${avista:.2f}')
    elif metodo == 3:
        print(f'\33[31mO Valor A Ser Pago Com \33[33m5%\33[m\33[31m De Desconto É De \33[32mR${debito:.2f}')
    elif metodo == 2:
        vezes = int(input('\33[33mDigite 1 Para 1X E 2 Para 2X No Cartão\nParcelas: '))
        if vezes == 1:
            print(f'\33[31mO Valor A Ser Pago É De \33[32mR$1X De R${cartao1x:.2f}')
        elif vezes == 2:
            print(f'\33[31mO Valor A Ser Pago É De \33[32m2X De R${cartao2x:.2f}')
        else:
            print('\33[31mOps, Algo Deu Errado, Tente Novamente!')
    elif metodo == 4:
        cartao3x = (compras + (compras*20/100)) / 3
        cartao4x = (compras + (compras*20/100)) / 4
        cartao5x = (compras + (compras*20/100)) / 5
        cartao6x = (compras + (compras*20/100)) / 6
        cartao7x = (compras + (compras*20/100)) / 7
        cartao8x = (compras + (compras*20/100)) / 8
        cartao9x = (compras + (compras*20/100)) / 9
        cartao10x = (compras + (compras*20/100)) / 10
        totall = (compras + (compras*20/100))
        v310 = int(input('\33[33mEm Quantas Vezes Deseja Parcelar? Você Pode Digitar De 3 A 10.\nParcelas: '))
        if v310 == 3:
            print(f'\33[31mO Valor A Ser Pago É De \33[32m3X De R${cartao3x:.2f} Total: R${totall:.2f}')
        elif v310 == 4:
            print(f'\33[31mO Valor A Ser Pago É De \33[32m4X De R${cartao4x:.2f} Total: R${totall:.2f}')
        elif v310 == 5:
            print(f'\33[31mO Valor A Ser Pago É De \33[32m5X De R${cartao5x:.2f} Total: R${totall:.2f}')
        elif v310 == 6:
            print(f'\33[31mO Valor A Ser Pago É De \33[32m6X De R${cartao6x:.2f} Total: R${totall:.2f}')
        elif v310 == 7:
            print(f'\33[31mO Valor A Ser Pago É De \33[32m7X De R${cartao7x:.2f} Total: R${totall:.2f}')
        elif v310 == 8:
            print(f'\33[31mO Valor A Ser Pago É De \33[32m8X De R${cartao8x:.2f} Total: R${totall:.2f}')
        elif v310 == 9:
            print(f'\33[31mO Valor A Ser Pago É De \33[32m9X De R${cartao9x:.2f} Total: R${totall:.2f}')
        elif v310 == 10:
            print(f'\33[31mO Valor A Ser Pago É De \33[32m10X De R${cartao10x:.2f} Total: R${totall:.2f}')
        else:
            print('\33[31mOps, Quantidade Invalida De Parcelas, Tente de 3 A 10.')
except ValueError:
    print('\33[31mOps, Algo Deu Errado, Tente Novamente!')


