# visualizer.py
import os
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def plot_title_lengths(df):
    fig = px.histogram(df, x="title_length", nbins=10,
                       title="Distribution of Title Lengths")
    os.makedirs("outputs/graphs", exist_ok=True)
    fig_path = "outputs/graphs/title_length_plot.png"
    fig.write_image(fig_path)
    return fig_path

def plot_snippet_lengths(df):
    df["snippet_length"] = df["snippet"].apply(len)
    fig = px.histogram(df, x="snippet_length", nbins=10,
                       title="Distribution of Snippet Lengths")
    path = "outputs/graphs/snippet_length_plot.png"
    fig.write_image(path)
    return path

def plot_wordcloud(df):
    text = " ".join(df["title"].tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    path = "outputs/graphs/title_wordcloud.png"
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    os.makedirs("outputs/graphs", exist_ok=True)
    plt.savefig(path)
    plt.close()
    return path
