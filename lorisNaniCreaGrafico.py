
# Loris Nani
import pandas as pd
import plotly.express as px
pd.options.plotting.backend = "plotly"
df=pd.read_csv("Food_Production.csv")
newdf=df
newdf.index=newdf["Food product"]
newdf=newdf.iloc[:,0:9].drop("Food product", axis=1)
newdf=newdf.sort_values(by="Total_emissions", ascending=False)

newdf["Other (Transport, Packging, Retail, Processing)"]=newdf.loc[:,["Transport", "Packging","Retail", "Processing"]].sum(axis=1)
newdf["Other (Transport, Packging, Retail, Processing)"]

plot=newdf.head(5).drop(columns=["Total_emissions","Transport", "Packging","Retail", "Processing"]).plot.bar(title="<b>Total emissions of the top 5 food products that emit the most CO2</b>", 
                                                                                                             barmode="stack",
                                                                                                             labels={"value":"<b>Total emissions (kg CO2 eq.)</b>", 
                                                                                                                     "variable":"<b>Type of Emissions</b>", 
                                                                                                                     "Food product":"<b>Food product</b>"},
                                                                                                             color_discrete_sequence=["#F57E61", "#68F570", "#F5AA29", "#6CDBF5", "#D24FF5"]
                                                                                                             )
plot.update_traces(
    hovertemplate = "%{value}",
    
)
plot.update_layout(
    legend=dict(
        yanchor="top",
        xanchor="right",
        x=1,
        title_font_family="Merriweather",
        font=dict(
            family="Merriweather",
        ),
        bgcolor="white",
        bordercolor="black",
        borderwidth=2
    ),
    font=dict(
        family="Gloock",
        size=13,
    ),
    title=dict(
        font=dict(size=20)
    ),
    hovermode="x",
    paper_bgcolor="#e8ddcc",   
)

plot.write_html("plot.html")