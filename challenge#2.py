def prod(array):
	mult = 1
	taille = len(array)
	for i in range(taille):
		mult *= array[i]
	return mult


def method_1(array):
	product = prod(array)
	return [product // i for i in array]

def method_2(array):
	new_array = []
	taille = len(array)
	for i in range(taille):
		second_array = list(array)
		second_array.pop(i)
		product = prod(second_array)
		new_array.append(product)
	return new_array


if __name__ == '__main__':
	test_array = [1,2,3,4,5]
	expected_array = [120, 60, 40, 30, 24]
	assert method_1(test_array) == expected_array
	assert method_2(test_array) == expected_array