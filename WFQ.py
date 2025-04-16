from collections import deque

# Use the given input packet stream directly
packet_stream = [
    "S Mary", "P Dee", "P Dee", "E Eileen", "E Mike", "E Joe", "P Dee",
    "E Vicky", "E George", "P Dee", "P Joe", "E Sally", "P Joe", "S Pete",
    "P Dee", "S Bill", "S Chase", "E Price", "P Dee", "E Sue"
]

# Step 1: Create queues
premium_queue = deque()
standard_queue = deque()
economy_queue = deque()

# Step 2: Sort packets into queues
for packet in packet_stream:
    priority, name = packet.split(maxsplit=1)
    if priority == 'P':
        premium_queue.append(name)
    elif priority == 'S':
        standard_queue.append(name)
    elif priority == 'E':
        economy_queue.append(name)

# Step 3: Dequeue using WFQ: 3 Premium, 2 Standard, 1 Economy
print("Dequeued packets in order:\n")
while premium_queue or standard_queue or economy_queue:
    for _ in range(3):
        if premium_queue:
            print(f"Premium: {premium_queue.popleft()}")
    for _ in range(2):
        if standard_queue:
            print(f"Standard: {standard_queue.popleft()}")
    if economy_queue:
        print(f"Economy: {economy_queue.popleft()}")
