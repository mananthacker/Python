def find_triplets(n):
    triplets = []
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c = (a ** 2 + b ** 2) ** 0.5
            if c == int(c) and c <= n:
                triplets.append((a, b, int(c)))
    return triplets

n = 30
print(find_triplets(n))

def print_24_hours():
    for hour in range(24):
        if hour == 0:
            print("Midnight")
        elif hour < 12:
            print(f"{hour} AM")
        elif hour == 12:
            print("Noon")
        else:
            print(f"{hour - 12} PM")

print_24_hours()
