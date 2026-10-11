birthday=0
#set1
print("is your birthdayin set1?")
print("1 3 5 7")
print("9 11 13 15")
print("17 19 21 23")
print("25 27 29 31")
answer1=int(input("Enter 0 for no and 1 for yes: "))
if answer1==1:
    birthday=birthday+1
#set2
print("is your birthday in set2?")
print("2 3 6 7")
print("10 11 14 15")
print("18 19 22 23")
print("26 27 30 31")
answer2=int(input("enter 0 for no and 1 for yes: "))
if answer2==1:
    birthday=birthday+2
#set3
print("is your birthday in set3?")
print("4 5 6 7")
print("12 13 14 15")
print("20 21 22 23")
print("28 29 30 31")
answer3=int(input("enter 0 for no and 1 for yes: "))
if answer3==1:
    birthday=birthday+4
#set4
print("is your birthday in set4?")
print("8 9 10 11")
print("12 13 14 15")
print("24 25 26 27")
print("28 29 30 31")
answer4=int(input("enter 0 for no and 1 for yes: "))
if answer4==1:
    birthday=birthday+8
#set5
print("is your birthday in set5?")
print("16 17 18 19")
print("20 21 22 23")
print("24 25 26 27")
print("28 29 30 31")
answer5=int(input("enter 0 for no and 1 for yes: "))
if answer5==1:
    birthday=birthday+16
print("your birthday is:" , birthday)
