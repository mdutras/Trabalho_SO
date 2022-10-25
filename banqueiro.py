from numpy import array, zeros, arange

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
    pesos = array([sum(recDisp) / (num if num else 1) for num in recDisp])
    sumM = array([sum(A * pesos) for A in procNec])
    index = arange(len(procNec))
    mergeSort(sumM, index, 0, len(procNec))
    return index

def banqueiro(procMax, procAlloc, recDisp):
    assert procMax.shape == procAlloc.shape
    assert procAlloc.shape[1] == recDisp.shape[0]
    procNec = procMax - procAlloc
    index = sortMatrix(procNec, recDisp)
    termino = zeros(len(procNec))
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


def main():
    print("Hi >:3")
    procMax = array([
        [5,1,1,7],
        [3,2,1,1],
        [3,3,2,1],
        [4,6,1,2],
        [6,3,2,5]
    ])
    procAlloc = array([
        [3,0,1,4],
        [2,2,1,0],
        [3,1,2,1],
        [0,5,1,0],
        [4,2,1,2]
    ])
    recDisp = array([0,3,0,1])
    banqueiro(procMax, procAlloc, recDisp)

if __name__ == "__main__":
    main()
