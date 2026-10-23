import random
import time
import os

filename = "dataset.txt"
target_size = 512 * 1024 * 1024  # 512 MiB
random.seed(42)

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
written = 0
records = 0
start = time.perf_counter()

with open(filename, "w", buffering=1024 * 1024) as f:
    while written < target_size:
        key = random.randrange(10**12)
        payload = "".join(random.choices(chars, k=80))
        line = f"{key:012d},{payload}\n"
        f.write(line)
        written += len(line)
        records += 1

print(f"Records generated: {records:,}")
print(f"File size: {os.path.getsize(filename) / (1024**2):.2f} MiB")
print(f"Generation time: {time.perf_counter() - start:.2f} seconds")
