a = float(input("Hur manga kronor kostade bensinen?"))

if a<10:
    print("Det var billigt!")
elif a>=10 and a<=15:
    print("Tanka full tank :)")
elif a>=15 and a<=20:
    print("Tanka bara 10 liter :(")
else:
    print("Nu saljer jag bilen och cyklar!!!")
