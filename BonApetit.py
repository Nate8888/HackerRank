def bonAppetit(bill, k, b):
	bActual = sum([bill[i] for i in range(len(bill)) if i!=k])/2
	if b > bActual:
		print(int(b-bActual))
	else:
		print("Bon Appetit")


print(bonAppetit([1,2,3],2,10))