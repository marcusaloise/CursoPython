# enviar email com os detalhes de compra 

compra_confirmada = False
dados_compra = 'compra no valor de R$12.50'


for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes do pedido enviado no seu email')
        break
else:
    print('Falaha na compra')
