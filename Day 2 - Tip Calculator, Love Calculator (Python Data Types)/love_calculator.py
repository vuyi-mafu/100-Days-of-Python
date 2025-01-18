# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
full_name = (f"{name1}"+f"{name2}")
# print(full_name)
t = 0
r = 0
u = 0
e = 0

l = 0
o = 0
v = 0
e = 0

full_name = full_name.lower()

t = full_name.count("t")
r = full_name.count("r")
u = full_name.count("u")
e = full_name.count("e")

true = t + r + u + e
# print(true)

l = full_name.count("l")
o = full_name.count("o")
v = full_name.count("v")
e = full_name.count("e")

love = l + o + v + e
true_love = int((f"{true}"+f"{love}"))
# print(true_love)

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together  like coke and mentos.")

elif true_love >= 40 and true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")

else:
    print(f"Your score is {true_love}")

