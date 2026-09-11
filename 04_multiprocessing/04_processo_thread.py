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

    # Threads

    print('Threads: mesma memória (mesmo pid, ident diferente)')
    threads = [threading.Thread(target=sum_thread) for _ in range(6)]

    # start() dispara o fluxo. Não cria um novo processo no SO (irá utilizar o do main)
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print('contador na main: ', count, flush=True)


    # Processos

    print('Processos: memoria isolada (pid novo; main nao ve n)')

    queue = mp.Queue()
    n_processos = 2

    # queue, -> Tupla
    processos = [mp.Process(target=sum_process, args=(queue,)) for _ in range(n_processos)]

    for p in processos:
        p.start()

    # get(): bloqueia até que cada filho colocar o valor na variavel
    # isso é a comunicação
    resultados = [queue.get() for _ in range(n_processos)]

    for p in processos:
        p.join()

    print('contador na main: ', count, flush=True)
    print('Cada processo devolveu:', *resultados, flush=True)

