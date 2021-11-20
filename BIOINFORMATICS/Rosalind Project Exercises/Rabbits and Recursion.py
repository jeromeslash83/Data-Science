def pythonic_rabbits(n, offspring):
    f1, child = 1, 1
    for _ in range (n-1):
        child, f1 = f1, f1 + (child*offspring)
    return child

print(pythonic_rabbits(34, 2))


def recursive_rabbits(n, offspring):
    if n == 1:
        return 1
    elif n == 2:
        return offspring
    
    f1 = recursive_rabbits(n-1, offspring)
    f2 = recursive_rabbits(n-2, offspring)

    if n <= 4:
        return f1 + f2
    
    return (f1 + (f2 * offspring))

print(recursive_rabbits(34, 2))
