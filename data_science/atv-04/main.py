import numpy as np
from numpy.core.fromnumeric import argmax

def gerar_dados():
    x = np.arange(start=0, stop=3)
    y = np.arange(start=0, stop=3)
    z = np.arange(start=0, stop=3)

    m = np.array(np.meshgrid(x, y, z))
    mm = m.T.reshape(-1, 3)

    x1 : list = []
    x2 : list = []
    x3 : list = []

    for m in mm:
        x1.append(m[0])
        x2.append(m[1])
        x3.append(m[2])
    
    return x1, x2, x3

def step_2(x1:list, x2:list):
    
    for x in x1:
        values, counts = np.unique(x, return_counts=True)
        Ri = len(values)
        Pi = 1
        pais : list = []
        cases : list = []
        for i, value in enumerate(values):
            cases.append(counts[i])
            Pi *= np.math.factorial(counts[i])
        Pi *= (np.math.factorial(Ri-1)) / (np.math.factorial(sum(cases) + (Ri-1)))

        # while antecessores > 0 and pais <= U:
        #     pn, pai = argmax
        #     if pn > Pi:
        #         Pi = pn
        #         pais.append(pai)
        #     else:
        #         break
        # antecessores.append(x)

def main():
    # x1 : list = []
    # x2 : list = []
    # x3 : list = []
    Xs : list = []
    U : int = 0 #Número de pais que cada nó pode ter
    antecessores : list = []
    Xs = gerar_dados()

    for x in Xs:
        values, counts = np.unique(x, return_counts=True)
        Ri = len(values)
        Pi = 1
        pais : list = []
        cases : list = []
        for i, value in enumerate(values):
            cases.append(counts[i])
            Pi *= np.math.factorial(counts[i])
        Pi *= (np.math.factorial(Ri-1)) / (np.math.factorial(sum(cases) + (Ri-1)))

        while antecessores > 0 and pais <= U:
            pn, pai = argmax
            if pn > Pi:
                Pi = pn
                pais.append(pai)
            else:
                break
        antecessores.append(x)



    # print(values, counts)

if __name__ == "__main__":
    main()
