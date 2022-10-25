def banqueiro(procMax, procAlloc, recDisp):
    assert len(procMax) == len(procAlloc)
    for i in range(len(procMax)):
        assert len(procMax[i]) == len(procAlloc[i]) and len(procAlloc[i]) == len(recDisp)
    procNec = [[procMax[i][j] - procAlloc[i][j] for j in range(len(recDisp))] for i in range(len(procMax))]
    print(procNec)
    termino = [False for i in range(len(procNec))]
    i = 0
    hold = 0
    steps = 0
    while(False in termino and hold < len(procNec)):
        if(i == len(procNec)):
            i = 0
        if(termino[i]):
            print(f"({steps}, {i}) V")
            i += 1
            hold += 1
            steps += 1
            continue
        enough = True
        for j in range(len(recDisp)):
            if(recDisp[j] < procNec[i][j]):
                enough = False
                hold += 1
        if(enough):
            print(f"({steps}, {i}) C")
            termino[i] = True
            recDisp = [recDisp[j] + procAlloc[i][j] for j in range(len(recDisp))]
            hold = 0
        else:
            print(f"({steps}, {i}) P")
        i += 1
        steps += 1
    if(hold == len(procNec)):
        print("Fuleco faleceu ;-;")
    else:
        print(f"Levou {steps} passos para completar o algoritmo :)")


def main():
    print("Hi >:3")
    procMax = [
        [7,5,3],
        [3,2,2],
        [9,0,2],
        [2,2,2],
        [4,3,3]
    ]
    procAlloc = [
        [0,1,0],
        [2,0,0],
        [3,0,2],
        [2,1,1],
        [0,0,2]
    ]
    recDisp = [3,3,2]
    banqueiro(procMax, procAlloc, recDisp)

if __name__ == "__main__":
    main()
