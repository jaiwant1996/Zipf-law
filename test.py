import numpy as np
from numpy.polynomial.polynomial import polyfit
import matplotlib.pyplot as plt; plt.rcdefaults()
import re
import fileinput

from collections import Counter

from numpy import array



name = input("Filename: ")



words = re.findall(r'\w+', open(name).read().lower())
res = Counter(words).most_common(50)

numbers = []
labels = []
anotha = []

index = 1
for k,v in res:
    print(index,'\t\t', k,'\t\t', v)
    numbers.append(index*v)
    labels.append(index)
    anotha.append(v)
    index += 1
print(numbers)



print("type for labels: ",type(labels[0]))
print("type for anotha: ",type(anotha[0]))

print(labels)
print(anotha)
print("------")

#sampple

x = labels
y = anotha

x = array(x)
y = array(y)

# Sample data
#x = np.arange(10)
#y = 5 * x + 10

print(type(x))
print(type(y))



# Fit with polyfit
b, m = polyfit(x, y, 1)

print("type for b: ", type(b))
print("type for m: ", type(m))

plt.plot(x, y, '.')
plt.plot(x, b + m * x, '-')

plt.show()