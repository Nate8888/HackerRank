def kangaroo(x1, v1, x2, v2):
	#10 * v1 = 2 * v2
    for x in range(10000):
        if((x1+v1)==(x2+v2)):
            return "YES"
        x1+=v1
        x2+=v2
    return "NO"