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
    pesos = np.array([1 / (num if num else 1) for num in recDisp])
    sumM = np.array([sum(A * pesos) for A in procNec])
    index = np.arange(len(procNec))
    mergeSort(sumM, index, 0, len(procNec))
    return index

def pseudopredict(procNec, procAlloc, recDisp):
    doable = True
    tamCol = len(procAlloc)
    tamRow = len(recDisp)

    # Checar se os recursos iniciais são insuficientes pra realizar qualquer processo
    for i in range(tamCol):
        doable = True
        if sum([0 if procNec[i][j] > recDisp[j] else 1 for j in range(tamRow)]) < tamRow:
            doable = False
        if doable:
            break

    if not doable:
        return doable

    # Checar se há um processo que necessite de mais recursos que os recursos disponíveis
    colNec = np.array([[procNec[i][j] for i in range(tamCol)] for j in range(tamRow)])
    colAlloc = np.array([[procAlloc[i][j] for i in range(tamCol)] for j in range(tamRow)])
    allRec = [sum(colAlloc[i]) + recDisp[i] for i in range(tamRow)]

    for i in range(tamRow):
        if(allRec[i] < max(procNec[i])):
            doable = False
            break

    if not doable:
        return doable

    # Checar se não há um caminho que possibilite a realização da fila de processos
    index = np.arange(tamRow)
    for i in range(tamRow):
        val = recDisp[i]
        col = colNec[i]
        index = np.arange(tamCol)
        mergeSort(col, index, 0, tamCol)
        print(index, col, val)
        for j in range(tamCol):
            print(f"{val} < {col[j]} : {val < col[j]}")
            if(val < col[j]):
                doable = False
                break
            else:
                val += colAlloc[i][index[j]]
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
                if(0 not in termino or hold >= len(procNec)):
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
            print("Processo entrou em loop!")
        else:
            print(f"Levou {steps} passos para completar o algoritmo!")
    else:
        print("Não é possível processar a fila de processos!")


def main():
    print("Hi >:3")
    procMax = np.array([
        [5,1,1,7],
        [3,2,1,1],
        [3,3,2,1],
        [4,6,1,2],
        [6,3,2,5]
    ])
    procAlloc = np.array([
        [3,0,1,4],
        [2,2,1,0],
        [3,1,2,1],
        [0,5,1,0],
        [4,2,1,2]
    ])
    recDisp = np.array([1,0,0,2])
    banqueiro(procMax, procAlloc, recDisp)


if __name__ == "__main__":
    main()
