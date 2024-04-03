import simplejson as json
from analyze_data import Statistics
import matplotlib.pyplot as plt
import matplotlib.cm
import numpy as np
import pandas as pd
from plottable import Table
from plottable.formatters import decimal_to_percent
from plottable.plots import circled_image
from plottable import ColumnDefinition
from pathlib import Path
def read_data():
    marvel_plays = None
    with open("marvel_play_data.json") as play_data:
        marvel_plays = json.loads(play_data.read())

    statistics = Statistics(marvel_plays)
    statistics.analyze_play_data()
    return statistics

def get_hero_image_filename(name):

    filename = ""
    if name == "Sp//der":
        filename = "peni_parker.png"
    elif " " in name:
        filename = name.replace(' ', '_').replace('.','').lower() + ".png"
    else:
        filename = name.lower() + ".png"
    
    return Path("/home/jgatkinsn/Dropbox/Photos/Marvel_Champions_Tier_List/Heroes/modded") / filename

def hero_plays(statistics):
    #convert different dictionary for panda consumption
    frame_dict = { hero[1].name: [
                                  get_hero_image_filename(hero[1].name),
                                  hero[1].total_plays, 
                                  hero[1].win_percentage, 
                                  hero[1].difficulty_data.standard1_win_percentage,
                                  hero[1].difficulty_data.expert1_win_percentage,
                                  hero[1].aspect_data.aspect_plays["Justice"].win_percentage,
                                  hero[1].aspect_data.aspect_plays["Leadership"].win_percentage,
                                  hero[1].aspect_data.aspect_plays["Aggression"].win_percentage,
                                  hero[1].aspect_data.aspect_plays["Protection"].win_percentage
                                  ] for hero in statistics.sorted_heroes}
    print(frame_dict)
    d = pd.DataFrame.from_dict(frame_dict, orient='index', columns =["Image",
                                                                     "Plays", 
                                                                     "Win %", 
                                                                     "S1", 
                                                                     "S1E1", 
                                                                     "Justice",
                                                                     "Leadership",
                                                                     "Aggression",
                                                                     "Protection"
                                                                     ]).round(2)
    #d = d.set_index("Hero")
    print(d)
    fig, ax = plt.subplots(figsize=(12, 10))
    # see https://matplotlib.org/stable/users/explain/colors/colormaps.html for colormap options
    tab = Table(d, column_definitions=[
        ColumnDefinition(name="index", title="Heroes", textprops={"ha":"left", "weight":"bold"}),
        ColumnDefinition(name="Image", title="", textprops={"ha":"right"}, width=1, plot_fn=circled_image),
        ColumnDefinition(name="Plays", group="Overall"),
        ColumnDefinition(name="Win %", group="Overall", formatter=decimal_to_percent, cmap=matplotlib.cm.YlGn),
        ColumnDefinition(name="S1", group="Difficulty Win %", formatter=decimal_to_percent, cmap=matplotlib.cm.BuGn),
        ColumnDefinition(name="S1E1", group="Difficulty Win %", formatter=decimal_to_percent, cmap=matplotlib.cm.PuBuGn),
        ColumnDefinition(name="Justice", group="Aspect Win %",  formatter=decimal_to_percent, cmap=matplotlib.cm.Wistia),
        ColumnDefinition(name="Leadership", group="Aspect Win %",  formatter=decimal_to_percent, cmap=matplotlib.cm.Blues),
        ColumnDefinition(name="Aggression", group="Aspect Win %",  formatter=decimal_to_percent, cmap=matplotlib.cm.Reds),
        ColumnDefinition(name="Protection", group="Aspect Win %",   formatter=decimal_to_percent,cmap=matplotlib.cm.Greens)
        ])
    plt.show()
    fig.savefig("hero_plays.png")

stats = read_data()

hero_plays(stats)

