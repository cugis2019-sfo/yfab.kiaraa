import pandas as pd
import plotly
from plotly.offline import plot
import plotly.graph_objs as go

df = pd.read_excel("GISdata.xlsx", sheet_name = "womenCEOs")
print(df)

womenceo = go.Bar(x=df["Year"], y=df["CEOs"], 
                  marker = {"color": df["CEOs"], "colorscale" : "Jet"}
                )
plot([womenceo])

titles = go.Layout(
        title = "Percenrage of Women CEOs Per Year",
        xaxis=go.layout.XAxis(
                title=go.layout.xaxis.Title(
                text="Year",
            )
        ),
        yaxis=go.layout.YAxis(
                title=go.layout.yaxis.Title(
                text="Percentage",
                )
            )
        )

fig = go.Figure(data=[womenceo], layout = titles)
plot(fig)


  