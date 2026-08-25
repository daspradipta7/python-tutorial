x = "Welcome"

print(f"3rd index {x[3]}")
print(f"Length of x: {len(x)}")
print(f"First chracter of x: {x[0]}")


txt = 'The best things in life are free!'
# print 'Yes, free is present in the text.' if free word present in txt

if 'free' in txt:
    print("Yes, free is present in the text.")
else:
    print("Not present in the txt")

# python slicing
txt = "Welcome"
print(f"slice 3 to 5 {txt[3:5]}")
print(f"reverse {txt[::-1]}")


# upper and lower case
print(f"Upper case {txt.upper()}")
print(f"Lower case {txt.lower()}")

#trim white spcaes
txt = " hello world "
print("trim txt", txt.strip())


# replace
a = "Hello world"
print(a.replace("H", "J"))

# split string
print(a.split(" "))

a = "Aromatic and bold"
print(f"Is bold present in a {a.index('bold')}")

# encode
encodeed = a.encode('utf-8')
print(f"Encode lable {encodeed}")

#decode
print(f"Decode lable {encodeed.decode('utf-8')}")