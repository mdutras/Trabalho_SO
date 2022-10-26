import numpy as np

def mergeSort(A, index, start, end):
    if((end - start) > 1):
        mid = start + int((end - start) / 2)
        mergeSort(A, index, start, mid)
        mergeSort(A, index, mid, end)
        for i in range(start, mid):
            if(A[i] > A[mid]):
                A[i], A[mid] = A[mid], A[i]
                index[i], index[mid] = index[mid], index[i]
            for i in range(mid, end -1):
                if(A[i] > A[i+1]):
                    A[i], A[i+1] = A[i+1], A[i]
                    index[i], index[i+1] = index[i+1], index[i]
                else:
                    break

def sortMatrix(procNec, recDisp):
    pesos = np.array([sum(recDisp) / (num if num else 1) for num in recDisp])
    sumM = np.array([sum(A * pesos) for A in procNec])
    index = np.arange(len(procNec))
    mergeSort(sumM, index, 0, len(procNec))
    return index

def pseudopredict(procNec, procAlloc, recDisp):
    doable = True
    tamCol = len(procAlloc)
    tamRow = len(recDisp)
    colNec = np.array([[procNec[i][j] for i in range(tamCol)] for j in range(tamRow)])
    colAlloc = np.array([[procAlloc[i][j] for i in range(tamCol)] for j in range(tamRow)])
    for i in range(tamRow):
        index = np.arange(tamCol)
        mergeSort(colNec[i], index, 0, tamRow)
        disp = recDisp[i]
        for j in range(tamCol):
            if(disp >= colNec[i][j]):
                disp += colAlloc[i][index[j]]
            else:
                #print(f"Coluna {i} não pôde ser processada")
                doable = False
                break
        if not doable:
            break
    return doable

def banqueiro(procMax, procAlloc, recDisp):
    assert procMax.shape == procAlloc.shape
    assert procAlloc.shape[1] == recDisp.shape[0]
    procNec = procMax - procAlloc
    if(pseudopredict(procNec, procAlloc, recDisp)):
        index = sortMatrix(procNec, recDisp)
        termino = np.zeros(len(procNec))
        hold = 0
        steps = 0
        print(" p  i")
        while(0 in termino and hold < len(procNec)):
            for i in index:
                if(0 not in termino or hold >= len(procNec)): #!TODO: Tentar um jeito melhor de fazer isso
                    break
                steps += 1
                if(termino[i]):
                    hold += 1
                    print(f"({steps}, {i}) V {hold}")
                    i += 1
                    continue
                if( all(recDisp[j] >= procNec[i][j] for j in range(len(recDisp))) ):
                    print(f"({steps}, {i}) C")
                    termino[i] = 1
                    recDisp = recDisp + procAlloc[i]
                    hold = 0
                else:
                    hold += 1
                    print(f"({steps}, {i}) P {hold}")
        if(hold >= len(procNec)):
            print("Fuleco faleceu ;-;")
        else:
            print(f"Levou {steps} passos para completar o algoritmo :)")
    else:
        print("Não é possível processar a fila de processos")


def main():
    print("Hi >:3")
    procMax = np.array([
        [4,2,1,2],
        [5,2,5,2],
        [2,3,1,6],
        [1,4,2,4],
        [3,6,6,5]
    ])
    procAlloc = np.array([
        [2,0,0,1],
        [3,1,2,1],
        [2,1,0,3],
        [1,3,1,2],
        [1,4,3,2]
    ])
    recDisp = np.array([3,3,2,1])
    #procNec = procMax - procAlloc
    #print(procNec)
    banqueiro(procMax, procAlloc, recDisp)
    #pseudopredict(procNec, procAlloc, recDisp)


if __name__ == "__main__":
    main()
