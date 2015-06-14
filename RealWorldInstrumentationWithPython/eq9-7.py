Kp = 1.0
Kb = 1.0
P = 0

rinput = 0
cinput = 1

def Acquire(port):
    return 1

def PControl():
    rval = Acquire(rinput)
    bval = Acquire(cinput)*Kb
    eval = rval - bval
    return (Kp*eval) + P
