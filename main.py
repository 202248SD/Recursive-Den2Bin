# We want to figure out a way to convert a denary number into a binary number using recursion

# Define Function
def denary_to_binary(denary):
    # Base Case: 0 is the same in both denary and binary
    if denary == 0:
        return 0
    # Use Recursive formula (Notice that any number % 2 is always 0 or 1, perfect for binary, which only has digits 0,1)
    return 10 * denary_to_binary(denary // 2) + denary % 2


print(denary_to_binary(64))
print(denary_to_binary(137))
