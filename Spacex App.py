Last login: Thu May  4 21:19:49 on console
python 3

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
(base) 192:~ haochenli$ python 3
python: can't open file '3': [Errno 2] No such file or directory
(base) 192:~ haochenli$ python
Python 3.6.8 |Anaconda custom (64-bit)| (default, Dec 29 2018, 19:04:46) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> # Import required libraries
... import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

#print(spacex_df['Launch Site'].unique())

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',
                                             options=[
                               >>> import dash
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'dash'
>>> from dash import html
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'dash'
>>> from dash import dcc
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'dash'
>>> from dash.dependencies import Input, Output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'dash'
>>> import plotly.express as px
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'plotly'
>>> 
>>> # Read the airline data into pandas dataframe
... spacex_df = pd.read_csv("spacex_launch_dash.csv")
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "/Users/haochenli/anaconda3/lib/python3.6/site-packages/pandas/io/parsers.py", line 709, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "/Users/haochenli/anaconda3/lib/python3.6/site-packages/pandas/io/parsers.py", line 449, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/Users/haochenli/anaconda3/lib/python3.6/site-packages/pandas/io/parsers.py", line 818, in __init__
    self._make_engine(self.engine)
  File "/Users/haochenli/anaconda3/lib/python3.6/site-packages/pandas/io/parsers.py", line 1049, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "/Users/haochenli/anaconda3/lib/python3.6/site-packages/pandas/io/parsers.py", line 1695, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas/_libs/parsers.pyx", line 402, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas/_libs/parsers.pyx", line 718, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: File b'spacex_launch_dash.csv' does not exist
>>> max_payload = spacex_df['Payload Mass (kg)'].max()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spacex_df' is not defined
>>> min_payload = spacex_df['Payload Mass (kg)'].min()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spacex_df' is not defined
>>> 
>>> #print(spacex_df['Launch Site'].unique())
... 
>>> # Create a dash application
... app = dash.Dash(__name__)
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'dash' is not defined
>>> 
>>> # Create an app layout
... app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
...                                         style={'textAlign': 'center', 'color': '#503D36',
...                                                'font-size': 40}),
...                                 # TASK 1: Add a dropdown list to enable Launch Site selection
...                                 # The default select value is for ALL sites
...                                 dcc.Dropdown(id='site-dropdown',
...                                              options=[
...                                                     {'label': 'All Sites', 'value': 'ALL'},
...                                                     {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
...                                                     {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
...                                                     {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
...                                                     {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}],
...                                              value='ALL',
...                                              placeholder="State",
...                                              searchable=True
...                                             ),
...                                 html.Br(),
... 
...                                 # TASK 2: Add a pie chart to show the total successful launches count for all sites
...                                 # If a specific launch site was selected, show the Success vs. Failed counts for the site
...                                 html.Div(dcc.Graph(id='success-pie-chart')),
...                                 html.Br(),
... 
...                                 html.P("Payload range (Kg):"),
...                                 # TASK 3: Add a slider to select payload range
...                                 dcc.RangeSlider(id='payload-slider',
...                                                 min=0, max=10000, step=1000,
...                                                 marks={0: '0', 100: '100'},
...                                                 value=[min_payload, max_payload]),
... 
...                                 # TASK 4: Add a scatter chart to show the correlation between payload and launch success
...                                 html.Div(dcc.Graph(id='success-payload-scatter-chart')),
...                                 ])
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'html' is not defined
>>> 
>>> # TASK 2:
... # Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
... # Function decorator to specify function input and output
... @app.callback(Output(component_id='success-pie-chart', component_property='figure'),
...               Input(component_id='site-dropdown', component_property='value'))
... def get_pie_chart(entered_site):    
...     if entered_site == 'ALL':
...         fig = px.pie(spacex_df, 
...                      values='class', 
...                      names='Launch Site', 
...                      title='Total Success Launches By Site')        
...     else:
...         filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
...         filtered_df = filtered_df.groupby('class').count().reset_index()        
...         fig = px.pie(filtered_df, 
...                      values='Unnamed: 0', 
...                      names='class', 
...                      title='Total Launches for site {}'.format(entered_site))        
...         # return the outcomes piechart for a selected site
...     return fig
...         
... # TASK 4:
... # Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
... @app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
  File "<stdin>", line 24
    @app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
    ^
SyntaxError: invalid syntax
>>>               Input(component_id='site-dropdown', component_property='value'), 
  File "<stdin>", line 1
    Input(component_id='site-dropdown', component_property='value'), 
    ^
IndentationError: unexpected indent
>>>               Input(component_id="payload-slider", component_property="value"))
  File "<stdin>", line 1
    Input(component_id="payload-slider", component_property="value"))
    ^
IndentationError: unexpected indent
>>> def get_scatter_chart(entered_site, payload_range):
...     print('Params: {} {}'.format(entered_site, payload_range))
...     if entered_site == 'ALL':
...         filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= int(payload_range[0])) &
...                                 (spacex_df['Payload Mass (kg)'] <= int(payload_range[1]))
...                                ]
...         fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version Category', title='All sites - payload mass between {:8,d}kg and {:8,d}kg'.format(int(payload_range[0]),int(payload_range[1])))
...     else:
...         filtered_df = spacex_df[(spacex_df['Launch Site'] == entered_site) & 
...                                 (spacex_df['Payload Mass (kg)'] >= int(payload_range[0])) &
...                                 (spacex_df['Payload Mass (kg)'] <= int(payload_range[1]))
...                                ]
...         fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version Category', title='Site {} - payload mass between {:8,d}kg and {:8,d}kg'.format(entered_site,int(payload_range[0]),int(payload_range[1])))
...     
...     return fig
... 
>>> # Run the app
... if __name__ == '__main__':
...     app.run_server(debug=True)
