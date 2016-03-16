from __future__ import division
import matplotlib.pyplot as plt

def covariance(x, y):
	n = len(x)
	mean_x = sum(x) / len(x)
	mean_y = sum(y) / len(y)
	return (sum((x_i - mean_x) * (y_i - mean_y) for x_i, y_i in zip(x, y)) / (n - 1))

def variance(x):
	n = len(x)
	mean_x = sum(x) / len(x)
	return (sum(((x_i - mean_x)**2 for x_i in x)) / (n - 1))


friends = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,10]
friends_lin = [0,1,2,3,4,5,6,7,8,9,10]
beers = [
			[0, 1, 2, 2, 3, 3, 3, 4, 5, 20],
			[1, 1, 2, 3, 5, 5, 6, 7, 7, 10],
			[4, 4, 4, 6, 6, 7, 8, 8, 10, 12],
			[6, 6, 6, 7, 8, 10, 10, 13, 14, 15],
			[9, 9, 9, 12, 12, 13, 15, 16, 17, 18],
			[9, 10, 10, 12, 12, 16, 17, 19, 20, 20],
			[10, 10, 12, 13, 15, 16, 16, 19, 19, 22],
			[12, 14, 15, 15, 16, 19, 20, 20, 22, 24],
			[15, 15, 15, 19, 20, 21, 22, 24, 24, 26],
			[16, 17, 18, 19, 20, 21, 22, 23, 26, 27],
			[17, 17, 19, 20, 22, 24, 26, 26, 28, 30],
		]

if __name__ == '__main__':
	lin_beers = []

	for v_beer in beers:
		for s_beer in v_beer:
			lin_beers.append(s_beer)

	print lin_beers

	cov = covariance(friends, lin_beers)
	var_x = variance(friends)
	var_y = variance(lin_beers)
	mean_x = sum(friends) / len(friends)	
	mean_y = sum(lin_beers) / len(lin_beers)

	a = cov / (var_x)
	b = mean_y - (a * mean_x)

	print 'a: %.2f' % a
	print 'b: %.2f' % b

	y_0 = a * 0 + b
	y_10 = a * 10 + b

	plt.plot([0, 10], [y_0, y_10])
	plt.plot(friends_lin, beers, "ro")
	plt.savefig("plot_reg2")