def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break
    else:
        # The else block associated with a for loop executes only when the loop finishes iterating completely without hitting a break statement.
        return True
    return False  # if it hits the break statement then else block will not be executed and it will return False


# Print all prime numbers from 2 to N
N = int(input("Enter N: "))
for num in range(2, N + 1):
    if is_prime(num):
        print(num, end=" ")
