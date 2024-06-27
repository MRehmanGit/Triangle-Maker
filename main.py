def generate_triangle(value):
    # Loop through each level from 1 to value (inclusive)
    for i in range(1, value + 1):
        # Print i asterisks for the current level
        print("*" * i)

# Prompt the user to enter a number
num = int(input("Enter a number: "))

# Call the generate_triangle function with the user's input
generate_triangle(num)
