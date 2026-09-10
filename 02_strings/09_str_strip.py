# Cleaning the whitespaces

# for removing left whitespaces lstrip()
# for removing right whitespaces rstrip()
# for removing left and right both whitespaces strip()

text = "   Engineering"
print(text.lstrip())

text1 = "Engineering                       "
print(text1.rstrip())

text2 = "   Engineering                             "
print(text2.strip())

# If we want to remove something other than white space still we can use strip

text3 = "$$$Abc$$$"
print(text3.strip("$"))

textt = "#####Ganesh%%##"
print(textt.strip("#").strip("%"))

print(textt.replace("#", "").replace("%", ""))


# Use Case
name = "  Ganesh"

if len(name) != len(name.strip()):
    print(name)
else:
    print("Fine")

print(
    f"Length of actual name : {len(name)}\nLength of striped name : {len(name.strip())}\nWhite Spaces : {len(name) - len(name.strip())}")
