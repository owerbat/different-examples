import os
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


if __name__ == '__main__':
    t = np.arange(start=0, stop=10, step=.01)
    signals = [
        np.random.rand() * np.sin(t) + np.random.rand() * np.cos(t)
        for _ in range(10)
    ]

    fig = make_subplots(rows=len(signals), cols=1)

    for i, signal in enumerate(signals):
        greater_idxs = np.squeeze(np.argwhere(t > 7.5))
        less_idxs = np.squeeze(np.argwhere(t < 2.5))
        other_idxs = np.squeeze(np.argwhere(np.logical_and(t <= 7.5, t >= 2.5)))

        fig.add_trace(go.Scatter(x=t[other_idxs], y=signal[other_idxs], name=f'signal {i + 1}'),
                      row=i + 1, col=1)
        fig.add_trace(go.Scatter(x=t[greater_idxs], y=signal[greater_idxs], name='',
                                 marker={'color': 'black'}, showlegend=False),
                      row=i + 1, col=1)
        fig.add_trace(go.Scatter(x=t[less_idxs], y=signal[less_idxs], name='',
                                 marker={'color': 'black'}, showlegend=False),
                      row=i + 1, col=1)

    fig.update_layout(height=150 * len(signals), width=800)

    results_dir = './results'
    os.makedirs(results_dir, exist_ok=True)
    fig.write_image(os.path.join(results_dir, 'multiple_plots.png'), scale=2)
