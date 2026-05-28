
import numpy as np
from scipy import stats

x_bar = 4
s = 1.5
n = 20
confidence = 0.90

df = n - 1

t_critical = stats.t.ppf((1 + confidence) / 2, df)

margin_of_error = t_critical * (s / np.sqrt(n))

lower_bound = x_bar - margin_of_error
upper_bound = x_bar + margin_of_error

print(f"t-critical value: {t_critical:.3f}")
print(f"Confidence Interval (90%): ({lower_bound:.2f}, {upper_bound:.2f})")



import numpy as num
import pandas as pan
import matplotlib.pyplot as mtpy
from scipy import stats

values = num.array([12, 23, 34, 45, 56, 67, 78, 89, 90, 98])
Mean_val = num.mean(values)
pop_mean = 56

t_stat, p_val = ttest_1samp(values, pop_mean)

print("Mean Value :", Mean_val, "\nStatistic :", t_stat, "\nP_Value :", p_val)

if p_val < 0.5 :
    print("Reject")
else:
    print("Accept")