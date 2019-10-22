x = int(input("Type total Load or wattage :"))
y = int(input("Type Total required battery backup :"))
 
a = 0.25 * x
b = x + a 
print("You should select a UPS of Watts:", b )

c = int(input("select the AH of battery needed for Backup 1200(12*100AH) , 1740(12*145AH) ,2280(12*190AH), 1020(12*85AH), 1380(12*115AH) : "))
if (c == 1200): # 100Ah 12V Battery
    d = 1200 / x
    e = y / d
    print("This is the required number of Batteries :", e) # after this copy
    f = 100 * 0.1 * e  # Charging current
    print("The required charging current in AMPERES is :", f)
    g = ((e * 100 * 0.40)+(e * 100))/(f + 2) # total AH of battery multiply by 40percent losses and divide by charging current with an addition of 2 for losses 
    print("The total charging time in Hours will be HOURS :", g)
    h = int(input("Do you want to know the number of Solar panels required (1) Without DC load or (2) With DC load"))
    if (h == 1) :
        i = 12 * f
        j = int(input("Which Solar panel to select (1) 150 Watt or (2) 330 Watt or (3) 60 Watt, Press (1),(2) or (3)"))
        if (j == 1):
            k = i / 150
            print("The number of Solar Panels required are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",f + 2)  
        elif (j == 2) :
            k = i / 330
            print("The number od solar Panels required of 330 watt are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",f + 2)  
        elif (j == 3):
            k = i / 60
            print("The number of solar Panels required of 60 watt are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",f + 2)      
        else:
            print("Incorrect selection")       
    elif (h == 2):
        l = int(input("Type the number of extra Amperes required on DC or AC load "))
        m = l + f
        print("the total required watts are now ", 12 * m)
        j = int(input("Which Solar panel to select (1) 150 Watt or (2) 330 Watt or (3) 60 Watt, Press (1),(2) or (3)"))
        if (j == 1):
            k = (m * 12) / 150
            print("The number of Solar Panels required are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",m + 2)  
        elif (j == 2) :
            k = (m * 12) / 330
            print("The number od solar Panels required of 330 watt are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",m + 2)  
        elif (j == 3):
            k = (m * 12) / 60
            print("The number of solar Panels required of 60 watt are :", k)
            print("Please attach these in Parallel Combination")  
            print("the required charge controller for this will be AMP :",m + 2)  
        else:
            print("Incorrect selection") 
    else:
        print("incorrect selection")

#The others start from here: Will do them tomorrow

elif (c == 1740): # 145AH 12V Battery
    d = 1740 / x
    e = y / d
    print("This is the required number of batteries :", e) # after this copy
    f = 145 * 0.1 * e  # Charging current
    print("The required charging current in AMPERES is :", f)
    g = ((e * 145 * 0.40)+(e * 145))/(f + 2) # total AH of battery multiply by 40percent losses and divide by charging current with an addition of 2 for losses 
    print("The total charging time in Hours will be HOURS :", g)
    h = int(input("Do you want to know the number of Solar panels required (1) Without DC load or (2) With DC load"))
    if (h == 1) :
        i = 12 * f
        j = int(input("Which Solar panel to select (1) 150 Watt or (2) 330 Watt or (3) 60 Watt, Press (1),(2) or (3)"))
        if (j == 1):
            k = i / 150
            print("The number of Solar Panels required are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",f + 2)  
        elif (j == 2) :
            k = i / 330
            print("The number od solar Panels required of 330 watt are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",f + 2)  
        elif (j == 3):
            k = i / 60
            print("The number of solar Panels required of 60 watt are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",f + 2)      
        else:
            print("Incorrect selection")       
    elif (h == 2):
        l = int(input("Type the number of extra Amperes required on DC or AC load "))
        m = l + f
        print("the total required watts are now ", 12 * m)
        j = int(input("Which Solar panel to select (1) 150 Watt or (2) 330 Watt or (3) 60 Watt, Press (1),(2) or (3)"))
        if (j == 1):
            k = (m * 12) / 150
            print("The number of Solar Panels required are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",m + 2)  
        elif (j == 2) :
            k = (m * 12) / 330
            print("The number od solar Panels required of 330 watt are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",m + 2)  
        elif (j == 3):
            k = (m * 12) / 60
            print("The number of solar Panels required of 60 watt are :", k)
            print("Please attach these in Parallel Combination")  
            print("the required charge controller for this will be AMP :",m + 2)  
        else:
            print("Incorrect selection") 
    else:
        print("incorrect selection")


