score = int(input("Enter your score from 1 to 10: "))

if score >= 4:
    if score >= 8:
        print("Excellent")
    elif score >= 6:
        print("Good")
    else:
        print("Average")
else:
    print("Not Good")
