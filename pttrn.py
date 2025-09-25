box = 15
for i in range(1, box + 1):
        for j in range(1, i + 1):
                print("^", end=" ")
        print()
        
'''The code in pttrn.py generates a right-angled triangle pattern using the `^` symbol. Here's how it works:

### Code Explanation:
```python
box = 15
```
- The variable `box` determines the number of rows in the triangle. In this case, the triangle will have 15 rows.

```python
for i in range(1, box + 1):
```
- This outer `for` loop iterates through the rows of the triangle. The `range(1, box + 1)` ensures that the loop runs from 1 to `box` (inclusive).

```python
    for j in range(1, i + 1):
```
- This inner `for` loop iterates through the columns of each row. The number of columns in each row is equal to the current row number (`i`).

```python
        print("^", end=" ")
```
- This prints the `^` symbol for each column in the current row. The `end=" "` ensures that the symbols are printed on the same line with a space between them.

```python
    print()
```
- This `print()` statement moves the cursor to the next line after completing the inner loop, starting a new row.

### Output:
For `box = 15`, the output will be:
```
^
^ ^
^ ^ ^
^ ^ ^ ^
^ ^ ^ ^ ^
^ ^ ^ ^ ^ ^
^ ^ ^ ^ ^ ^ ^
^ ^ ^ ^ ^ ^ ^ ^
^ ^ ^ ^ ^ ^ ^ ^ ^
^ ^ ^ ^ ^ ^ ^ ^ ^ ^
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
```

### Key Points:
- The outer loop controls the rows.
- The inner loop controls the number of symbols printed in each row.
- The `end=" "` ensures the symbols are printed on the same line, and the `print()` after the inner loop moves to the next row.'''


    

