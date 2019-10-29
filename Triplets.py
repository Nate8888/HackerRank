# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice+= 1
        elif b[i] > a[i]:
            bob += 1
    return [alice,bob]

print(compareTriplets([1,2,3],[3,2,1]))