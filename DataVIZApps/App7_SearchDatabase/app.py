from shiny import App, render, ui
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from gapminder import gapminder
app_ui = ui.page_navbar(
            ui.nav_panel("A",
                        ui.h1("Home Page"),
                        ui.p("Boxplot of Life Expectancy v Continent"),
                        ui.output_plot("LifeBoxplot")
                        ),
            ui.nav_panel("B",
                        ui.h1("B"),
                        ui.p("Text on page B")
                        ),
            ui.nav_panel("C",
                        ui.h1("Gapminder Data Grid"),
                        ui.output_data_frame("GapData")
                        ),
                        position='fixed-bottom'
                        )
def server(input, output, session):
    @output
    @render.plot
    def LifeBoxplot():
        sns.boxplot(x = "continent", y = "lifeExp", data = gapminder)
        plt.ylabel("Life expectancy")

    @output
    @render.data_frame
    def GapData():
        return render.DataGrid(gapminder, filters = True)
    

app = App(app_ui, server)
