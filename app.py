import mysql.connector


db  =  mysql . conector . conectar (
    host = 'localhost' ,
    banco_de_dados =  'FROTA_VEICULOS' ,
    usuário =  'root' ,
    senha = 'Gui281209'
)


while True:
    print('==============================================')
    print('           CONTROLE DE FROTA')
    print('==============================================')
    print('')
    opcao = input('OPÇÕES DO PROGRAMA.\n'
    '[1] - REGISTRAR VEÍCULO\n'
    '[2] - ALTERAR DADOS \n'
    '[3] - LISTA DE VEÍCULOS\n'
    '[4] - SELECIONAR VEÍCULO POR PLACA\n'
    '[5] - DELETAR REGISTRO\n'
    '[6] - FINALIZAR EXECUÇÃO DO PROGRAMA\n'
    'Informe a opção desejada => ')