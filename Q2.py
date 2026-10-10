def length_of_string(s):
    last_seen = {}
    start = best =0
    for i, c in enumerate(s):
        if c in last_seen and last_seen[c] >= start:
            start = last_seen[c] + 1
        last_seen[c] = i
        best = max(best, i - start + 1)
    return best

print(length_of_string("abcabcbb"))
print(length_of_string("bbbbb"))
