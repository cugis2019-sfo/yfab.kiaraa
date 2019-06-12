cadbury1 = "milk choclate"
cadbury2 = "dark chocolate"
cadbury3 = "white chocolate"

cadburymilk = 5
cadburydark = 3
cadburywhite = 8

milk = 5
milk, 5

chocolate1 = {"cadburymilk":5}
chocolate2 = {"cadburydark":3}
chocolate3 = {"cadburywhite":8}

print(chocolate1, chocolate2, chocolate3)

chocolates = {"milk":5, "dark":3, "white":8}

studentinfo = {"steve":32, "lia":28, "vin":45, "katie":38}
print(studentinfo)

gender = {"steve":"male", "lia":"female", "vin":"male", "katie":"female"}

import pandas
dir(pandas)

studentinfocol = pandas.Series(studentinfo)
print(studentinfocol)

gendercol = pandas.Series(gender)
print(gendercol)

chocolatescol = pandas.Series(chocolates)
print(chocolatescol)

print(chocolates)
#dataframes
chocolatesdata = [chocolates] #convert dict to list
print(chocolatesdata)

chocolatesdf = pandas.DataFrame(chocolatesdata)
print(chocolatesdf)

studentinfo = {"steve":32, "lia":28, "vin":45, "katie":38}
studentinfodata = [studentinfo]
print(studentinfodata)

studentinfodf = pandas.DataFrame(studentinfodata)
print(studentinfodf)

gender = {"steve":"male", "lia":"female", "vin":"male", "katie":"female"}
genderdata = [gender]
print(genderdata)

genderdf = pandas.DataFrame(genderdata)
print(genderdf)

studentlist = [["steve",32,"male"],["lia",28,"female"],["vin",45,"male"],["katie",38,"female"]]
studentlistdf = pandas.DataFrame(studentlist,columns=["name","age","gender"],index=["1","2","3","4"])
print(studentlistdf)

print(studentinfo)
print(gender)

studentdf1 = [studentinfo, gender]
print(studentdf1)

studentdf2 = pandas.DataFrame(studentdf1,index=["age","gender"])
print(studentdf2)

import pandas as pd
import plotly, plot

















