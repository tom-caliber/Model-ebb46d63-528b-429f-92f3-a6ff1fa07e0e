'''
A starter's dataset generated for playing with linear regression.
# Tags: Adoption; GetStarted; LinearRegressionData
'''

from sygmoid.imports import *

n_samples = 1000
with open('01-dummy-lr-data.csv', 'w') as f:
    X = np.random.uniform(low=0, high=100, size=n_samples)
    Y = 3*X + 5 + np.random.normal(scale=7, size=n_samples)
    for i in range(n_samples):
        f.write("%s,%s\n" % (X[i], Y[i]))