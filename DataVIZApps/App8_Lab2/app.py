from shiny import App, render, ui
import matplotlib.pyplot as plt
import numpy as np
from gapminder import gapminder

app_ui = ui.page_fluid(
    ui.input_slider("lifeExp", "lifeExp", 20, 90, 20),ui.output_data_frame("grid"))
def server(input, output, session):
    @output
    @render.data_frame
    def grid():
        return render.DataGrid(gapminder)
        
app = App(app_ui, server)