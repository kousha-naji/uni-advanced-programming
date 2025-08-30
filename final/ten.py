def sum_of_cubes(n):
    if n == 1:
        return 1
    return (n**3) + sum_of_cubes(n-1)

print(sum_of_cubes(5))