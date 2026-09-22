def ft_harvest_total():
    total = 0
    for i in range(3):
        print(f"Day {i+1} harvest: ", end="")
        total += int(input())

    print(f"Total harverst: {total}")