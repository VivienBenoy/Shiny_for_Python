from shiny import App, render, ui
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
import pandas as pd
from gapminder import gapminder


app_ui = ui.page_fluid(
    ui.input_numeric("numeric", "Life Expectancy", 100, min=1, max=1703))

def server(input, output, session):
    @output
    @render.text
    def value():
        return input.numeric()

    @output
    @render.plot
    def dist():
       df=gapminder
       sns.hist(x='lifeExp', data=df)
       plt.title(' Life Expectancy ')


        
app = App(app_ui, server)
