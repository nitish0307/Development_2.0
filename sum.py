positive_sum = 0
negative_sum = 0
zero_count = 0

for i in range(1, 11):
    number = int(input(f"Enter number {i}: "))

    if number > 0:
        positive_sum += number
    elif number < 0:
        negative_sum += number
    else:
        print("Zero entered")
        zero_count += 1

print("\nResults:")
print("Sum of Positive Numbers:", positive_sum)
print("Sum of Negative Numbers:", negative_sum)
print("Total Zeros:", zero_count)