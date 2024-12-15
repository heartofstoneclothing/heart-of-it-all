
```python
import numpy as np
A = np.array([
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
])

print(A[:, :2])
```
---
```python
import pandas as pd

certificates_earned = pd.Series(
    [8, 2, 5, 6],
    index=['Tom', 'Kris', 'Ahmad', 'Beau']
)

print(certificates_earned)
print(certificates_earned[certificates_earned > 5])
```
---
```python
import pandas as pd

certificates_earned = pd.DataFrame({
    'Certificates': [8, 2, 5, 6],
    'Time (in months)': [16, 5, 9, 12]
})

certificates_earned.index = ['Tom', 'Kris', 'Ahmad', 'Beau']

print(certificates_earned.iloc[2])
```
---
```python
import pandas as pd

certificates_earned = pd.DataFrame({
    'Certificates': [8, 2, 5, 6],
    'Time (in months)': [16, 5, 9, 12]
})
names = ['Tom', 'Kris', 'Ahmad', 'Beau']

certificates_earned.index = names
longest_streak = pd.Series([13, 11, 9, 7], index=names)
certificates_earned['Longest streak'] = longest_streak

print(certificates_earned)
```
---
```python
import pandas as pd
import numpy as np

s = pd.Series(['a', 3, np.nan, 1, np.nan])

print(s.notnull().sum())
```
---
```python
import math

# Calculate the number of routes
routes = math.comb(40, 20)
print(routes)
```
---
```python
# Calculate 2^1000
number = 2**1000

# Convert the number to a string to extract the digits
digits = str(number)

# Sum the digits
digit_sum = sum(int(digit) for digit in digits)

# Print the result
print(digit_sum)
```
---
```python
a = np.ones((2, 4))
b = a.reshape((4, 2))
print(b)

a = np.ones((2, 4))
b = a.reshape((2, 4))
print(b)

a = np.ones((2, 4))
b = a.reshape((8, 1))
print(b)
```
---
```python
b = np.array([[1.0,2.0,3.0],[3.0,4.0,5.0]])
print(b)
```
---
```python
import pandas as pd
import numpy as np

s = pd.Series([np.nan, 1, 2, np.nan, 3])
s = s.fillna(method='ffill')

print(s)
```
---
