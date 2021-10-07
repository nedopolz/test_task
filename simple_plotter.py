import pandas as pd
import plotly.express as px


lines = pd.read_csv(r'data.csv', sep=';')
poses = lines['INTERNAL_ORG_ORIGINAL_RK'].unique()
poses = list(poses)
poses.sort()
poses = [str(i) for i in poses]
df = pd.read_csv(r'data_out.csv', sep=',', skiprows=0, index_col='Date/Pos')
fig = px.line(df, y=poses)
fig.show()



