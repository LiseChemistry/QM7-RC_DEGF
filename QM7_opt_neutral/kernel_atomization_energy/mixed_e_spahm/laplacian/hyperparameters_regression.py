#!/usr/bin/env python3

import re
import os
import numpy as np
from sklearn.model_selection import train_test_split
from qstack.regression.kernel_utils import defaults
from qstack.regression import hyperparameters
from qstack.regression import regression
import sys

seed = int(sys.argv[1])

base_path = os.path.dirname(os.path.realpath(__file__))
results_dir = os.path.join(base_path, "results")

X = np.load(f"data_e_spahm.npy")
y = np.loadtxt(f"./Atomization_en.txt")

hyperparams = hyperparameters.hyperparameters(X, y, akernel="myLfast", random_state=seed, adaptive=True)
print(f"Hyperparameters for split_{seed}: {hyperparams}")
hyperparameters_file = os.path.join(results_dir, f'myLfast_hyperparam_split_{seed}.txt')
np.savetxt(hyperparameters_file, np.array(hyperparams))

min_index = np.argmin(hyperparams[:, 0])
min_eta = float(hyperparams[min_index, 2])
min_sigma = float(hyperparams[min_index, 3])
print(f"min_eta: {min_eta}, min_sigma: {min_sigma}")

regression_results_file = os.path.join(results_dir, f'myLfast_regression_split_{seed}.txt')
target_predicted_file = os.path.join(results_dir, f'myLfast_target_pred_split_{seed}.txt')
mae_file = os.path.join(results_dir, f'myLfast_MAE_split_{seed}.txt')

regression_results = regression.regression(X, y, read_kernel=False, sigma=min_sigma, eta=min_eta, akernel="myLfast", random_state=seed, n_rep=1, save_pred=True)
print(f"Regression results for split_{seed}: {regression_results}")
regression_array = np.array(regression_results, dtype=object)

results, (target_values, predicted_values) = regression_results
data = np.column_stack((target_values, predicted_values))
np.savetxt(target_predicted_file, data, fmt='%s', delimiter="\t", comments='')

first_line = str(regression_array[0])
cleaned_line = re.sub(r'[^\d.,-]', '', first_line)
mae_values = cleaned_line.split(',')
mae_values = [float(value.strip()) for value in mae_values]
mae_values = np.array(mae_values).reshape(-1, 3)
np.savetxt(mae_file, mae_values)

print("All calculations are completed.")
