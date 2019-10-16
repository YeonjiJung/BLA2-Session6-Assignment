#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:46:08 2019

@author: Yeonji
"""

import dash

import dash_core_components as dcc

import dash_daq as daq

import dash_html_components as html

from dash.dependencies import Input, Output

 

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

 

df = pd.read_csv("Performance_Data.csv")

X = df[df.columns.difference(['Paper 7'])]

Y = df['Paper 7']



 

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

 

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

 

regressor = LinearRegression() 

regressor.fit(X_train, Y_train)

 

 

 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

 

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server=app.server

 

app.layout = html.Div([

       

    html.H1('Student Essay Predictor'),

       

    html.Div([  

    html.Label('Paper 1 Score'),

    dcc.Slider(id='paper1-slider',

            min=0, max=100, step=1, value=60,

               marks={
                
        0: {'label': '0'},

        25: {'label': '25'},

        50: {'label': '50'},

        75: {'label': '75'},

        100: {'label': '100'}                            

    }),

 

html.Br(),

html.Label('Paper 2 Score'),

dcc.Slider(id='paper2-slider',

            min=0, max=100, step=1, value=60,

               marks={
                
        0: {'label': '0'},

        25: {'label': '25'},

        50: {'label': '50'},

        75: {'label': '75'},

        100: {'label': '100'}                            

    }),

 

html.Br(),

html.Label('Paper 3 Score'),

dcc.Slider(id='paper3-slider',

            min=0, max=100, step=1, value=60,

               marks={
                
        0: {'label': '0'},

        25: {'label': '25'},

        50: {'label': '50'},

        75: {'label': '75'},

        100: {'label': '100'}                            

    }),

 

html.Br(),

html.Label('Paper 4 Score'),

dcc.Slider(id='paper4-slider',

            min=0, max=100, step=1, value=60,

               marks={
                
        0: {'label': '0'},

        25: {'label': '25'},

        50: {'label': '50'},

        75: {'label': '75'},

        100: {'label': '100'}                            

    }),

 

html.Br(),

html.Label('Paper 5 Score'),

dcc.Slider(id='paper5-slider',

            min=0, max=100, step=1, value=60,

               marks={
                
        0: {'label': '0'},

        25: {'label': '25'},

        50: {'label': '50'},

        75: {'label': '75'},

        100: {'label': '100'}                            

    }),

 

html.Br(),

html.Label('Paper 6 Score'),

dcc.Slider(id='paper6-slider',

            min=0, max=100, step=1, value=60,

               marks={
                
        0: {'label': '0'},

        25: {'label': '25'},

        50: {'label': '50'},

        75: {'label': '75'},

        100: {'label': '100'}                            

    }),


],className="pretty_container four columns"),

 

  html.Div([

 

    daq.Gauge(

        id='paper7-gauge',

        showCurrentValue=True,

        color={"gradient":True,"ranges":{"red":[0,0.4],"yellow":[0.4,0.7],"green":[0.7,1]}},

        label="Probability",

        max=1,

        min=0,

        value=1

    ),

])

    ])

 

 

@app.callback(

    Output('paper7-gauge', 'value'),

    [Input('paper1-slider', 'value'),

     Input('paper2-slider', 'value'),

     Input('paper3-slider', 'value'),

     Input('paper4-slider', 'value'),

     Input('paper5-slider', 'value'),

     Input('paper6-slider', 'value')

     ])

def update_output_div(paper1,

                      paper2,

                      paper3,

                      paper4,

                      paper5,

                      paper6):

   X_case = pd.DataFrame({'Paper 1':[paper1],'Paper 2':[paper2],'Paper 3':[paper3],'Paper 4':[paper4],'Paper 5':[paper5],'Paper 6':[paper6]})

   Y_case = regressor.predict(X_case)

 

   return Y_case[0]

 

 

if __name__ == '__main__':

    app.run_server()
