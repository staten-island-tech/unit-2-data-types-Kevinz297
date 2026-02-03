def print_values(values):
    print(values[x])
    print(values[y])
    print(values[z])
    for i in values[x:y:z]:
        print(i)
values = [0, 1, 2, 3, 4, 5, 6]

x = 5
y = 1
z = 2

print_values(values)
print("Done")