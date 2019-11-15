import input

def findDupe(latest_freq, seen_freq, frequencies):
    for freq in frequencies:
        latest_freq = latest_freq + freq
        if latest_freq in seen_freq:
            return latest_freq, latest_freq, seen_freq
        print(latest_freq)
        seen_freq.add(latest_freq)
    return None, latest_freq, seen_freq

dupe, latest_freq, seen_freq = findDupe(0, set(), input.frequencies)
while dupe is None:
    dupe, latest_freq, seen_freq = findDupe(latest_freq, seen_freq, input.frequencies)
print("Dupe Found: {}".format(dupe))