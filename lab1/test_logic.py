import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random
import time


available_palettes = {'TABLEAU_COLORS': mcolors.TABLEAU_COLORS,
                      'BASE_COLORS': mcolors.BASE_COLORS,
                      'CSS4_COLORS': mcolors.CSS4_COLORS,
                      'XKCD_COLORS': mcolors.XKCD_COLORS}


def load_df(test_group: int = None):
    df = pd.read_csv(r'J:\work\test_labs\lab1\preprocessed_results.csv')

    if test_group:
        df = df[df.number.round(0) == test_group]

    results = dict(df.result.value_counts(normalize=True).mul(100).round(1))
    labels, results = list(results.keys()), list(results.values())
    return labels, results


def draw_graphic(data, size=(16,9), legend=True, palette=''):
    labels, results = data

    if not palette or palette not in available_palettes:
        palette = random.choice(list(available_palettes.keys()))

    count_colors = len(labels)
    colors = random.sample(list(available_palettes[palette].values()), k=count_colors)

    fig, ax = plt.subplots(figsize=size)

    labels = [f'{label} — {result}%' for label, result in zip(labels, results)]

    ax.pie(results,
           colors=colors,
           wedgeprops={'edgecolor': '0',
                       'linewidth': 1,
                       'linestyle': 'solid',
                       'antialiased': True})
    ax.axis('equal')
    if legend:
        ax.legend(labels, bbox_to_anchor=(0.748, 1.025),loc='upper left')

    stime = time.time()
    path = rf'J:\work\test_labs\lab1\media\{stime}.jpg'
    fig.savefig(path)

    return path

