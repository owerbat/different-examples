import os
import numpy as np
import plotly.graph_objects as go


if __name__ == '__main__':
    n = 1000
    distr1 = np.random.normal(0, 2, n)
    distr2 = np.random.normal(5, 2, n)

    fig = go.Figure()

    fig.add_trace(go.Histogram(x=distr1, name='distr1', nbinsx=30))
    fig.add_trace(go.Histogram(x=distr2, name='distr2', nbinsx=30))
    fig.add_vline(x=2.5, line_dash="dash", annotation_text='2.5')

    fig.update_layout(barmode='overlay',
                      xaxis_title_text='Value',
                      yaxis_title_text='Count')
    fig.update_traces(opacity=0.75)

    results_dir = './results'
    os.makedirs(results_dir, exist_ok=True)
    fig.write_image(os.path.join(results_dir, 'hists.png'), scale=2)
