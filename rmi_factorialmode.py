#server.py
import Pyro4
from collections import Counter

@Pyro4.expose
class Calculator:
    def factorial(self, n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact
    
    def mode(self, arr):
        counts = Counter(arr)
        highest = max(counts.values())
        modes = [x for x, count in counts.items()
                 if count == highest]
        return modes
daemon = Pyro4.Daemon()
uri = daemon.register(Calculator())
print("Server is ready")
print("Server URI:", uri)
daemon.requestLoop()

#client.py

import Pyro4
uri = input("Enter Server URI: ")
calculator = Pyro4.Proxy(uri)
n = int(input("Enter n for factorial: "))
print("Factorial:", calculator.factorial(n))
arr = list(map(int, input(
    "Enter array elements separated by spaces: "
).split()))
print("Mode:", calculator.mode(arr))
calculator._pyroRelease()
