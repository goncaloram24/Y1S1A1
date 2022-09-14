from matplotlib import pyplot as plt
import numpy as np

friends = np.array([70, 65, 72, 63, 71, 64, 60, 64, 67])
minutes = np.array([175, 170, 205, 120, 220, 130, 105, 145, 190])
labels  = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])

plt.figure(1)
plt.scatter(friends, minutes)

# label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy=(friend_count, minute_count),   # put the label with its point
                 xytext=(5,-5),                     # but slightly offset
                 textcoords='offset points')

plt.title("Daily Minutes vs Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")

plt.figure(2)
test_1_grades = np.array([99, 90, 85, 97, 80])
test_2_grades = np.array([100, 85, 60, 90, 70])

plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes aren't comparable")
plt.xlabel("Test 1 Grades")
plt.ylabel("Test 2 Grades")

plt.show()
