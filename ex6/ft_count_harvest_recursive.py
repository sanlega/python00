def count_days(day, days):
    if day > days:
        print("Harvest time!")
        return
    print("Day", day)
    count_days(day + 1, days)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count_days(1, days)
