import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt 
from matplotlib.ticker import FuncFormatter
import seaborn as sns; sns.set()

def main(path):
    # read csv
    data = pd.read_csv(path)
    # get values
    y_values = data["Peso"]
    x_values = data["Data"]
    print(data)
    fig, ax = plt.subplots()
    # set title and labels
    ax.set_title("Peso x Tempo")
    ax.set_xlabel("Dias")
    ax.set_ylabel("Peso")
    def t(x, pos):
        print(x)
        print(pos)
        return x + pos
    # function to format labels
    fmt = lambda x, pos: "{}kg".format( x )
    # ticks
    ax.yaxis.set_major_formatter(FuncFormatter(fmt))
    # set y label
    ax.set_ylim(min(y_values)*0.99, max(y_values)*1.01)
    # plot values
    ax.plot(x_values, y_values)
    # show plot
    plt.show()


if __name__ == "__main__":
    main("weigths.csv")