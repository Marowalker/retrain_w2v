import matplotlib.pyplot as plt

figure_counter = 0


def next_plot():
    global figure_counter
    figure_counter += 1
    plt.figure(figure_counter)


def show_figure(block=False):
    plt.show(block=block)
