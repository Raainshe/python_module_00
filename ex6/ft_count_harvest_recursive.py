def ft_count_harvest_recursive():
    print("Days until harvest: ", end="")
    days = int(input())

    def day_counter(day):
        if day>days:
            return
        print(f"Day {day}")
        day_counter(day+1)
    
    day_counter(1)
    print("Harvest time!")
