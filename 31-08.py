import threading

def firstPart(x):
    results['first'] = x**2 + 3

def secondPart():
    results['second'] = 36 / 4

if __name__ == "__main__":

    num = int(input('Insert a number: '))

    results = {};

    first = threading.Thread(target=firstPart(num), name='first')
    second = threading.Thread(target=secondPart, name='second')

    first.start()
    second.start()

    first.join()
    second.join()
    
    result = results['first'] * 7 - results['second']

    print(result);