
import time

clock_a = 0.0
clock_b = 0.0

drift_per_second = 0.010  # 10 milliseconds
duration = 60              # 1 minute

print("Time\tClock A\tClock B\tDifference")

for second in range(1, duration + 1):
    clock_a += 1
    clock_b += 1 + drift_per_second

    difference = clock_b - clock_a

    print(f"{second}s\t{clock_a:.3f}s\t"
          f"{clock_b:.3f}s\t{difference:.3f}s")

print("\nFinal difference:",
      f"{(clock_b - clock_a) * 1000:.0f} milliseconds")
