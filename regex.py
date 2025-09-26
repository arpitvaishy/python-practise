import re

pattern = r'^[+-]?(\d*\.\d+|\d+\.\d*)$'

T = int(input())
for _ in range(T):
    s = input()
    print(bool(re.match(pattern, s)))

'''The code in regex.py checks whether a given string represents a valid floating-point number. Here's a detailed explanation:

### Code Breakdown:
```python
import re
```
- The `re` module is imported to use regular expressions for pattern matching.

---

```python
pattern = r'^[+-]?(\d*\.\d+|\d+\.\d*)$'
```
- This is the regular expression pattern used to validate floating-point numbers.
- **Explanation of the pattern**:
  - `^`: Matches the start of the string.
  - `[+-]?`: Matches an optional `+` or `-` sign.
  - `(\d*\.\d+|\d+\.\d*)`: Matches a floating-point number:
    - `\d*`: Matches zero or more digits before the decimal point.
    - `\.`: Matches the decimal point.
    - `\d+`: Matches one or more digits after the decimal point.
    - `|`: OR operator, allowing the decimal point to appear after digits as well.
    - `\d+\.\d*`: Matches one or more digits before the decimal point and zero or more digits after.
  - `$`: Matches the end of the string.

---

```python
T = int(input())
```
- Reads an integer `T` from the user, representing the number of test cases.

---

```python
for _ in range(T):
    s = input()
    print(bool(re.match(pattern, s)))
```
- Loops `T` times to process each test case:
  - `s = input()`: Reads a string `s` from the user.
  - `re.match(pattern, s)`: Checks if the string `s` matches the regular expression `pattern`.
  - `bool()`: Converts the result of `re.match` to `True` or `False`.
  - `print()`: Prints `True` if the string is a valid floating-point number, otherwise `False`.

---

### Example:
#### Input:
```
3
4.0
-1.23
abc
```

#### Execution:
1. For `4.0`:
   - Matches the pattern.
   - Output: `True`.

2. For `-1.23`:
   - Matches the pattern.
   - Output: `True`.

3. For `abc`:
   - Does not match the pattern.
   - Output: `False`.

#### Output:
```
True
True
False
```

Let me know if you need further clarification!'''