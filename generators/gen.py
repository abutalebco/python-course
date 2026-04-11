import sys

# --- Generator ---
def my_generator(n):
    for x in range(n):
        yield x ** 2

values = my_generator(5)

for x in values:
    print(x)

print(f"size of this generator is {sys.getsizeof(values)}")


# --- Function List ---
def my_function_list(n):
    results = []
    for x in range(n):
        results.append(x ** 2)
    return results

values = my_function_list(5)
print(values[:])