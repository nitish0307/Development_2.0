evenCount = 0
oddCount = 0

for i in range(1,6):
  n = int(input(f"Enter the number {i}: "))

  if n % 2 == 0:
    print(f"{n} is Even.")
    evenCount += 1
  else:
    print(f"{n} is Odd.")
    oddCount +=1

print("\nTotal Even Numbers:", evenCount)
print("Total Odd Numbers:", oddCount)


