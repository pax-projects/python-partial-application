# python-partial-application
This little function allows a partial application of Python functions by using a decorator.

# How to use it:
You can use this function with a little decorator like in the example right bellow :
```python
# Once code added
@partial
def test(a: any, b: any, c: any = None) -> tuple[any, any, any]:
    return (a, b, c)
```

The output according to the functio calls bellow are :
```
print("Test 1.0 :", test(b = 2)) # OUT : Test 1.0 : Arguments function not completed...
print("Test 1.1 :", test(1)) # OUT : Test 1.1 : Arguments function not completed...
print("Test 1.2 :", test(c = 3)) # OUT : Test 1.2 : (1, 2, 3)
print("Test 2 :", test(1, 2)) # OUT : Test 2 : Arguments function not completed...
print("Test 3 :", test(c = 10)) # OUT : Test 3 : (1, 2, 10)
print("Test 4 :", test(0, 1, 2)) # OUT : Test 4 : (0, 1, 2)
```
