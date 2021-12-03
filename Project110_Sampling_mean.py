import pandas as pd
import plotly.figure_factory as pff
import statistics as st
import random

df = pd.read_csv("Data\medium_data.csv")
population_list = df["population"].tolist()

population_list_mean = st.mean(population_list)
print("The population mean is ", population_list_mean)
print("The population stdev is ", st.stdev(population_list))


def randon_set_of_mean(sample_size):
    data_set = []
    for i in range(0, sample_size):
        random_index = random.randint(0, len(population_list)-1)
        value = population_list[random_index]
        data_set.append(value)

    mean = st.mean(data_set)
    return(mean)


def plot_graph(mean_list):
    """ graph = pff.create_distplot([mean_list], ["population"], show_hist=False)
    graph.show()
 """

def setup():
    mean_list = []
    for i in range(0, 100):
        mean = randon_set_of_mean(30)
        mean_list.append(mean)
    plot_graph(mean_list)
    sampling_mean = st.mean(mean_list)

    print("mean for the sample data is ", sampling_mean)
    print("stdev for the sample data is ", st.stdev(mean_list))


setup()
