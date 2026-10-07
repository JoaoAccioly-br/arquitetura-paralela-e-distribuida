# Troca de mensagens (Padrão MPI)

from multiprocessing import Process, Queue

def worker(entra,sai):
    # Recv (receber)
    # get(): espera até chegar uma mensagem na fila "entra"

    msg = entra.get()

    # put(): coloca a resposta na fila 'sai'
    # Equivale a ideia de Send (enviar)

    sai.put('eco:' + msg)

if __name__ == "__main__":
    entra , sai = Queue(), Queue()

    p = Process(target=worker,args=(entra,sai))
    p.start()

    entra.put('Olá')
    print(sai.get())

    p.join()