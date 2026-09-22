def ft_water_reminder():
    print("Days since laster watering: ", end="")
    water = int(input())
    if water > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")