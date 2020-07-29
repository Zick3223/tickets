a = input()
if len(a) != 6 or not a.isdigit():
    print("That's not a ticket number")
else:
    if a[0] + a[1] + a[2] == a[3] + a[4] + a[5]:
        print("A lucky ticket!")
    else:
        print("Not a lucky ticket")