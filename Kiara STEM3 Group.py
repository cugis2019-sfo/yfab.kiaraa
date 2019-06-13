import plotly
dir(plotly)

studentlist = [["steve",32,"male"],["lia",28,"female"],["vin",45,"male"],["katie",38,"female"]]
print(studentlist)

studentlistdf = pandas.DataFrame(studentlist)
print(studentlistdf)

studentlistdf = pandas.DataFrame(studentlist,columns=["name","age","gender"])
print(studentlistdf)

studentlistdf = pandas.DataFrame(studentlist,columns=["name","age","gender"],index=["1","2","3","4"])
print(studentlistdf)

#graph our data
from plotly.offline import plot
import plotly.graph_objs as go

agename = go.Bar(x=studentlistdf["name"], y=studentlistdf["age"])

plot([agename])



































