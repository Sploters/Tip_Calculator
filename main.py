from msvcrt import getch
# A prompt for user
print("Welcome to the Tip Calculator.")
total_bill = float(input("What was the total bill?\n $"))
people = int(input("How many people to split the bill?\n"))
percentage = int(input(
    "What percentage tip would you like to give? 10, 12 or 15?\n"))
result = round(float(total_bill/people) * float(100 + percentage)/100, 2)
print(f"Each person should pay: ${result}")
getch()
