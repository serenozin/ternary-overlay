import pandas as pd
import plotly.graph_objects as go

textura = pd.read_csv("https://github.com/serenozin/ternary-overlay/raw/main/textura_solo%20.csv")
texturas = []
for i in range(0, len(textura.columns), 3):
    texturas.append([textura.iloc[:, i+x].dropna(axis=0) for x in range(3)])

colors=['#264653', '#2A9D8F', '#E9C46A',
    '#F4A261', '#E76F51',   '#388F85',
    '#D8BD78', '#E2A574', '#D47A63',
    '#547370', '#B9B097', '#B08F87',]

text = ['Areia', 'Areia franca', 'Franco arenoso',
        'Franco argilo siltosa','Argilo arenosa',
        'Argila', 'Franco argilosa',
        'Argilo siltosa', 'Franco argiloso siltosa',
        'Franco siltosa', 'Silte', 'Franca']

fig = go.Figure()

for i in range(len(texturas)):
    fig.add_trace(go.Scatterternary(
        name=text[i],
        a=texturas[i][0], b=texturas[i][1], c=texturas[i][2],
        mode= "lines",
        line=dict(width=0),
        fill='toself',
        fillcolor = colors[i],
        opacity=1,
    ))


fig.update_layout({
    'title': "Texturas do solo",
    'ternary':
        {
            'aaxis':{'title': 'Argila', 'min': 0.01, 'linewidth':2, 'ticks':'outside' },
            'baxis':{'title': 'Silte', 'min': 0.01, 'linewidth':2, 'ticks':'outside' },
            'caxis':{'title': 'Areia', 'min': 0.01, 'linewidth':2, 'ticks':'outside' }
        },
    'hoverlabel':{'bgcolor': "#000000"},

})
fig.show()