positive_sum = 0
negative_sum = 0
zero_count = 0

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))

    if num > 0:
        positive_sum += num
    elif num < 0:
        negative_sum += num
    else:
        print("Zero entered")
        zero_count += 1

print("\nResults:")
print("Sum of Positive Numbers:", positive_sum)
print("Sum of Negative Numbers:", negative_sum)
print("Total Zeros:", zero_count)
