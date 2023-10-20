# logging - serve para guardar informações de erros que o programa acuse. Não ...
# ..apenas erros, mas exemplo, caso haja um login no programa, ele vai registrar tudo.

import logging

# niveis de log
# debug -> Só estou informando informaçoes para os desenvolvedores.
# info -> Só quero informar sobre algo que está acontecendo no programa, mas não é um erro.
# warning -> Quero alertar sobre algo que está acontecendo, possivelmente fora do esperado, mas ainda não é um erro, mas pode ser que seja no futuro
# critical -> Um erro com consequencias graves


# Abaixo ele vai definir algumas regras pra impressão do log de erro no terminal.
# filename='serve para colocar o nome do arquivo.log'
# filemode='a' -> vai abrir arquivo acrescentando novas informações sem perder as anteriores
# format='%(levelname)s - %(message)s')  -> serve para formatar a mensagem a ser exibida

logging.basicConfig(level=logging.DEBUG, filename='app.logo', filemode='a',
                    format='%(levelname)s - %(message)s')

logging.debug("Logging no nível debur")
logging.info('Logging no nivel info')
logging.warning('logging no nível warning')
logging.error('loggin no nível error')
logging.critical('logging no nível critial')

