def prod(array):
	mult = 1
	taille = len(array)
	for i in range(taille):
		mult *= array[i]
	return mult


def method_1(array):
	return [prod(array) // i for i in array]


if __name__ == '__main__':
	array = [1,2,3,4,5]
	print(method_1(array))