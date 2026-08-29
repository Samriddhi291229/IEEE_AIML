N = int(input("Enter the no of integers in the list: "))
num = input("Enter the integers (space separated) : ")
list = [int(x) for x in num.split()]

# 1) the largest element
max = list[0]
for i in range(N):
    if list[i] > max:
        max = list[i]
print("Largest:", max)

# 2) the smallest element
min = list[0]
for i in range(N):
    if list[i] < min:
        min = list[i]
print("Smallest:", min)

# 3) the sum of all elements

sum = 0
for i in range(N):
    sum += list[i]
print("Sum:", sum)

# 4) The number of even elements
even_count = 0
for i in range(N):
    if list[i] % 2 == 0:
        even_count += 1
print("Even count:", even_count)

# 5) The number of odd elements
odd_count = 0
for i in range(N):
    if list[i] % 2 != 0:
        odd_count += 1
print("Odd count:", odd_count)

# 6) The list in reverse order
print("Reversed:", end=" ")
for i in range(N-1, -1, -1):
    print(list[i], end=" ")
print("")
