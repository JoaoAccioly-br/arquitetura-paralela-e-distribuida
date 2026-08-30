import threading
import time

def mensagem():
    time.sleep(0.5)
    print('teste 01 - executando em paralelo')

def mensagem2():
    time.sleep(5)
    print('teste 03 - executando em paralelo')

if __name__ == "__main__":
    print('objetivo - exibir duas mensagens em paralelo')
    t = threading.Thread(target=mensagem, name='worker')
    t.start();

    t2 = threading.Thread(target=mensagem2, name='worker2')
    t2.start()

    print('main - teste02 - sem esperar a thread')

    t.join()
    t2.join()

    print('fim')