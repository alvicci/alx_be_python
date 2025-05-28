rows = 5
count = 1
i = 0

for num in range(0, rows):
    for c in range(count, rows):
        # Print leading spaces for alignment
        print(" ", end="")
    # Print stars, increasing each row
    print("*" * (count + i))
    # Increment i to increase stars next row
    i += 1
    # Increment count to reduce spaces next row
    count += 1
