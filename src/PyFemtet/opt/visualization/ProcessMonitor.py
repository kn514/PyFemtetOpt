# import numpy as np
# import pandas as pd

# import plotly.graph_objs as go
# import plotly.express as px

# import dash
# from dash import dcc, html
# from dash.dependencies import Output, Input



# # pairplot(scatter matrix)

# def create_scatter_matrix_fig(FEMOpt):
    


# class MultiobjectiveProcessMonitor:

#     def __init__(self, FEMOpt):
#         # 引数の処理
#         self.FEMOpt = FEMOpt
        
#         # application の準備
#         self.app = dash.Dash(__name__)

#         # figure の準備
#         fig = px.scatter_matrix(
#             df,
#             dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"],
#             )




#         graph1 = dcc.Graph(id='scatter-graph', animate=False)
#         graph2 = dcc.Graph(id='pairplot-graph', animate=False)
#         interval_component = dcc.Interval(
#             id='interval',
#             interval=2*1000,
#             n_intervals=0
#             )
#         self.app.layout = html.Div([graph1, graph2, interval_component])

#         # # decolator を書き下す形で callback を設定
#         # self.app.callback(
#         #     dash.dependencies.Output('hv', 'figure'),
#         #     dash.dependencies.Input('interval', 'n_intervals')
#         #     )(self.update_hv)
#         # self.app.callback(
#         #     dash.dependencies.Output('pp', 'figure'),
#         #     dash.dependencies.Input('interval', 'n_intervals')
#         #     )(self.update_pp)
#         @self.app.callback(
#             Output('pairplot-graph', 'figure'),
#             Input('interval', 'n_intervals')
#             )
#         def update_pp(_):
#             return self.update_pp()

#         @self.app.callback(
#             Output('scatter-graph', 'figure'),
#             Input('interval', 'n_intervals')
#             )
#         def update_hv(_):
#             return self.update_hv()


    
#     def start(self):
#         self.app.run_server(debug=True, host='localhost', port=8050)
#         import webbrowser
#         webbrowser.open("http://localhost:8050")

#     def update_hv(self):
#         df = self.FEMOpt.history
#         fig = go.Figure()
#         x = df['n_trial']
#         y = df['hypervolume']
#         fig.add_trace(go.Scatter(x=x, y=y, mode='lines'))
#         fig.update_layout(
#             xaxis_range=[0, x.max()*1.1],
#             yaxis_range=[0, y.max()*1.1],
#             )
#         return fig

        
#     def update_pp(self):
#         # https://plotly.com/python/splom/
#         df = self.FEMOpt.history

#         obejctive_names = self.FEMOpt.get_history_columns('objective')
#         parameter_names = self.FEMOpt.get_history_columns('parameter')
#         index_vals = df['non_domi'].astype('category').cat.codes

#         # fig = go.Figure(
#         #     data=go.Splom(
#         #         dimensions=[dict(label=column, values=df[column]) for column in obejctive_names],
#         #         showupperhalf=False,
#         #         diagonal_visible=False,
#         #         text=df[parameter_names],
#         #         marker=dict(
#         #             color=index_vals,
#         #             showscale=False, # colors encode categorical variables
#         #             line_color='white',
#         #             line_width=0.5
#         #             )
#         #         )
#         #     )
#         # fig.update_layout(
#         #     title='pp',
#         #     # width=600,
#         #     # height=600,
#         # )

#         fig = px.scatter_matrix(
#             df,
#             dimensions=obejctive_names,
#             color="non_domi",
#             symbol="non_domi",
#             title="Scatter matrix",
#             )
#         fig.update_traces(
#             diagonal_visible=False,
#             showupperhalf=False,
#             )
#         return fig
    
# if __name__=='__main__':
#     class DummyFEMOpt:
#         def __init__(self):
#             self.history = pd.DataFrame(
#                 dict(
#                     n_trials=np.arange(10),
#                     obj1=np.random.rand(10),
#                     obj2=np.random.rand(10),
#                     obj3=np.random.rand(10),
#                     prm1=np.random.rand(10),
#                     prm2=np.random.rand(10),
#                     non_domi=np.random.rand(10)>0.5,
#                     )
#                 )
#         def get_history_columns(self, kind):
#             if kind=='parameter':
#                 return ['prm1', 'prm2']
#             if kind=='objective':
#                 return ['obj1', 'obj2', 'obj3']
#     dpm = DashProcessMonitor(DummyFEMOpt())
#     dpm.start()