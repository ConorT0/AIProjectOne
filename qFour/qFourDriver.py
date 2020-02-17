import fireStratOne
import fireStratTwo
import fireStratThree
import matplotlib
import numpy
import copy
import collections
import sys
import pandas

if __name__ == "__main__":
	# q = 0, 0.1, 0.2, ..., 1.0
	fire_probabilities = numpy.arange(0, 1.1, 0.1)
	P0 = 0.2
	DIM = 10
	NUM_RUNS = 100

	strategies = {
		"fireStratOne": {
			"class": fireStratOne.FireStratOne,
			"average_successes": dict(),
			"successes": list()
		},
		"fireStratTwo": {
			"class": fireStratTwo.FireStratTwo,

			"average_successes": dict(),
			"successes": list()
		},
		"fireStratThree": {
			"class": fireStratThree.FireStratThree,
			"average_successes": dict(),
			"successes": list()
		}
	}

	nr = 0
	for q in fire_probabilities:
		for strat in strategies:

			f = strategies[strat]["class"](DIM, P0, q)
			success_count, fail_count = 0, 0

			# make 1000 mazes for each strat and get the average success fail
			for i in range(0, NUM_RUNS):
				nr += 1
				sys.stdout.write('\r' + str(nr))
				sys.stdout.flush()

				path = f.walk_fire_maze()
				if (path[-1][0], path[-1][1]) == (DIM - 1, DIM - 1):
					# success
					success_count += 1
				else:
					fail_count += 1
				f.clear_grid()
				f.generateGrid()

			# averaged over 1000
			strategies[strat]["average_successes"][q] = float(success_count) / float(NUM_RUNS)
			strategies[strat]["successes"].append(success_count)

	print(strategies)

	df = pandas.DataFrame({'Fire Probability': fire_probabilities,
	                   'Strategy 1': list(strategies["fireStratOne"]["average_successes"].values()),
	                   'Strategy 2': list(strategies["fireStratTwo"]["average_successes"].values()),
	                   'Strategy 3': list(strategies["fireStratThree"]["average_successes"].values())})

	matplotlib.pyplot.plot('Fire Probability', 'Strategy 1', data=df, color='skyblue')
	matplotlib.pyplot.plot('Fire Probability', 'Strategy 2', data=df, color='olive')
	matplotlib.pyplot.plot('Fire Probability', 'Strategy 3', data=df, color='orange')
	matplotlib.pyplot.legend()

	matplotlib.pyplot.show()
