
# Lamport Logical Clock

n = 3
clock = [0] * n

def internal_event(pid):
    clock[pid] += 1
    print(f"P{pid}: Internal event, Clock = {clock[pid]}")

def send_message(pid):
    clock[pid] += 1
    timestamp = clock[pid]
    print(f"P{pid}: Sends message, Timestamp = {timestamp}")
    return timestamp

def receive_message(pid, timestamp):
    clock[pid] = max(clock[pid], timestamp) + 1
    print(f"P{pid}: Receives message, Clock = {clock[pid]}")

# Process events
internal_event(0)
timestamp = send_message(0)
receive_message(1, timestamp)

internal_event(1)
timestamp = send_message(1)
receive_message(2, timestamp)

internal_event(2)

print("\nFinal Lamport Clocks:")
for i in range(n):
    print(f"P{i}: {clock[i]}")
