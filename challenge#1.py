
def method_1(array, k):
	taille = len(array)
	for i in range(taille):
		for j in range(i+1, taille):
			if (array[i] + array[j]) == k:
				return True
				break
			else:
				pass
		return False



def method_2(array, k):
	i = 0
	taille = len(array)
	while i < taille:
		value = abs(k - array[i])
		if (value in array) and (value != array[i]):
			return True
			break
		else:
			pass
		return False
		i += 1

if __name__ == '__main__':
	k = 17
	array = [10,15,3,7]
	print(method_1(array, k))
	print(method_2(array, k))