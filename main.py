
import pandas as pd

def weekly_average_grapher(country):

    df1 = pd.read_csv(country + '_Weekly_average_data_Cases.csv')
    df2 = pd.read_csv(country + '_Weekly_average_data_Mobility.csv')

    print(df1)
    print(df2)

    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates

    fig = plt.figure(figsize=(14, 5))
    fig.subplots_adjust(left=0.1, right=0.9)

    plt.plot(df2['date_time_for_mobility'], df2['average_mobility_7'], 'g')

    plt2 = plt.twinx()
    plt2.plot(df1['date_time'], df1['average_cases_7'], 'r')

    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=10))
    ax2 = plt.gca()
    ax2.xaxis.set_major_locator(mdates.DayLocator(interval=10))
    plt.savefig(country + '_the_graph.png')

weekly_average_grapher('Australia')
weekly_average_grapher('Brazil')
weekly_average_grapher('Denmark')
weekly_average_grapher('Colombia')
weekly_average_grapher('Canada')
weekly_average_grapher('Poland')
weekly_average_grapher('Romania')