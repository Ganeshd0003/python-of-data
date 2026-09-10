# Clean the data "986-Maria, ( D@t@ Engineer);; 27y)  "

data = "986-Maria, ( D@t@ Engineer);; 27y)  "

output = (
    data.replace("986-", "Name : ")
        .replace(",", " | Role :")
        .replace("(", "")
        .replace("D@t@", "Data")
        .replace(");;", " | Age : ")
        .replace("y)", "")
        .strip()
)

print(output)
