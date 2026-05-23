import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# PROBABILITY THEORY

# Probability tells how likely an event is to happen

# Example:
# Probability of getting HEAD in a coin toss = 0.5

# In Data Science:
# Probability is used to:
# - Predict patterns
# - Understand uncertainty
# - Make decisions


# PDF - PROBABILITY DENSITY FUNCTION

# PDF = Probability Density Function

# PDF tells:
# How data is distributed over different values

# Higher PDF value means:
# That value is more likely to occur

# Important:
# PDF itself is NOT probability
# Area under the PDF curve gives probability


# GENERATING NORMAL DISTRIBUTION

# Mean represents average value
mean = 70

# Standard deviation represents spread of data
std_dev = 10

# Generate x-axis values from 30 to 110
x = np.linspace(30, 110, 500)

# Generate PDF values using normal distribution
pdf = norm.pdf(x, mean, std_dev)


# PLOT PDF

plt.figure(figsize=(10, 5))
plt.plot(x, pdf)
plt.title("PDF - Normal Distribution")
plt.xlabel("Marks")
plt.ylabel("Density")
plt.grid(True)
plt.show()


# PDF OBSERVATION

# Peak of the curve shows most common marks

# Most students score near average marks

# Very low and very high marks are rare


# CDF - CUMULATIVE DISTRIBUTION FUNCTION

# CDF = Cumulative Distribution Function

# CDF tells:
# Probability that a value is
# less than or equal to a specific value

# Example:
# Probability that student scored <= 80 marks

# CDF values always increase from 0 to 1


# GENERATE CDF

# Generate cumulative probabilities
cdf = norm.cdf(x, mean, std_dev)


# PLOT CDF

plt.figure(figsize=(10, 5))
plt.plot(x, cdf)
plt.title("CDF - Cumulative Distribution")
plt.xlabel("Marks")
plt.ylabel("Cumulative Probability")
plt.grid(True)
plt.show()


# CDF OBSERVATION

# CDF starts near 0 and ends near 1

# It accumulates probabilities step-by-step

# Example:
# If CDF at 80 = 0.84
# It means 84% students scored 80 or below


# PDF vs CDF

# PDF:
# - Shows density/distribution
# - Used to understand shape of data
# - Area gives probability

# CDF:
# - Shows cumulative probability
# - Used to find probability up to a value
# - Always increases from 0 to 1


# REAL-TIME EXAMPLE

# Scenario:
# A school wants to analyze student marks

# Find probability that student scored <= 80
probability_80 = norm.cdf(80, mean, std_dev)

# Example result:
# 0.84 means
# 84% students scored 80 or below


# PROBABILITY BETWEEN TWO VALUES

# Find probability between 60 and 80
prob_between = norm.cdf(80, mean, std_dev) - norm.cdf(60, mean, std_dev)

# Example result:
# 0.68 means
# 68% students scored between 60 and 80


# PDF helps us understand:
# WHERE data is concentrated

# CDF helps us understand:
# HOW MUCH probability is accumulated

# These concepts are heavily used in:
# - Machine Learning
# - AI
# - Data Analysis
# - Risk Analysis
# - Finance
# - Medical Predictions
# - Weather Forecasting



# NORMAL DISTRIBUTION AND BINOMIAL DISTRIBUTION
# EXPLANATION USING COMMENTS ONLY

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom

# NORMAL DISTRIBUTION

# Normal Distribution is also called Gaussian Distribution

# It is used when:
# - Data is continuous
# - Data is naturally distributed around an average
# - Examples:
#   height, weight, marks, salary, temperature

# Important Terms:
# mean      -> center of data
# std_dev   -> spread of data

mean = 70
std_dev = 10

# Generate x-axis values
x = np.linspace(30, 110, 500)

# Generate PDF values
pdf = norm.pdf(x, mean, std_dev)

# norm.pdf()
# pdf = Probability Density Function
# Shows how data is distributed

plt.figure(figsize=(10,5))
plt.plot(x, pdf)

plt.title("Normal Distribution - PDF")
plt.xlabel("Marks")
plt.ylabel("Density")

plt.grid(True)
plt.show()

# NORMAL DISTRIBUTION CDF

# norm.cdf()
# CDF = Cumulative Distribution Function

# It calculates probability up to a value

cdf = norm.cdf(x, mean, std_dev)

plt.figure(figsize=(10,5))
plt.plot(x, cdf)

plt.title("Normal Distribution - CDF")
plt.xlabel("Marks")
plt.ylabel("Cumulative Probability")

plt.grid(True)
plt.show()

# REAL EXAMPLE

# Probability student scores <= 80

probability = norm.cdf(80, mean, std_dev)

# This gives probability of scoring
# less than or equal to 80


# BINOMIAL DISTRIBUTION

# Binomial Distribution is used when:
# - Only two outcomes exist
# - Success or Failure
# - Yes or No
# - Head or Tail

# Examples:
# - Tossing a coin
# - Pass or Fail
# - Product Defective or Not

# Important Terms:
# n -> number of trials
# p -> probability of success

n = 10
p = 0.5

# Generate x values
x = np.arange(0, n + 1)

# Calculate probability values
binomial_pmf = binom.pmf(x, n, p)

# binom.pmf()
# PMF = Probability Mass Function
# Used for discrete values

plt.figure(figsize=(10,5))
plt.bar(x, binomial_pmf)

plt.title("Binomial Distribution - PMF")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")

plt.grid(True)
plt.show()

# BINOMIAL DISTRIBUTION CDF

binomial_cdf = binom.cdf(x, n, p)

# binom.cdf()
# Calculates cumulative probability

plt.figure(figsize=(10,5))
plt.plot(x, binomial_cdf, marker='o')

plt.title("Binomial Distribution - CDF")
plt.xlabel("Number of Successes")
plt.ylabel("Cumulative Probability")

plt.grid(True)
plt.show()

# REAL EXAMPLE

# Example:
# Toss a coin 10 times
# Find probability of getting exactly 6 heads

exact_6 = binom.pmf(6, n, p)

# Example:
# Find probability of getting
# 6 or fewer heads

less_than_6 = binom.cdf(6, n, p)

