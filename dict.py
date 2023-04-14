pairs = {
   1: "apple",
   "orange": [2, 3, 4], 
   True: False, 
   12: "True",
}

print(pairs.get("orange"))
print(pairs.get(True, 40))
print(pairs.get(12345, "not found"))