import dash
from dash import dcc, html, Dash
import plotly.express as px
import pandas as pd
import seaborn as sns
import requests
import json
import csv
from datetime import datetime

def get_data():
    """
    This function retrieves COVID-19 confirmed cases data for Singapore from a public API and returns it in JSON format.

    Args:
    None

    Returns:
    A JSON object containing COVID-19 confirmed cases data for Singapore from 2020-03-01 to today.
    The data includes the date, number of confirmed cases, and unique identifier for each record.

    """
    now = datetime.now().strftime("%y-%m-%d")
    url = "https://api.covid19api.com/country/singapore/status/confirmed/live?from=2020-03-01T00:00:00Z&to=" + now+ "T00:00:00Z"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()

def generate_dashboard():
    """
    Creates a Dash application for visualizing COVID19 analytics. It reads data from a CSV file, transforms it, and
    generates a graph showing the number of COVID19 cases per day from 1st March 2020 till today.

    Parameters: None

    Returns: A Dash application object.

    Algorithm:

    Reads data from "data.csv" file using pandas.
    Converts the "Date" column to a datetime format.
    Sorts the data by "Date" column.
    Creates a Dash application object.
    Defines the layout of the application with a title, a paragraph, and a graph.
    Configures the graph with data and layout.

    :return: Returns the Dash application object.
    """

    data = (
        pd.read_csv("data.csv")
            .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%Y-%m-%d"))
            .sort_values(by="Date")
    )

    app = Dash("COVID19 Reports")
    app.layout = html.Div(
        children=[
            html.H1(children="COVID19 Analytics"),
            html.P(
                children=(
                    "Graph of COVID19 cases from 1st March 2020 till today"
                ),
            ),
            dcc.Graph(
                figure={
                    "data": [
                        {
                            "x": data["Date"],
                            "y": data["Cases"],
                            "type": "lines",
                        },
                    ],
                    "layout": {"title": "Number of Cases per day"},
                },
            ),
        ]
    )
    return app

def convert_to_csv(data):
    """
    Converts a list of dictionaries to a CSV file.

    Args:
    data (list): A list of dictionaries containing data to be converted.

    Returns:
    None

    Output:
    A CSV file named "data.csv" containing the data in the input list of dictionaries.

    Example Usage:
    data = [{'name': 'John', 'age': 25, 'location': 'USA'}, {'name': 'Jane', 'age': 30, 'location': 'Canada'}]
    convert_to_csv(data)
    """
    csvfile = open("data.csv", "w")
    csvwriter = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)

    title = [item for item in data[0]]
    csvwriter.writerow(title)
    for dict in data:
        values = []
        for item in title:
            values.append(dict[item])
        csvwriter.writerow(values)


if __name__ == '__main__':
    """
    This code is the main driver code that executes the program. It first calls the get_data() function to 
    retrieve COVID19 data from an API and saves it in a CSV file using the convert_to_csv(data) function. 
    Then it generates a dashboard to display the data using the generate_dashboard() function. Finally,
     it runs the dashboard server in debug mode using the run_server() method of the app object. 
     The if __name__ == '__main__': statement ensures that this code block only runs if this script is executed as
      the main program.
    """
    data = get_data()
    convert_to_csv(data)
    app = generate_dashboard()
    app.run_server(debug=True)

