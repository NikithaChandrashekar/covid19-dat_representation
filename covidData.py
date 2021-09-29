import pandas as pd
import plotly.express as px
df=pd.read_csv("virus_data.csv")
#fig=px.bar(df , x="Country" , y= "InternetUsers")
fig=px.scatter(df , x="date" , y= "cases", color="country")
fig.show()
