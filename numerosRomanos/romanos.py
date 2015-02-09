'''
Created on 8/2/2015

@author: Jonnathan
'''
def convertirRomano(numero):
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    entero = 0
    for i in range(len(numero)):
        entero = entero + romanos[numero[i]] 
    return entero






if __name__ == '__main__':
    pass