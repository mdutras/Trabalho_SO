from numpy import array, zeros

def banqueiro(procMax, procAlloc, recDisp):
    assert procMax.shape == procAlloc.shape
    assert procAlloc.shape[1] == recDisp.shape[0]
    procNec = procMax - procAlloc
    # print(procNec)
    termino = zeros(len(procNec))
    i = 0
    hold = 0
    steps = 0
    print(" p  i")
    while(0 in termino and hold < len(procNec)):
        steps += 1
        if(i == len(procNec)):
            i = 0
        if(termino[i]):
            print(f"({steps}, {i}) V")
            hold += 1
            i += 1
            continue
        if( all(recDisp[j] >= procNec[i][j] for j in range(len(recDisp))) ):
            print(f"({steps}, {i}) C")
            termino[i] = 1
            recDisp = recDisp + procAlloc[i]
            hold = 0
        else:
            hold += 1
            print(f"({steps}, {i}) P")
        i += 1
    if(hold == len(procNec)):
        print("Fuleco faleceu ;-;")
    else:
        print(f"Levou {steps} passos para completar o algoritmo :)")


def main():
    print("Hi >:3")
    procMax = array([
        [7,5,3],
        [3,2,2],
        [9,0,2],
        [2,2,2],
        [4,3,3]
    ])
    procAlloc = array([
        [0,1,0],
        [2,0,0],
        [3,0,2],
        [2,1,1],
        [0,0,2]
    ])
    recDisp = array([3,3,2])
    banqueiro(procMax, procAlloc, recDisp)

if __name__ == "__main__":
    main()
