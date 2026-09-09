# threads no MESMO processo = memória compartilhada

import threading

# multiprocessing: processos separados = memoria isolada + fila

import multiprocessing as mp
import os

count = 0

def sum_thread():
    global count
    count += 1
    print(f'[thread] pid: {os.getpid()} ident={threading.get_ident()} contador: {count}', flush = True)

def sum_process(saida):
    n = 1
    print(f'[processo] pid : {os.getpid()} n: {n} copia local de contador: {count}', flush=True)
    saida.put(n)

if __name__ == '__main__':
    print('pid da main: ',os.getpid(), flush=True)
    print(flush=True)

    saida = []

    # Threads

    print('Threads: mesma memória (mesmo pid, ident diferente)')
    t1 = threading.Thread(target=sum_thread)
    t2 = threading.Thread(target=sum_thread)
    t3 = threading.Thread(target=sum_thread)
    t4 = threading.Thread(target=sum_thread)
    t5 = threading.Thread(target=sum_thread)
    t6 = threading.Thread(target=sum_thread)

    # start() dispara o fluxo. Não cria um novo processo no SO (irá utilizar o do main)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()

    print('contador na main: ', count, flush=True)


    # Processos

    print('Processos: memoria isolada (pid novo; main nao ve n)')

    queue = mp.Queue()

    # queue, -> Tupla

    p1 = mp.Process(target=sum_process, args=(queue,))
    p2 = mp.Process(target=sum_process, args=(queue,))

    p1.start()
    p2.start()

    # get(): bloqueia até que cada filho colocar o valor na variavel
    # isso é a comunicação

    a = queue.get()
    b = queue.get()

    p1.join()
    p2.join()

    print('contador na main: ', count, flush=True)
    print('Cada processo devolveu:', a, 'e', b, flush=True)

