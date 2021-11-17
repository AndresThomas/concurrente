import random
import threading
import time

class Filosofo(threading.Thread):
    def __init__(self, num, tenedor):
        threading.Thread.__init__(self)
        self.tenedor = tenedor
        self.num = num
        self.temp = self.num + 1 % 5

def come(self):
    print( "El filosofo "+str(self.num)+" come ")

def piensa(self):
    print ("El filosofo "+str(self.num)+" piensa ")

def obtieneTenIzq(self):
    print( "El filosofo "+str(self.num)+" obtiene tenedor izquierdo ")
    print( "obtiene el tenedor "+str(self.num))
    self.tenedor[self.num].acquire()

def obtieneTenDer(self):
    print( "El filosofo "+str(self.num)+" obtiene tenedor derecho ")
    self.tenedor[self.temp].acquire()

def liberaTenDer(self):
    print( "El filosofo "+str(self.num)+" libera tenedor derecho ")
    self.tenedor[self.temp].release()

def liberaTenIzq(self):
    print ("El filosofo "+str(self.num)+" libera tenedor izquierdo ")
    self.tenedor[self.num].release()


def run(self):
    while(True):
        self.piensa()
        self.obtieneTenIzq()
        self.obtieneTenDer()
        self.come()
        self.liberaTenDer()
        self.liberaTenIzq()

Nfilosofos = 5

tenedor = [1,1,1,1,1]

for i in range(0, 4):
    tenedor[i] = threading.BoundedSemaphore(1)

for i in range(0, 4):
    t = Filosofo(i, tenedor)
    t.start()
    time.sleep(0.1)