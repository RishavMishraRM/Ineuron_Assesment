def max_min_distance(stalls, k):
    stalls.sort()
    left, right = 0, stalls[-1]
    while left < right:
        mid = (left + right + 1) // 2
        horses = 1
        last_stall = stalls[0]

        for stall in stalls:
            if stall - last_stall >= mid:
                horses += 1
                last_stall = stall
        if horses >= k:
            left = mid
        else:
            right = mid - 1
    return left
stalls = [1, 2, 4, 8, 9]
k = 3
print(max_min_distance(stalls, k))  

# Output: 3