from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_len=120, min_len=30):
    if len(text.strip()) == 0:
        return "No content to summarize."

    try:
        summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)[0]['summary_text']
        return summary
    except Exception as e:
        return f"Error during summarization: {e}"