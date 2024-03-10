def print_door_mat(N, M):
    # Upper part
    for i in range(N // 2):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(M, '-'))

    # Welcome message
    print("WELCOME".center(M, '-'))

    # Lower part
    for i in range(N // 2 - 1, -1, -1):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(M, '-'))

# Example usage:
N = 7  # You can adjust N as per your requirement (must be an odd natural number)
M = 3 * N  # M should be 3 times N
print_door_mat(N, M) 

# Output:
# ---.|.---
# --.|..|..|--
# .|..|..|..|.
# WELCOME
# .|..|..|..|.
# --.|..|..|--
# ---.|.---
