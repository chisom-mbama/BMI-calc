
#Declaring fixed variables for the calculation of drop factor and BMI 
Blooddropfactor = 15
Fluiddropfactor = 20
print ("Welcome")
print ("")

name = input ("Please input your name\n")
print ("Welcome", name)
print ("")

def action():
    red= input ("Do you want to exit? \n(e)Yes \n(f)No\n")
    if (red == "f"):
        qestio()
    elif (red == "e"):
        print ("Thank You for using my app")
        exit()
    else:
        print ("please,select an option")
        return action()

def qestio():
    reason = input("What do you want to calculate \n(a)BMI or \n(b)Drop factor\n")
    if (reason == "a"):
        WT=float(input('input weight in Kg\n'))
        HT=float(input('input height in metres\n'))
        BMI=WT/(HT**2)
        Y = round (BMI,1)
        print ("Your BMI is", Y,"kg/m2")
        return action()
    else:
        (reason == "b")
        Vol=int(input('Input Volume of fluid\n'))
        Time=int(input('Input Time in hours\n'))
    Fluidtype=input ("(c)Blood or \n(d)Fluid\n")
    if (Fluidtype == "c"):
        Dropfactor=(Vol*Blooddropfactor)/(Time*60)
        X = round(Dropfactor,1)
        print ("Drop Factor is" , X,"drops per minute")
        return action()
    else:
        (Fluidtype == "d")
        Dropfactor=(Vol*Fluiddropfactor)/(Time*60) 
        X = round (Dropfactor,1)
        print ("Drop Factor is" , X,"drops per minuite")
        return action()
print (qestio())

    
    
                
