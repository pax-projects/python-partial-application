# python-partial-application
This little function allows a partial application of Python functions by using a decorator.

## How to use it:

> First test

You can use this function with a little decorator like in the example right bellow :
```python
# Once code added
@partial
def test(a: any, b: any, c: any = None) -> tuple[any, any, any]:
    return (a, b, c)
```

The output according to the function calls bellow are :
```python
print("Test 1.0 :", test(b = 2)) # OUT : Test 1.0 : Arguments function not completed...
print("Test 1.1 :", test(1)) # OUT : Test 1.1 : Arguments function not completed...
print("Test 1.2 :", test(c = 3)) # OUT : Test 1.2 : (1, 2, 3)
print("Test 2 :", test(1, 2)) # OUT : Test 2 : Arguments function not completed...
print("Test 3 :", test(c = 10)) # OUT : Test 3 : (1, 2, 10)
print("Test 4 :", test(0, 1, 2)) # OUT : Test 4 : (0, 1, 2)
```

> Second test

The function used :
```python
@partial
def add(x, y):
    return x + y
```

The output according to the function call below is :
```python
list(map(lambda x: 1 + x, [0, 1, 2])) # OUT : [1, 2, 3]
# This is the equivalent of :
list(map(lambda x: add(1)(x), [0, 1, 2])) # OUT : [1, 2, 3]
```

## Warning !
Do not store the function in a variable, because the arguments will be used.
The following code will not work :
```python
function = add(1)
list(map(function, [0, 1, 2])) # OUT : Will not be the same as [1, 2, 3]
```
