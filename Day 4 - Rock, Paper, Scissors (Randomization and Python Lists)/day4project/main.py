# 🚨 Don't change the code below 👇
row1 = ["⬜","⬜","️⬜"]
row2 = ["⬜","⬜","️⬜"]
row3 = ["⬜","⬜","⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
position = int(position)

if position == 11:
    map[0][0] = 'X'
elif position == 21:
    map[0][1] = 'X'
elif position == 31:
    map[0][2] = 'X'
elif position == 12:
    map[1][0] = 'X'
elif position == 22:
    map[1][1] = 'X'
elif position == 32:
    map[1][2] = 'X'
elif position == 13:
    map[2][0] = 'X'
elif position == 23:
    map[2][1] = 'X'
elif position == 33:
    map[2][2] = 'X'
else:
    print("You have entered an invalid number!")

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

