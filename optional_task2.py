temperature_above20 = True 
weekend = True 
sunny = True 

temp_check = input("Is the temperature today above 20 degrees? (Yes or No) ")
if temp_check == "Yes":
    temperature_above20 = True
    print("Wear a short-sleeved shirt")
elif temp_check == "No":
    temperature_above20 = False
    print("You should wear a long-sleeved shirt")
    
check_if_weekend = input("Is it the weekend? (Yes or No) ")
if check_if_weekend == "Yes":
    weekend = True 
    print("You should wear a shorts")
elif check_if_weekend == "No":
    weekend = False
    print("You should wear a jeans")
    
check_if_sunny = input("Is it sunny today? (Yes or No) ")
if check_if_sunny == "Yes":
    sunny = True
    print("You should wear a cap")
elif check_if_sunny == "No":
    sunny = False
    print("You should wear a raincoat")