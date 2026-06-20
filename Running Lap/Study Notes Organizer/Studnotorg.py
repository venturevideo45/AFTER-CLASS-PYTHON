import os

# 1. Create files
with open("math.txt", "w") as f:
    f.write("Math is about numbers.")

with open("sci.txt", "w") as f:
    f.write("Science is about nature.")

# 2. Count words
with open("math.txt", "r") as f:
    print("Math words:", len(f.read().split()))

with open("sci.txt", "r") as f:
    print("Science words:", len(f.read().split()))

# 3. Check and delete old merged file
if os.path.exists("merged.txt"):
    os.remove("merged.txt")

# 4. Merge files
with open("merged.txt", "w") as out:
    with open("math.txt", "r") as f1:
        out.write(f1.read() + "\n")
    with open("sci.txt", "r") as f2:
        out.write(f2.read())

print("Done!")
