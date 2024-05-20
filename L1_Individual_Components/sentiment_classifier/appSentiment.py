import streamlit as st
import pandas as pd
from main import TextClassifier
import time

class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

# Set the page to wide layout
st.set_page_config(layout="wide")

# Initialize the profanity masker

# Streamlit app
st.title("📊 Sentiment Classification")

# Description table as a single dictionary
description_table = {
    "Component": "Sentiment Classification",
    "Category":"N/A",
}

description_table2 = {
    "Model": "distilbert-base-uncased-finetuned-sst-2-english",
    "property":"N/A",
}

message = """
component TextClassifier{
    service infer{
        /**
        * Performs sentiment analysis on the input text.
        *
        * @param input_text the text you want to analyse for sentiment.
        * @param sentiment predicted sentiment label for the input text ("NEGATIVE" or "POSITIVE").
        */

        [in] string input_text;
        [out] string sentiment;
        [out] int error_code;
    };
};
"""

# Display the table with all details in the first row
st.table(description_table)

st.write("Interface Definition Language (IDL)")
# Print the message with the same indentation and format
st.code(message, language='plaintext')

st.table(description_table2)

checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"

classification = TextClassifier(checkpoint)        

# Performance section
performance_expander = st.expander("Performance", expanded=False)
with performance_expander:
    warmup_criteria = st.number_input("Enter warmup criteria:", min_value=0, value=10, step=1)
    runs_criteria = st.number_input("Enter runs criteria:", min_value=1, value=100, step=1)
    if st.button("Start Runs"):
        # Load the CSV file
        sentences_df = pd.read_csv('reviews.csv') # Assuming 'sentences.csv' is the name of your CSV file
        # Extract the required number of sentences for warmup
        warmup_sentences = sentences_df['text'].head(warmup_criteria).tolist()
        
        # Perform masking during the warmup phase without displaying anything
        for sentence in warmup_sentences:
                result = classification.infer(sentence)

        
        # Prepare to collect metrics for the runs criteria loop
        total_time = 0
        sentence_times = []
        
        # Start the runs criteria loop
        start_time = time.time()
        for _ in range(runs_criteria):
            # Select a sentence for masking (you can modify this to use a different sentence for each run)
            sentence = sentences_df['text'].sample(1).iloc[0]
            result = classification.infer(sentence)

            
            # Start the timer for this run
            
            
            
            # Calculate performance metrics for this run
            
            
        total_time = time.time() - start_time
        # Calculate average time per sentence
        average_time_per_sentence = total_time / runs_criteria
        
        # Display the total time taken and the average time per sentence
        description_table1 = {
    "Total Time Taken": f"{total_time:.2f} seconds",
    "Average Time Per Sentence": f"{average_time_per_sentence:.2f} seconds",
}

        st.table(description_table1)
checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"

classification = TextClassifier(checkpoint)        

# Functionality section
functionality_expander = st.expander("Functionality", expanded=False)
with functionality_expander:
    user_input = st.text_input("Enter your sentence here:")
    if st.button("📊 Classify"):
        if user_input:
            result = classification.infer(user_input)

            st.write("Sentiment:")
            st.write(result)
        else:
            st.write("Please enter a sentence.")
