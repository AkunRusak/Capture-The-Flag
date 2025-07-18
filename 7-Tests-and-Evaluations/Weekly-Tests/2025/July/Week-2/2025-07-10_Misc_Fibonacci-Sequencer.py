def fib_mod(n, m):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % m
    return a

for i in range(10000):
    if fib_mod(i, 9973) == 6015:
        print(f"flag{{{i}}}")  # ➝ flag{2023}
        break
