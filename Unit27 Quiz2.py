import pickle
with open('words.txt', 'r') as file:
    line = None
    while line != ',.':
        line = file.readline()
        print(line.strip('\n'))