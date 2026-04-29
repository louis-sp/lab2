def main():
print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")



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
def main():






cbmi (height = 1.6,weight = 57)





