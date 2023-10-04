print("How many element to store in the list ? ", end="")
n = input()

arr = []
print("\nEnter", n, "Elements: ", end="")
n = int(n)
for i in range(n):
    element = input()
    arr.append(element)

print("\nThe list is:")
for i in range(n):
    print(arr[i], end=" ")
