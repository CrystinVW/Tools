import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Graphs:
    def __init__(self):
        self.x = 0

    def line_graph(self, x, data_y, color, label):
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)

        ax1.plot(x, data_y, 'b-', color=color, label=label)
        #ax1.plot(data_2_x, data_2_y, 'rx', color='blue', label='temperature')
        #ax1.set_ylabel('Density (cgs)', color='red', label='density')
        #ax1.set_ylabel('Temperature (K)', color='blue', label='temperature')
        ax1.set_xlabel('Time (s)')
        plt.rc('legend', fontsize='large')
        ax1.legend()
        plt.show()

    def side_by_side_line_graphs(self, x, title):

        df = pd.DataFrame(x)
        # Initialize the figure
        plt.style.use('seaborn-darkgrid')

        # create a color palette
        palette = plt.get_cmap('Set1')

        # multiple line plot
        num = 0
        for column in df.drop('x', axis=1):
            num += 1

            # Find the right spot on the plot
            plt.subplot(3, 3, num)

            # plot every groups, but discreet
            for v in df.drop('x', axis=1):
                plt.plot(df['x'], df[v], marker='', color='grey', linewidth=0.6, alpha=0.3)

            # Plot the lineplot
            plt.plot(df['x'], df[column], marker='', color=palette(num), linewidth=2.4, alpha=0.9, label=column)

            # Same limits for everybody!
            plt.xlim(0, 10)
            plt.ylim(-2, 22)

            # Not ticks everywhere
            if num in range(7):
                plt.tick_params(labelbottom='off')
            if num not in [1, 4, 7]:
                plt.tick_params(labelleft='off')

            # Add title
            plt.title(column, loc='left', fontsize=12, fontweight=0, color=palette(num))

        # general title
        plt.suptitle(title, fontsize=13, fontweight=0, color='black',
                     style='italic', y=1.02)

        # Axis title
        plt.text(0.5, 0.02, 'Time', ha='center', va='center')
        plt.text(0.06, 0.5, 'Note', ha='center', va='center', rotation='vertical')

        plt.show()


graph = Graphs()

'''t = np.linspace(0., 10., 100)
graph.two_lines(t, t ** 2, t, 1000 / (t + 1))

# Make a data frame
data = {'x': range(1, 11), 'y1': np.random.randn(10), 'y2': np.random.randn(10) + range(1, 11),
                   'y3': np.random.randn(10) + range(11, 21), 'y4': np.random.randn(10) + range(6, 16),
                   'y5': np.random.randn(10) + range(4, 14) + (0, 0, 0, 0, 0, 0, 0, -3, -8, -6),
                   'y6': np.random.randn(10) + range(2, 12), 'y7': np.random.randn(10) + range(5, 15),
                   'y8': np.random.randn(10) + range(4, 14), 'y9': np.random.randn(10) + range(4, 14)}
graph.side_by_side_line_graphs(data, "How the 9 students improved\nthese past few days?")'''
