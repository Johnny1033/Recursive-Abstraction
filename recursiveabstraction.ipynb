import boto3
import nltk
import openai
import pandas as pd
from io import StringIO

# Constants and configurations
bucket_name = 'your-bucket-name'
s3_filename = 'book_to_summarize'
openai.api_key = 'your-api-key'
s3 = boto3.client('s3')
comprehend = boto3.client('comprehend', region_name='us-west-2')

# Function to detect sentiment scores using Amazon Comprehend
def detect_sentiment_scores(text):
    response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    scores = response['SentimentScore']
    return scores

# Function to detect named entities (names and places) using Amazon Comprehend
def detect_entities(text):
    response = comprehend.detect_entities(Text=text, LanguageCode='en')
    entities = response['Entities']
    names_and_places = [entity['Text'] for entity in entities if entity['Type'] in ['PERSON', 'LOCATION']]
    return ', '.join(names_and_places)

# Constants and configurations
bucket_name = 'your-bucket-name'
s3_filename = 'book_to_summarize'
openai.api_key = 'your-api-key'
s3 = boto3.client('s3')
comprehend = boto3.client('comprehend', region_name='us-west-2')

# Function to detect sentiment using Amazon Comprehend
def detect_sentiment(text):
    response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    return response['Sentiment']

# Read the original file from S3
file_obj = s3.get_object(Bucket=bucket_name, Key=s3_filename)
file_content = file_obj['Body'].read().decode('utf-8')

# Tokenize the text using the NLTK library
tokens = nltk.word_tokenize(file_content)

# Split the tokens into chunks of 750
chunks = [tokens[i:i + 750] for i in range(0, len(tokens), 750)]

# Functions
def generate_summary(text, prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{prompt}:\n\n{text}"}
        ],
        max_tokens=2500,
        n=1,
        temperature=0.7,
    )
    summary = response.choices[0].message.content.strip()
    return summary

def generate_meta_summary(summaries):
    text = "\n\n".join(summaries)
    prompt = "Create a meta summary of these summaries"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{prompt}:\n\n{text}"}
        ],
        max_tokens=2500,
        n=1,
        temperature=0.7,
    )
    meta_summary = response.choices[0].message.content.strip()
    return meta_summary

def process_text_chunk(bucket_name, chunk, counter):
    filename = f'book_url_chunk{counter}.txt'

    # Write the chunk to a temporary file
    with open(filename, 'w') as f:
        f.write(' '.join(chunk))

    # Upload the file to S3
    s3.upload_file(Filename=filename, Bucket=bucket_name, Key=filename)

    # Get the file content
    file_obj = s3.get_object(Bucket=bucket_name, Key=filename)
    file_content = file_obj['Body'].read().decode('utf-8')

    # Generate chunksummary
    prompt = "Create a summary of this text"
    chunksummary = generate_summary(file_content, prompt)

    return (filename, chunksummary)

# Process each chunk and generate chunk summary
chunksummaries = [process_text_chunk(bucket_name, chunk, i) for i, chunk in enumerate(chunks)]

# Convert the chunk summaries into a pandas DataFrame
chunksummaries_df = pd.DataFrame(chunksummaries, columns=['File', 'ChunkSummary'])

# Analyze sentiment and sentiment scores for each chunk summary
chunksummaries_df['Sentiment'] = chunksummaries_df['ChunkSummary'].apply(detect_sentiment)
chunksummaries_df['SentimentScores'] = chunksummaries_df['ChunkSummary'].apply(detect_sentiment_scores)

# Detect named entities (names and places) for each chunk summary
chunksummaries_df['NamesAndPlaces'] = chunksummaries_df['ChunkSummary'].apply(detect_entities)

# Create metasummary for each group of 4 chunk summaries
chunksummaries_list = chunksummaries_df['ChunkSummary'].tolist()
meta_summaries = create_meta_summaries(chunksummaries_list, 4)

# Save each meta summary as a separate text file
for i, meta_summary in enumerate(meta_summaries):
    meta_summary_filename = f'metasummary_{i}.txt'
    
    # Write the meta summary to a text file
    with open(meta_summary_filename, 'w') as f:
        f.write(meta_summary)
    
    # Upload the meta summary text file to S3
    s3.upload_file(Filename=meta_summary_filename, Bucket=bucket_name, Key=meta_summary_filename)

# Save the DataFrame to a CSV file and upload it to S3
csv_buffer = StringIO()
chunksummaries_df.to_csv(csv_buffer, index=False)
s3.put_object(Bucket=bucket_name, Key='summary_sentiment_analysis.csv', Body=csv_buffer.getvalue())

print('Summary and meta summary generation complete')