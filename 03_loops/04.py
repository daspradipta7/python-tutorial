#skip 5 and stop when reach at 10

i = 1

while i < 15:
  
    if i == 5:
        i += 1
        continue

    if i == 10:
        break

    print(f"{i}")
    i += 1