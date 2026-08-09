```python
# Multiplication Table: 12 Different Ways

n = 5

# 1. Using for loop
print("1. FOR LOOP")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


# 2. Using while loop
print("\n2. WHILE LOOP")
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1


# 3. Using format()
print("\n3. FORMAT()")
for i in range(1, 11):
    print("{} x {} = {}".format(n, i, n * i))


# 4. Using % formatting
print("\n4. % FORMATTING")
for i in range(1, 11):
    print("%d x %d = %d" % (n, i, n * i))


# 5. Using string concatenation
print("\n5. STRING CONCATENATION")
for i in range(1, 11):
    print(str(n) + " x " + str(i) + " = " + str(n * i))


# 6. Using function
print("\n6. FUNCTION")

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

multiplication_table(n)


# 7. Using list comprehension
print("\n7. LIST COMPREHENSION")
[print(f"{n} x {i} = {n * i}") for i in range(1, 11)]


# 8. Using map()
print("\n8. MAP()")
list(map(lambda i: print(f"{n} x {i} = {n * i}"), range(1, 11)))


# 9. Using lambda
print("\n9. LAMBDA")
table = lambda i: print(f"{n} x {i} = {n * i}")

for i in range(1, 11):
    table(i)


# 10. Using recursion
print("\n10. RECURSION")

def recursive_table(n, i=1):
    if i > 10:
        return

    print(f"{n} x {i} = {n * i}")
    recursive_table(n, i + 1)

recursive_table(n)


# 11. Using list
print("\n11. LIST")

results = [n * i for i in range(1, 11)]

for i, result in enumerate(results, 1):
    print(f"{n} x {i} = {result}")


# 12. Using join()
print("\n12. JOIN()")

table = "\n".join(
    f"{n} x {i} = {n * i}"
    for i in range(1, 11)
)

print(table)
```
