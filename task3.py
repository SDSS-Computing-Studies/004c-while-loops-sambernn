#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""
num = input("enter a number:\n")
num = float(num)
targetnum = 2
targetnum = int(targetnum)
while num != targetnum:
    targetnum + 2
    if num == targetnum:
        print("That is an even integer")

print("That is not an even integer")

#theres gotta be a better way to do this