
def display_main_menu():
    print("Enter some numbers separated by commas")


def get_user_input():
    uinumbers = input()
    uisplitnumbers = uinumbers.split(",")
    uilist = [float(num) for num in uisplitnumbers]
    print(uilist)
    return uilist


def calc_average(uilist):
    total_count = len(uilist)
    total = sum(uilist)
    average = total / total_count
    print(average)
    return total_count


def find_min_max(uilist):
    minui = min(uilist)
    maxui = max(uilist)
    print(minui)
    print(maxui)
    return minui, maxui


def sort_temperature(uilist):
    sorted_list = sorted(uilist)
    print(sorted_list)
    return sorted_list


def calc_median_temperature(uilist, total_count):
    sortuilist = sorted(uilist)
    mid = total_count // 2

    if total_count % 2 == 1:
        median = sortuilist[mid]
    else:
        median = (sortuilist[mid - 1] + sortuilist[mid]) / 2

    print(median)
    return median


def cbmi(height, weight):
    print("Height =", height)
    print("Weight =", weight)

    bmi = weight / (height ** 2)
    print(bmi)

    if bmi < 18.5:
        return -1
    elif bmi > 25:
        return 1
    else:
        return 0


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")



if __name__ == "__main__":
    main()

    display_main_menu()
    uilist = get_user_input()

    total_count = calc_average(uilist)

    find_min_max(uilist)
    sort_temperature(uilist)
    calc_median_temperature(uilist, total_count)
    cbmi(height = 1.7 , weight = 80)

   