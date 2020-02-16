import time
import random

codes = [31, 32, 33, 34, 35, 36, 37, 91, 92, 93, 94, 95, 96, 97]
a = ord("a")
for i in range(a, a + 100):
    time.sleep(0.2)
    print(f'{chr(155)}{random.choice(codes)};1m{chr(i)}', end=' ', flush=True)
print('\x1b[0m')