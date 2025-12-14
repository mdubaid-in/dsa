count = 10
diamond_count = 13


# Square Pattern
for i in range(count):
    print("*" * count)


# Right Triangle Pattern
for i in range(1, count + 1):
    print("*" * i)


# Left Triangle Pattern
for i in range(1, count + 1):
    print(" " * (count - i) + "*" * i)


# Pyramid Pattern
for i in range(count):
    space = count - i - 1
    middle = 2 * i + 1
    print(" " * space + "*" * middle + " " * space)


# Inverted Pyramid Pattern
for i in range(count):
    revert = count - i
    space = count - revert
    middle = 2 * revert - 1
    print(" " * space + "*" * middle + " " * space)


mid_value = (diamond_count + 1) // 2
# Diamond Pattern
for i in range(diamond_count):
    revert = diamond_count - i
    space = mid_value - i - 1 if i < mid_value else mid_value - revert
    middle = 2 * i + 1 if i < mid_value else 2 * revert - 1
    print(" " * space + "*" * middle + " " * space)

# Right Pyramid Pattern
for i in range(diamond_count):
    revert = diamond_count - i
    space = mid_value - i - 1 if i < mid_value else mid_value - revert
    middle = i + 1 if i < mid_value else diamond_count - i
    print("*" * middle + " " * space)

# Border Diamond Pattern
for i in range(diamond_count):
    revert = diamond_count - i - 1
    border = mid_value - i if i < mid_value else mid_value - revert
    space = 2 * i + 1 if i < mid_value else 2 * revert + 1
    print("*" * border + " " * space + "*" * border)

# Number Triangle Pattern
for i in range(count):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

for i in range(count):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

for i in range(count):
    for j in range(i):
        print((i + j) % 2, end=" ")
    print()

for i in range(count):
    for j in range(i):
        print(j + i, end=" ")
    print()
