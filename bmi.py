def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    #Add code here to calculate BMI
    bmi = weight / (height * height)
    #Add code here to display calculate BMI
    print(str(bmi))
    if(bmi<18.5):
        print("Under Weight")
    elif(bmi>25.0):
        print("Over Weight")
    else:
        print("Normal Weight")
calculate_bmi(weight=57, height=1.73)