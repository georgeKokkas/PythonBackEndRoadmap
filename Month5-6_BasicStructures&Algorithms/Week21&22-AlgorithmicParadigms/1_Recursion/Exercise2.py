# Implement a recursive function to solve the Tower of Hanoi problem.

def tower_of_hanoi(n, source, target, auxiliary):
    # Base case: only one disk to move from source to target
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, target)
    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    # Move the n-1 disks from auxiliary to target
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Test Tower of Hanoi
tower_of_hanoi(3, 'A', 'C', 'B')
# Output:
# Move disk 1 from A to C
# Move disk 2 from A to B
# Move disk 1 from C to B
# Move disk 3 from A to C
# Move disk 1 from B to A
# Move disk 2 from B to C
# Move disk 1 from A to C
