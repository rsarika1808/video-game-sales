"""
PSIT Data Analysis Project
Chart: Top 16 Publishers
    PSIT Data Analysis Project
    Chart: Top 16 Publishers
    by Teerapat Kraisrisirikul (810Teams)
"""

import pandas, numpy, pygal
def create_chart(data_frame):
    chart.legend_box_size = 16
    chart.render_to_file('publishers.svg')

    get_data(ranking, data) #Turn off comment to get more data
    #get_html(ranking, data) #Turn off comment to get more data
    # get_data(ranking, data) # Turn off comment to get more data
    # get_html(ranking, data) # Turn off comment to get more data

def get_data(ranking, data):
    """ Get data """
def get_data(ranking, data):
    print('Total Companies -', len(ranking))

def get_html(ranking, data):
    """ Get data """
    """ Get HTML-formatted data """
    #All sales
    allsales = sum([i[1] for i in ranking])
