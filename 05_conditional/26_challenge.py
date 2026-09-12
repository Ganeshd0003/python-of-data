attempts = 0
while attempts < 3:
    ans = input("Enter yes or no ? ")
    if ans == 'yes':
        print("Thank you")
        break
    attempts += 1
else:
    print("You exceed limit")