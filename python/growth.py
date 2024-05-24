"""
PSIT Data Analysis Project
Chart: Growth of Video Games Amount
    PSIT Data Analysis Project
    Chart: Growth of Video Games Amount
    by Supakit Theanthunyakit (POKINBKK)
"""

import pandas, numpy, pygal
from pygal.style import CleanStyle
from project_module import project

data_frame = pandas.read_csv('vgsales.csv')
df_chage_platform = project.platform_convert_df(data_frame)
year_pf_list = numpy.array(df_chage_platform[['Year','Platform']]).tolist()

####################################################
df_change_platform = project.platform_convert_df(data_frame)
year_pf_list = numpy.array(df_change_platform[['Year','Platform']]).tolist()

def main():
    """ This is Main Function """
    df_chage_platform = project.platform_convert_df(data_frame)
    """ Main function """
    df_change_platform = project.platform_convert_df(data_frame)
    game_type = ['Home Video Game Consoles','Handheld Game Consoles', 'Microsoft Windows']
    game_in_years = numpy.array(data_frame.groupby('Year', as_index=False).count()[['Year', 'Rank']]).tolist()
    g_in_year = numpy.array(data_frame.groupby('Year', as_index=False).count()[['Year', 'Rank']]).tolist()
def main():

    #Create_Chart(amount_of_HVGC,amount_of_HHGC,amount_of_MSW)

####################################################

 def pf_count_by_all(platform):
    """ This Function for count Game in a specific Platform in Each year """
    """ Count game in a specific Platform in Each year """
    amount = []
    count = 0
    for i in range(1980, 2017):
         def pf_count_by_all(platform):
               amount.append(count)
    return amount

####################################################

def create_chart(hvgc, hhgc, msw):
    """ This Function for create chart """
    """ Create chart """
    chart = pygal.StackedBar(truncate_label=5, style=CleanStyle, fill=True, dots_size=1.75, interpolate='cubic')

    chart.x_title = 'Year'
