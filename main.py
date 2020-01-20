import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt 
from matplotlib.ticker import FuncFormatter
import seaborn as sns; sns.set()

def main(path):
    # read csv
    data = pd.read_csv(path)
    # get values
    y_values = data["Peso"].values
    x_values = data["Data"].values
    print(data)

    fig, axes = plt.subplots(2, 1)

    # set title and labels
    axes[0].set_ylabel("Peso")
    # function to format labels
    fmt = lambda x, pos: "{}kg".format( round(x, 1) )
    # ticks
    #axes[0].yaxis.set_major_formatter(FuncFormatter(fmt))
    # set y label
    axes[0].set_ylim(min(y_values)*0.99, max(y_values)*1.01)
    # plot values
    axes[0].plot(x_values, y_values)

    # set title and labels
    axes[1].set_xlabel("Dias")
    axes[1].set_ylabel("Variação")
    # function to format labels
    fmt = lambda x, pos: "{}kg".format( x )
    # ticks
    #axes[1].yaxis.set_major_formatter(FuncFormatter(fmt))
    # set y label
    #axes[1].set_ylim(min(y_values)*0.99, max(y_values)*1.01)
    #variation = y_values[1:] - y_values[:-1]
    #print(variation)
    # plot values
    axes[1].plot(x_values[1:], y_values[1:] - y_values[:-1])

    # show plot
    plt.show()


if __name__ == "__main__":
    main("weigths.csv")