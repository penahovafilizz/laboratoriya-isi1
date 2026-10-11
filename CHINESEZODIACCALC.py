year=int(input("enter you birth year: "))
remainder=year%12
if remainder==0:
     print("monkey")
elif remainder==1:
    print("rooster")
elif remainder==2:
    print("dog")
elif remainder==3:
    print("pig")
elif remainder==4:
    print("rat")
elif remainder==5:
    print("ox")
elif remainder==6:
    print("tiger")
elif remainder==7:
    print("rabbit")
elif remainder==8:
    print("dragon")
elif remainder==9:
    print("snake")
elif remainder==10:
    print("horse")
else:
    print("goat")