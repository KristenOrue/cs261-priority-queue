   
def iterative_factorial(n):
    product = 1
    for i in range(1, n-1):
        product = product * i

    return product 


num = 5

print(f'The iterative factorial of {num} is {iterative_factorial(num)}.')


def recursive_factorial(n):
#base case if your way out
    if (n==1):
        return n
    else:
        return n* recursive_factorial(n-1)
    
print(f'The iterative factorial of {num} is {recursive_factorial(num)}.')
