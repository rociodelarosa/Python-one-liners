## Data
visitors = [
    'Firefox', 'corrupted', 'Chrome', 'corrupted',
    'Safari', 'corrupted', 'Safari', 'corrupted',
    'Chrome', 'corrupted', 'Firefox', 'corrupted'
]

## One-Liner
visitors[1::2] = visitors[::2]
# lista[inicio:final:pasos(steps)]

## Result
print(visitors)