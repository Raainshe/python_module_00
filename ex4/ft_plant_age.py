def ft_plant_age():
    print("Enter plant age in days: ", end="")
    plantAge = int(input())
    if plantAge > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")