from matplotlib import pyplot as plt
import random
from collections import Counter
import math
import numpy as np

MAX_FRIENDS = 100
MAX_MINUTES = 90
NUM_USERS = 500

num_friends = []
daily_minutes = []
for k in range(0,NUM_USERS):
    #n = random.randint(0,100)
    if k != NUM_USERS-1:
        m = -1
        while m < 0 or m > MAX_FRIENDS:
            m = int(random.gauss(5, 5))

        n = -1
        while n < 0 or n > MAX_MINUTES:
            n = int(random.gauss(m, 10))

    else:
        print("here")
        m = MAX_FRIENDS-2
        n = 0

    num_friends.append(m)
    daily_minutes.append(n)

plt.figure(1)
friend_counts = Counter(num_friends)
xs = range(MAX_FRIENDS+1)                         # largest value is 100
ys = [friend_counts[x] for x in xs]     # height is just # of friends
plt.bar(xs, ys)
plt.axis([0, MAX_FRIENDS+1, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")

# some basic statistics
num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)
sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]
print("num_points: ", num_points)
print("largest_value: ", largest_value)
print("smallest_value: ", smallest_value)
print("sorted_values: ", sorted_values)
print("second_smallest_value: ", second_smallest_value)
print("second_largest_value: ", second_largest_value)

# functions with more advanced statistics
def mean(x):
    return sum(x)/len(x)

print("mean: ", mean(num_friends))

def median(x):
    """finds the 'middle-most' value of x"""
    n = len(x)
    sorted_x = sorted(x)
    midpoint = n // 2

    if n % 2 == 1:
        # if odd, return the middle value
        return sorted_x[midpoint]
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_x[lo] + sorted_x[hi]) / 2

print("median: ", median(num_friends))

def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

print("quantile(0.10): ", quantile(num_friends, 0.10))
print("quantile(0.25): ", quantile(num_friends, 0.25))
print("quantile(0.75): ", quantile(num_friends, 0.75))
print("quantile(0.90): ", quantile(num_friends, 0.90))
print("quantile(0.95): ", quantile(num_friends, 0.95))
print("quantile(0.99): ", quantile(num_friends, 0.99))
print("quantile(0.995): ", quantile(num_friends, 0.995))

def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]

print("mode: ", mode(num_friends))

# "range" already means something in Python, so we'll use a different name
def data_range(x):
    return max(x) - min(x)

print("data_range: ", data_range(num_friends))

def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    squared_deviations = [dev_i**2 for dev_i in deviations]
    return sum(squared_deviations) / (n - 1)

print("variance: ", variance(num_friends))


def standard_deviation(x):
    return math.sqrt(variance(x))

print("standard_deviation. ", standard_deviation(num_friends))


def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, .25)

print("interquantile_range: ", interquartile_range(num_friends))


def covariance(x, y):
    n = len(x)
    return np.dot(de_mean(x), de_mean(y)) / (n - 1)

print("covariance: ", covariance(num_friends, daily_minutes))


def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0    # if no variation, correlation is zero

print("correlation: ", correlation(num_friends, daily_minutes))

plt.figure(2)
plt.scatter(num_friends, daily_minutes)
plt.xlabel("# of friends")
plt.ylabel("minutes per day")
plt.title("Correlation with an Outlier")

outlier = num_friends.index(MAX_FRIENDS-2)  # index of outlier

num_friends_good = [x
                    for i, x in enumerate(num_friends)
                    if i != outlier]

daily_minutes_good = [x
                      for i, x in enumerate(daily_minutes)
                      if i != outlier]

print("correlation_good: ", correlation(num_friends_good, daily_minutes_good))

plt.figure(3)
plt.scatter(num_friends_good, daily_minutes_good)
plt.xlabel("# of friends")
plt.ylabel("minutes per day")
plt.title("Correlation after removing the Outlier")
plt.axis([0, 40, 0, 50])

plt.show()

