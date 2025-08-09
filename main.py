# main.py 
from scraper import fetch_news
from processor import clean_news_data
from visualizer import plot_title_lengths, plot_snippet_lengths, plot_wordcloud
from summarizer import generate_summary

def run_pipeline():
    keyword = input("🔍 Enter a keyword to search: ").strip()
    print("\n📥 Fetching news...")
    news = fetch_news(keyword)

    if not news:
        print("❌ No news data found.")
        return

    print("🧼 Cleaning data...")
    df = clean_news_data(news)

    print("📊 Generating visualizations...")
    paths = []
    paths.append(plot_title_lengths(df))
    paths.append(plot_snippet_lengths(df))
    paths.append(plot_wordcloud(df))
    for p in paths:
        print(f"✅ Chart saved to {p}")

    print("🧠 Generating summary using OpenAI...")
    summary = generate_summary(df)
    print("\n📄 Insight Summary:")
    print(summary)

if __name__ == "__main__":
    run_pipeline()

# Sample input: Artificial Intelligence in Education 