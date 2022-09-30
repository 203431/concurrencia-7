import threading
mutex = threading.Lock()
def crito(id):
    global x;
    x = x + id
    print("La persona: "+str(id)+ " Tiene ambos palillos y empieza a comer")
    if(id==8):
        print("La persona: "+str(id-7)+" " +"Esta esperando")
    else: print("La persona: "+str(x)+" " +"Esta esperando")
    if(id==8):
        print("La persona: "+str(id)+" terminó de comer y dió su palillo a la persona: "+str(x-8))
    else: print("La persona: "+str(id)+" terminó de comer y dió su palillo a la persona: "+str(x))
    x=1

class Hilo(threading.Thread):
     def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id

     def run(self):
        mutex.acquire() #Inicializa semáforo , lo adquiere
        crito(self.id)
        mutex.release() #Libera un semáforo e incrementa la varibale

hilos = [Hilo(1), Hilo(2), Hilo(3), Hilo(4), Hilo(5), Hilo(6), Hilo(7),Hilo(8)]
x=1;
for h in hilos:
    h.start()