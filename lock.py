import threading
from threading import Lock

class CuentaBanco():
    def __init__(self,id,amount):
        self.id = id
        self.amount = amount
        self.lock = Lock()

    def deposit(self,mount):
        self.amount = self.amount + mount

    def transfer(self,to,mount):
        if self.id != to.id:
            if self.amount > mount :
                if to.lock.acquire() and self.lock.acquire():
                    to.deposit(mount)
                    self.amount = self.amount - mount
                    to.lock.release()
                    self.lock.release()
                    print(self.id + " tiene ",self.amount, to.id+" tiene",to.amount)
            else:
                raise Exception("No cuentas con suficiente saldo")
        else:
            raise Exception("No puedes transferirte dinero a ti mismo")

p1 = CuentaBanco("p1",10000)
p2 = CuentaBanco("p2",26000)
p3 = CuentaBanco("p3",50000)

t1 = threading.Thread(name="t1",target=p1.transfer,args=(p2,200))
t2 = threading.Thread(name="t2",target=p2.transfer,args=(p1,5000))
t3 = threading.Thread(name="t3",target=p1.transfer,args=(p3,2000))
t4 = threading.Thread(name="t4",target=p3.transfer,args=(p1,20000))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()