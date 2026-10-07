# Sem lock o total cai; Com lock fica certo
# OpenMP

import multiprocessing as mp

N = 80_000

def sem_lock(counter):
    for _ in range(N):
        counter.value = counter.value + 1

def com_lock(counter,lock):
    for _ in range(N):
        with lock: # Exclusão mútua
            counter.value = counter.value + 1

def dois_processos(target, *extra):
    counter = mp.Value('i', 0)
    p1 = mp.Process(target=target, args=(counter,*extra))
    p2 = mp.Process(target=target, args=(counter,*extra))

    process = [p1, p2]

    for p in process:
        p.start()
    for p in process:
        p.join()

    return counter.value

if __name__ == "__main__":
    print('Valor esperado: ', 2 * N)
    print('Sem lock: ', dois_processos(sem_lock))
    print('Com lock: ', dois_processos(com_lock,mp.Lock()))
