"""
This module is responsible for visualising the data retrieved from a database using Matplotlib.
"""

"""
Task 28 - 30: Write suitable functions to visualise the data as follows:

- Display the top 5 countries for confirmed cases using a pie chart
- Display the top 5 countries for death for specific dates using a bar chart
- Display a suitable (animated) visualisation to show how the number of confirmed cases, deaths and recovery change over
time. This could focus on a specific country/countries.

Each function for the above should utilise the functions in the module 'database' to retrieve any data.
You may add additional methods to the module 'database' if needed. Each function should then visualise
the data using Matplotlib.
"""

# TODO: Your code here

import database
import matplotlib.pyplot as plt


def top5_countries_confirmed():
    ax = database.top_confirmed_cases()
    x1, x2, x3, x4, x5 = ax[0][0], ax[1][0], ax[2][0], ax[3][0], ax[4][0]
    y1, y2, y3, y4, y5 = ax[0][1], ax[1][1], ax[2][1], ax[3][1], ax[4][1]
    # sizes = []
    # labels = []
    # for t in countries:
    #     x, y, z = t
    #     labels.append(x)
    #     sizes.append(z)
    labels = (x1, x2, x3, x4, x5)
    values = [y1, y2, y3, y4, y5]
    exp = [0, 0.1, 0, 0, 0]
    plt.pie(values, labels=labels, autopct='%0.1f%%', explode=exp)
    plt.title("Top 5 countries with confirmed cases")
    plt.show()

