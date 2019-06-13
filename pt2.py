import pandas as pd
import plotly
from plotly.offline import plot
import plotly.graph_objs as go

df = pd.read_excel("GISdata.xlsx", sheet_name = "womenOccupation")

womenoccupation = go.Bar(x= df["occupation"], y=df["women"])
plot([womenoccupation])
