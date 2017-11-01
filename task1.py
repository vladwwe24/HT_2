# task 1 season
def season(x = int(input("Enter number of month(1-12): \n"))):
    wi = (12, 1, 2)
    sp = (3, 4, 5)
    su = (6, 7, 8)
    au = (9, 10, 11)
    if x <= 0 or x >=13:
        print("Error : Number must to be from 1 to 12")
    elif x in wi :
        print("Winter")
    elif x in sp :
        print("Spring")
    elif x in su :
        print("Summer")
    elif x in au :
        print("Autumn")
    else :
        print("Error : Number must to be from 1 to 12")

season()

def season(x = int(input())):
    a = "Enter month number"
    seasons = {
        'Winter': (12, 1, 2),
        'Spring': (3, 4, 5),
        'Summer': (6, 7, 8),
        'Autumn': (9, 10, 11)
    }
    for key, value in seasons.items():
        if x in value:
            result = key
    print(result)
    return result

season()
