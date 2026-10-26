
import random

n = int(input("Enter number of processes: "))

# Randomly assign clock times in minutes
clocks = [random.randint(1, 60) for _ in range(n)]

print("\nOriginal clock times:")
for i in range(n):
    print(f"P{i}: {clocks[i]} minutes")

# Master calculates average time
average = sum(clocks) / n

print(f"\nAverage clock time: {average:.2f} minutes")

# Calculate adjustments and synchronize clocks
print("\nClock adjustments:")

for i in range(n):
    adjustment = average - clocks[i]
    print(f"P{i}: {adjustment:+.2f} minutes")
    clocks[i] = average

print("\nSynchronized clock times:")
for i in range(n):
    print(f"P{i}: {clocks[i]:.2f} minutes")

print("\nAll clocks synchronized.")
