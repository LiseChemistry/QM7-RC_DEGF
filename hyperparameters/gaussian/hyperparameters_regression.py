#!/usr/bin/env python3

import os
import numpy as np
from sklearn.model_selection import train_test_split
from qstack.regression.kernel_utils import defaults
from qstack.regression import hyperparameters
from qstack.regression import regression
import sys

atom = sys.argv[1]
rep = sys.argv[2]
seed = int(sys.argv[3])

base_path = os.path.dirname(os.path.realpath(__file__))
results_dir = os.path.join(base_path, "results")

X = np.load(f"{atom}_{rep}.npy")
y = np.loadtxt(f"/home/student/MasterProject_SPAHM-ENN/charges/{atom}_charges.txt")

hyperparams = hyperparameters.hyperparameters(X, y, akernel="G", random_state=seed)

print(f"Hyperparameters for {atom}_{rep}_split_{seed}: {hyperparams}")

hyperparameters_file = os.path.join(results_dir, f'gaussian_hyperparam_{atom}_{rep}_split_{seed}.txt')
np.savetxt(hyperparameters_file, np.array(hyperparams))
print(hyperparams)
min_index = np.argmin(hyperparams[:, 0])

min_eta = float(hyperparams[min_index, 2])
min_sigma = float(hyperparams[min_index, 3])

print(f"min_eta: {min_eta}, min_sigma: {min_sigma}")

regression_results = regression.regression(X, y, read_kernel=False, sigma=min_sigma, eta=min_eta, akernel="G", random_state=seed)

print(f"Regression results for {atom}_{rep}_split_{seed}: {regression_results}")

regression_results_file = os.path.join(results_dir, f'gaussian_regression_{atom}_{rep}_split_{seed}.txt')
np.savetxt(regression_results_file, np.array(regression_results))

print("All calculations are completed.")
