import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a',
                    format='%(levelname)s - %(message)s - %(asctime)s')  # %(asctime)s vai adicionar o horario do log

# Uma aplicação que vai receber uma senha e email para um usuario ter acesso a uma conta bancária
try:
    email = input('Digite seu email: ')
    senha = int(input('Digite sua senha bancária: '))
    if senha == 1234:
        print('Login feito com sucesso')
        logging.info(f'{email} entrou em sua conta bancária')
except ValueError as erro:
    print('Digite apenas numeros')
    logging.info(erro)
 
# após colocar este programa para funcionar, será criado um arquivo com a informação informando, caso a senha esteja correta,
# de acesso a conta.     
        