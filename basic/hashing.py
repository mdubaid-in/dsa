# Hashing | Maps | Time Complexity | Collisions | Division Rule of Hashing | Strivers A2Z DSA Course

list = [10, 5, 10, 15, 10, 5]

hash_map = {}


def count_freq(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq


def get_high_and_low_freq(arr):
    if not arr:
        return None, None

    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    high = max(freq, key=freq.get)
    low = min(freq, key=freq.get)

    return high, low


print("Frequency of numbers from", list, "is", count_freq(list))
print(
    "Highest and lowest frequency number from", list, "is", get_high_and_low_freq(list)
)
