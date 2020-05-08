#! coding:utf-8

"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

import re

mapping = dict(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10, k=11, l=12, m=13, n=14, o=15, p=16, q=17, r=18, s=19, t=20, u=21, v=22, w=23, x=24, y=25, z=26)

"""
message = '111'
fem = int(message)
print(int(message[0]+message[1]))
"""
		

def decode_number(message):
	nbre = 1
	taille = len(message)
	ex_1 = r"^0[0-9]*$"
	ex_2 = r"^[0-9]*[03-9][0]+$"
	if (re.match(ex_1, message) or re.match(ex_2, message)):
		return print(f'{message} n\'est pas autorisé')
	else:
		for i in range(taille-1):
			if int(message[i] + message[i+1]) in mapping.values():
				nbre += 1
		return print(nbre)

if __name__ == '__main__':
	# 1er test
	message = '111'
	decode_number(message)

	# 2e test
	message = '100'
	decode_number(message)