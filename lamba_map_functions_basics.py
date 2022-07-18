## Data
txt = [
    'lambda functions are anonymous functions.',
    'anonymous functions dont have a name.',
    'functions are objects in Python.'
]


## One-Liner
### Opción map y lambda
# mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)

### Opción list comprehension
mark = [(True, s) if 'anonymous' in s else (False, s) for s in txt]

## Result
### Opción map y lambda
# print(list(mark))

### Opción list comprehension
print(mark)