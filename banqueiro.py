def banqueiro(procMax, procAlloc, recDisp):
    assert len(procMax) == len(procAlloc)
    for i in range(len(procMax)):
        assert len(procMax[i]) == len(procAlloc[i]) and len(procAlloc[i]) == len(recDisp)
    procNec = [[procMax[i][j] - procAlloc[i][j] for j in range(len(recDisp))] for i in range(len(procMax))]
    termino = [False for i in range(procNec)]
    i = 0
    hold = 0
    steps = 0
    while(False in termino and hold < len(procNec)):
        if(i == len(procNec)):
            i = 0
        if(termino[i]):
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
            termino[i] = True
            recDisp = [recDisp[j] + procAlloc[i][j] for j in range(recDisp)]
            hold = 0
        i += 1
        steps += 1
    if(hold == len(procNec)):
        print("Fuleco faleceu ;-;")
    else:
        print(f"Levou {steps} passos para completar o algoritmo :)")


def main():
    print("Hi >:3")

if __name__ == "__main__":
    main()
