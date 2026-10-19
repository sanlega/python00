def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    days = range(days)
    for day in days:
        print(f"Day {day+1}")
    print("Harvest time!")
