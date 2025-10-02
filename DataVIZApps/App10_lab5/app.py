from shiny import App, render, ui
import matplotlib.pyplot as plt
import numpy as np
from gapminder import gapminder
import plotly.express as px
from shinywidgets import output_widget, render_widget
from gapminder import gapminder


app_ui = ui.page_fluid(
            ui.navset_pill_list(
                ui.nav_panel("Seaborn",
                ui.h1("Home Page"),
                ui.p("Scatterplot of Life Expectancy v GDP"),
                output_widget("plotly_scatter")
                ),
                ui.nav_panel("Plotly",
                ui.h1("Gapminder Founder"),
                ui.input_text("label", "Label the image below"),
                ui.output_image("hans"),
                ui.output_text("print_text")
                )
            )
        )

def server(input, output, session):
    @output
    @render.text
    def scatter():
        sns.scatterplot(x='gdpPercap',y='lifeExp',data=gapminder)
        plt.title('Scatter plot of life expectancy VS GDP')
app = App(app_ui, server)