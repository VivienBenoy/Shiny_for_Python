from shiny import App, render, ui
import matplotlib.pyplot as plt
import numpy as np

app_ui = ui.page_fluid(
    ui.input_slider("n", "Sample Size", 0, 1000, 20),ui.output_plot("dist"))
def server(input, output, session):
    @render.plot
    def dist():
        x = np.random.randn(input.n())
        plt.hist(x, range=[-3, 3])
        
app = App(app_ui, server)