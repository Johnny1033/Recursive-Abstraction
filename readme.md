Book Summarizer and Sentiment Analyzer

This Python script downloads a book from a URL, divides the book into smaller chunks, and generates summaries for each chunk using GPT-3.5-turbo from OpenAI. It then analyzes the sentiment and sentiment scores for each summary using Amazon Comprehend, detects named entities (names and places), and creates a meta summary for each group of 4 summaries. The final summary, sentiment analysis, and meta summaries are saved to an S3 bucket.

Prerequisites

To run the script, you need:

An AWS account with S3 and Comprehend services access
The boto3, nltk, openai, pandas, matplotlib, and requests libraries installed

Usage

Set up your AWS credentials using the official AWS guide.
Replace your_bucket_name with the name of the S3 bucket where you want to store the results.
Replace your_api_key with your OpenAI API key.
Optionally, change the book_url variable to the URL of the book or text file you want to summarize.

How it works

The script performs the following steps:

Downloads the book from the provided URL and saves it to the specified S3 bucket.
Tokenizes the book text using the NLTK library and divides it into smaller chunks.
Processes each chunk by generating a summary using GPT-3.5-turbo from OpenAI.
Analyzes the sentiment and sentiment scores for each summary using Amazon Comprehend.
Detects named entities (names and places) in each summary using Amazon Comprehend.
Creates a meta summary for each group of 4 summaries.
Saves the summary, sentiment analysis, and meta summaries to the specified S3 bucket as text files and a CSV file.
Visualizes the sentiment scores for each chunk using a line chart.

Output

The script generates:

A summary and a meta summary for each group of 4 summaries, saved as separate text files in the S3 bucket.
A CSV file containing the summary, sentiment analysis, and named entities detection for each chunk, saved in the S3 bucket.
A line chart visualizing the sentiment scores for each chunk.