from shiny import App, render, ui
import matplotlib.pyplot as plt
import numpy as np
from gapminder import gapminder

app_ui = ui.page_fluid(
    ui.input_selectize(
    'continent',
    'Select Continent',
    'continent',
    selected='Europe',
    multiple=True
    ),ui.output_plot('scatter'))

def server(input, output, session):
    @output
    @render.text
    def scatter():
        sns.scatterplot(x='gdpPercap',y='lifeExp',data=gapminder)
        plt.title('Scatter plot of life expectancy VS GDP')
app = App(app_ui, server)