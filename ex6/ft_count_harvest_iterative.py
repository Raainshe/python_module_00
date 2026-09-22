def ft_count_harvest_iterative():
    print("Days until harvest: ", end="")
    days = int(input())
    for day in range(days):
        print(f"Day {day+1}")
    print("Harvest time!")