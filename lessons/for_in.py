"""An example of for in syntax."""

names: list[str] = ["Ben", "Sahil", "Joe", "Mama"]

# Example of iterating through names using a while loop
print("while output")
i: int = 0 
while i < len(names): 
    name: str = names[i]
    print(name)
    i += 1


# For...in loop is the same as above 
print("for in output")
for name in names: 
    print(name)
