
def display_main_menu():
    print("enter some numbers seperated by commas")

def get_user_input():
    uinumbers = input()
    uisplitnumbers = uinumbers.split(",")
    uilist = [float(num) for num in uisplitnumbers]
    print (uilist)
    return (uilist)

def calc_average(uilist):
    total_count = len(uilist)
    total = sum(uilist)
    average = total / total_count
    print (average)
    return (total_count)
    

def find_min_max(uilist):
    minui = min(uilist)
    maxui = max(uilist)
    print (minui)
    print (maxui)   
    return (minui,maxui)

def sort_temperature(uilist):
    sort_temp = uilist.sort
    print (sort_temp)
    return (sort_temp)

def calc_median_temperature(uilist,total_count):
    sortuilist = sorted(uilist)
    medianpos = total_count % 2
    if medianpos == 1 :
        odd = total_count // 2 
        oddpos = int(medianpos)
        print (uilist[oddpos])
        return (uilist[oddpos])
    else: 
        odd = total_count // 2
        oddpos = int(medianpos)
        evenpos = oddpos - 1
        middle = (uilist[oddpos] + uilist[evenpos]) / 2
        print (middle)
        return(middle)




def cbmi ( height, weight):
    print ("Height = "+str(height))
    print ("Weight = "+str(weight))
    bmi = weight / (height * height)
    print (str(bmi))
    if(bmi < 18.0):
        print ("underweight")
    elif (bmi > 25.0):
        print ("overweight")
    else:
        print ("normal range")
    return bmi


    cbmi (height = 1.6,weight = 57)

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
display_main_menu()
uilist = get_user_input()
total_count = calc_average (uilist)
find_min_max(uilist)
sort_temperature(uilist)
calc_median_temperature(uilist,total_count)

if __name__ == "__main__":
    main()