#Next will be done from here    
elif (c == 2280): #190AH 12V Battery
    d = 2280 / x
    e = y / d
    print("This is the required number of batteries :", e) # after this copy
    f = 190 * 0.1 * e  # Charging current
    print("The required charging current in AMPERES is :", f)
    g = ((e * 190 * 0.40)+(e * 190))/(f + 2) # total AH of battery multiply by 40percent losses and divide by charging current with an addition of 2 for losses 
    print("The total charging time in Hours will be HOURS :", g)
    h = int(input("Do you want to know the number of Solar panels required (1) Without DC load or (2) With DC load"))
    if (h == 1) :
        i = 12 * f
        j = int(input("Which Solar panel to select (1) 150 Watt or (2) 330 Watt or (3) 60 Watt, Press (1),(2) or (3)"))
        if (j == 1):
            k = i / 150
            print("The number of Solar Panels required are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",f + 2)  
        elif (j == 2) :
            k = i / 330
            print("The number od solar Panels required of 330 watt are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",f + 2)  
        elif (j == 3):
            k = i / 60
            print("The number of solar Panels required of 60 watt are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",f + 2)      
        else:
            print("Incorrect selection")       
    elif (h == 2):
        l = int(input("Type the number of extra Amperes required on DC or AC load "))
        m = l + f
        print("the total required watts are now ", 12 * m)
        j = int(input("Which Solar panel to select (1) 150 Watt or (2) 330 Watt or (3) 60 Watt, Press (1),(2) or (3)"))
        if (j == 1):
            k = (m * 12) / 150
            print("The number of Solar Panels required are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",m + 2)  
        elif (j == 2) :
            k = (m * 12) / 330
            print("The number od solar Panels required of 330 watt are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",m + 2)  
        elif (j == 3):
            k = (m * 12) / 60
            print("The number of solar Panels required of 60 watt are :", k)
            print("Please attach these in Parallel Combination")  
            print("the required charge controller for this will be AMP :",m + 2)  
        else:
            print("Incorrect selection") 
    else:
        print("incorrect selection")


#Next from here    
elif (c == 1020): #85AH 12V Battery
    d = 1020 / x
    e = y / d
    print("This is the required number of batteries :", e)# after this copy
    f = 85 * 0.1 * e  # Charging current
    print("The required charging current in AMPERES is :", f)
    g = ((e * 85 * 0.40)+(e * 85))/(f + 2) # total AH of battery multiply by 40percent losses and divide by charging current with an addition of 2 for losses 
    print("The total charging time in Hours will be HOURS :", g)
    h = int(input("Do you want to know the number of Solar panels required (1) Without DC load or (2) With DC load"))
    if (h == 1) :
        i = 12 * f
        j = int(input("Which Solar panel to select (1) 150 Watt or (2) 330 Watt or (3) 60 Watt, Press (1),(2) or (3)"))
        if (j == 1):
            k = i / 150
            print("The number of Solar Panels required are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",f + 2)  
        elif (j == 2) :
            k = i / 330
            print("The number od solar Panels required of 330 watt are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",f + 2)  
        elif (j == 3):
            k = i / 60
            print("The number of solar Panels required of 60 watt are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",f + 2)      
        else:
            print("Incorrect selection")       
    elif (h == 2):
        l = int(input("Type the number of extra Amperes required on DC or AC load "))
        m = l + f
        print("the total required watts are now ", 12 * m)
        j = int(input("Which Solar panel to select (1) 150 Watt or (2) 330 Watt or (3) 60 Watt, Press (1),(2) or (3)"))
        if (j == 1):
            k = (m * 12) / 150
            print("The number of Solar Panels required are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",m + 2)  
        elif (j == 2) :
            k = (m * 12) / 330
            print("The number od solar Panels required of 330 watt are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",m + 2)  
        elif (j == 3):
            k = (m * 12) / 60
            print("The number of solar Panels required of 60 watt are :", k)
            print("Please attach these in Parallel Combination")  
            print("the required charge controller for this will be AMP :",m + 2)  
        else:
            print("Incorrect selection") 
    else:
        print("incorrect selection")

#NExt    
elif (c == 1380): # 115 AH 12V battery
    d = 1380 / x
    e = y / d
    print("This is the required number of batteries :", e)# after this copy
    f = 115 * 0.1 * e  # Charging current
    print("The required charging current in AMPERES is :", f)
    g = ((e * 115 * 0.40)+(e * 115))/(f + 2) # total AH of battery multiply by 40percent losses and divide by charging current with an addition of 2 for losses 
    print("The total charging time in Hours will be HOURS :", g)
    h = int(input("Do you want to know the number of Solar panels required (1) Without DC load or (2) With DC load"))
    if (h == 1) :
        i = 12 * f
        j = int(input("Which Solar panel to select (1) 150 Watt or (2) 330 Watt or (3) 60 Watt, Press (1),(2) or (3)"))
        if (j == 1):
            k = i / 150
            print("The number of Solar Panels required are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",f + 2)  
        elif (j == 2) :
            k = i / 330
            print("The number od solar Panels required of 330 watt are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",f + 2)  
        elif (j == 3):
            k = i / 60
            print("The number of solar Panels required of 60 watt are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",f + 2)      
        else:
            print("Incorrect selection")       
    elif (h == 2):
        l = int(input("Type the number of extra Amperes required on DC or AC load "))
        m = l + f
        print("the total required watts are now ", 12 * m)
        j = int(input("Which Solar panel to select (1) 150 Watt or (2) 330 Watt or (3) 60 Watt, Press (1),(2) or (3)"))
        if (j == 1):
            k = (m * 12) / 150
            print("The number of Solar Panels required are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",m + 2)  
        elif (j == 2) :
            k = (m * 12) / 330
            print("The number od solar Panels required of 330 watt are :", k)
            print("Please attach these in Parallel Combination")
            print("the required charge controller for this will be AMP :",m + 2)  
        elif (j == 3):
            k = (m * 12) / 60
            print("The number of solar Panels required of 60 watt are :", k)
            print("Please attach these in Parallel Combination")  
            print("the required charge controller for this will be AMP :",m + 2)  
        else:
            print("Incorrect selection") 
    else:
        print("incorrect selection")
       

 #Next
else:
    print("invalid Battery AH")    


# Add a while loop to control the outcome and restart automatically by pressing x or ys


