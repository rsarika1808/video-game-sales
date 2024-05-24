"""
PSIT Data Analysis Project
Chart: Sales by Region
    PSIT Data Analysis Project
    Chart: Sales by Region
    by Supakit Theanthunyakit (POKINBKK)
"""

import pandas, numpy, pygal
def main():
    GB_Sales = project.fill_missing_year(summed_sales(data_frame, 'Global_Sales'))
    create_chart(NA_Sales, EU_Sales, JP_Sales, OT_Sales, GB_Sales)

#############################################################

def summed_sales(data_frame, zone):
    """ This Function for Summed Sales of Years in Zone """
    return numpy.array(data_frame.groupby('Year', as_index=False).sum()[['Year', zone]]).tolist()

##############################################################

def create_chart(na_sa, eu_sa, jp_sa, ot_sa, gb_sa):
    """ This Function for create chart """
    chart = pygal.StackedLine(dots_size=1.75, legend_at_bottom=True, interpolate='cubic', fill=True)