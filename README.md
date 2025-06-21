# 📰 AI News Summarizer

An AI-powered web app that fetches the latest news from around the web and generates concise, human-readable summaries using advanced NLP models.

## 🚀 Features

- 🔍 **Keyword-based Search**: Search for any topic using flexible query syntax (`AND`, `OR`, `"quotes"`, etc.)
- 📰 **Real-time News Fetching**: Pulls headlines from over 80,000 trusted sources via NewsAPI
- 🧠 **AI Summarization**: Uses `facebook/bart-large-cnn` from HuggingFace to generate readable summaries
- 📅 **Date Range Selection**: Filter articles by publication date
- 🧼 **Clean Interface**: Built using Streamlit for simplicity and speed

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** – web app UI
- **NewsAPI** – for fetching real-time news
- **Transformers (Hugging Face)** – for summarization (`facebook/bart-large-cnn`)
- **dotenv** – for securely managing API keys

🔑 Environment Variables (Required)
Create a .env file in the root directory and add your own NewsAPI key. You can get a free key from https://newsapi.org/.
⚠️ Note: This app will not work unless you supply your own NewsAPI key.

🧠 Model Notes
Uses the facebook/bart-large-cnn model, optimized for English summarization.
If you want multilingual support, consider upgrading to OpenAI or mT5-based models.

Made by Mikhail Belkin
