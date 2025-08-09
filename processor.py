# processor.py
import pandas as pd

def clean_news_data(news_list):
    df = pd.DataFrame(news_list)
    df.dropna(inplace=True)
    df["title_length"] = df["title"].apply(len)

    df.to_csv("outputs/cleaned_news.csv", index=False)
    return df
