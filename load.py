import numpy as np

x = np.load('palabras.npy')

while True:
    s = input('Texto: ')
    s = s.split(' ')

    tk = []

    for i in s:
        if (x == i).max() == False:
            tk.append('<UNK>')
        else:
            tk.append(i)

    print(tk)