import simplejson as json
from analyze_data import Statistics
import matplotlib.pyplot as plt
import matplotlib.cm
import numpy as np
import pandas as pd
from plottable import Table
from plottable import ColumnDefinition
def read_data():
    marvel_plays = None
    with open("marvel_play_data.json") as play_data:
        marvel_plays = json.loads(play_data.read())

    statistics = Statistics(marvel_plays)
    statistics.analyze_play_data()
    return statistics



def hero_plays(statistics):
    #convert different dictionary for panda consumption
    frame_dict = { hero[1].name: [hero[1].total_plays, 
                                  hero[1].win_percentage*100, 
                                  hero[1].difficulty_data.standard1_win_percentage,
                                  hero[1].difficulty_data.expert1_win_percentage,
                                  hero[1].aspect_data.aspect_plays["Justice"].win_percentage,
                                  hero[1].aspect_data.aspect_plays["Leadership"].win_percentage,
                                  hero[1].aspect_data.aspect_plays["Aggression"].win_percentage,
                                  hero[1].aspect_data.aspect_plays["Protection"].win_percentage
                                  ] for hero in statistics.sorted_heroes}
    print(frame_dict)
    d = pd.DataFrame.from_dict(frame_dict, orient='index', columns =["Plays", 
                                                                     "Win %", 
                                                                     "S1 Win %", 
                                                                     "S1E1 Win %", 
                                                                     "Just Win %",
                                                                     "Lead Win %",
                                                                     "Aggr Win %",
                                                                     "Prot Win %"
                                                                     ]).round(2)
    #d = d.set_index("Hero")
    print(d)
    fig, ax = plt.subplots(figsize=(12, 10))
    tab = Table(d, column_definitions=[
        ColumnDefinition(name="Win %", cmap=matplotlib.cm.YlGn),
        ColumnDefinition(name="S1 Win %", cmap=matplotlib.cm.BuGn),
        ColumnDefinition(name="S1E1 Win %", cmap=matplotlib.cm.PuBuGn),
        ColumnDefinition(name="Just Win %", cmap=matplotlib.cm.Wistia),
        ColumnDefinition(name="Lead Win %", cmap=matplotlib.cm.Blues),
        ColumnDefinition(name="Aggr Win %", cmap=matplotlib.cm.Reds),
        ColumnDefinition(name="Prot Win %", cmap=matplotlib.cm.Greens)
        ])
    plt.show()
    fig.savefig("hero_plays.png")

stats = read_data()

hero_plays(stats)

