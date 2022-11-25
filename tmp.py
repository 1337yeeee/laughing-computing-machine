import numpy as np

# dem = [3, 2, 3, 2]
# x = [1, 2, 4]
# w = [
# 	[[1, 2], [4, 2], [1, 4]],
# 	[[4, 2, 5], [1, 7, 9]],
# 	[[6, 2], [5, 1], [4, 2]],
# ]
# b = [1, 3, 2]

# dem = [2, 2, 1]
# x = [1, 2]
# w = [
# 	[[1, 4], [2, 3]],
# 	[[6], [1]]
# ]
# b = [[2, 1], [3]]
# y = [1]


def fun(x, w, b):
	dem = [len(x)]
	for i in w:
		dem.append(len(i[0]))

	x_s = []
	for k in range(len(dem) - 1):
		pre_j = []
		for j in range(dem[k + 1]):
			pre_result = 0
			for i in range(dem[k]):
				if k != 0:
					try:
						pre_result += x_s[k-1][i] * w[k][i][j]
					except:
						print(i, j, k)
				else:
					pre_result += x[i] * w[k][i][j]

			pre_result += b[k][j]
			pre_j.append(pre_result)

		x_s.append(pre_j)

	return x_s[-1]


def viz(dem: list[int]):
	x_s = []
	# for am_y in range(dem[-1]):
	for k in range(len(dem)-1):
		pre_j = []
		for j in range(dem[k+1]):
			pre_result = ''
			for i in range(dem[k]):
				if k != 0:
					pre_result += f'({x_s[k-1][i]}) * w{k+1}{i+1}{j+1} + '
				else:
					pre_result += f'x{i+1} * w{k+1}{i+1}{j+1} + '

			pre_result += f'b{k+1}{j+1}'
			pre_j.append(pre_result)

		x_s.append(pre_j)

	for i in x_s[-1]:
		print(i)
		print('\n')


def gradient(x, w, b, y):
	dem = [len(x)]
	for i in w:
		dem.append(len(i[0]))

	value_of_f = fun(x, w, b)

	def some(k_, m_, j_, L, l=len(dem)-2):
		summa = 0

		if l - L > 2:
			for i in range(dem[l]):
				summa += w[l][i][k_] * some(i, m_, j_, L, l-1)

		elif l - L == 2:
			for i in range(dem[L+2]):
				if L != 0:
					summa += w[L+2][i][k_] * w[L+1][j_][i] * fun(x, w[:L], b[:L])[m_]
				else:
					summa += w[L + 2][i][k_] * w[L + 1][j_][i] * x[m_]

		print(f'summa = {summa}, k_ = {k_}, m_ = {m_}, j_ = {j_}, L = {L}, l = {l}')
		return summa

	print(some(0, 0, 0, 0))


	# ans = [[[0 for i in range(dem[k+1])] for j in range(dem[k])] for k in range(len(dem)-1)]


	# for iter_y in range(dem[-1]):
	# 	loss = (value_of_f[iter_y] - y[iter_y]) ** 2
	# 	for L in range(len(dem)-1, 0, -1):
	# 		for j in range(dem[L]):
	# 			for i in range(dem[L-1]):
	# 				# if L == len(dem)-1:
	# 				# 	ans[L][i][iter_y] = 0
	# 				# else:
	# 				ans[L][i][j] = 0

# dem = [2, 3, 2, 3, 2]
x = [2, 3]

w = [
	[[3, 3, 3], [2, 2, 2]],
	[[2, 2], [3, 3], [4, 4]],
	[[5, 4, 6], [2, 3, 3]],
	[[4, 1], [4, 2], [7, 3]]
]

b = [
	[4, 3, 1],
	[0, 0],
	[6, 3, 2],
	[1, 3]
]

y = [5, 2]


if __name__ == '__main__':
	# viz([2, 3, 2, 3, 2])
	# print(fun(x, w, b))
	gradient(x, w, b, y)
	
	pass

