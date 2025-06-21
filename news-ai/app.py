import streamlit as st
from datetime import date, timedelta
from src.fetch_news import fetch_news
from src.summarize import summarize_text

st.set_page_config(page_title="AI News Summarizer", layout="wide")

st.title("📰 AI-Powered News Summarizer")

st.markdown("Get concise, AI-generated summaries of the latest news from across the web. Enter keywords and let the summarizer do the rest.")

# --- Sidebar filters ---
st.sidebar.header("🔍 Filters")

query = st.sidebar.text_input("Keyword(s)", value="technology OR politics OR climate")

today = date.today()
default_start = today - timedelta(days=7)
from_date = st.sidebar.date_input("From Date", default_start)
to_date = st.sidebar.date_input("To Date", today)

with st.sidebar.expander("❓ How to use keywords"):
    st.markdown("""
- Use keywords to search for specific topics in article titles and descriptions.
- Combine terms with:
    - `AND`: e.g., `AI AND ethics`
    - `OR`: e.g., `cryptocurrency OR blockchain`
    - `NOT`: e.g., `inflation NOT oil`
- Use quotes for exact matches:
    - `"climate change"`
    - `"World Health Organization"`
    """)

num_articles = st.sidebar.slider("Number of Articles", 5, 30, 10)

run = st.sidebar.button("Fetch & Summarize")

# --- Main content ---
if run:
    with st.spinner("Fetching news articles..."):
        articles = fetch_news(
            query=query,
            from_date=from_date,
            to_date=to_date,
            language="en",
            page_size=num_articles
        )

    if not articles:
        st.warning("No articles found. Try adjusting the filters.")
    else:
        st.success(f"Found {len(articles)} article(s). Summarizing...")

        for idx, article in enumerate(articles, 1):
            st.markdown("---")
            st.markdown(f"### {idx}. [{article['title']}]({article['url']})")
            st.markdown(f"🗓️ Published: {article['publishedAt']} | 📰 Source: {article['source']}")

            with st.spinner("Generating summary..."):
                summary = summarize_text(article['content'])
            st.markdown(f"**🧠 Summary:** {summary}")