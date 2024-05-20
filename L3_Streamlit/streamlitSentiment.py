import streamlit as st
import pandas as pd
from googlereviews import CSVProcessor
from PII.pii import TextAnalyzerService
from profanity_masker.main import profanity_masker
from sentiment_classifier.main import TextClassifier
import time
import matplotlib.pyplot as plt


# Step 1: Upload the CSV file
st.set_page_config(layout="wide")
st.title('📚 Sentiment Analysis on Google Reviews 📚')
uploaded_file = st.file_uploader("Upload your reviews file", type=["csv"])
if uploaded_file is not None:
    # Save the uploaded file
    csv_file_path = "reviews.csv"
    with open(csv_file_path, "wb") as f:
        f.write(uploaded_file.getvalue())

    # Step 2: Process the CSV file
    
    processor = CSVProcessor(csv_file_path)
    a = time.perf_counter()
    # columns_to_drop = ['business_name', 'author_name', 'photo', 'rating_category','rating']
    # processor.drop_columns(columns_to_drop)
    b = time.perf_counter()
    processor.save_to_csv("processed_reviews.csv")
    # preprocessing_time = time.perf_counter()

    # Step 3: Anonymize the text
    df = pd.read_csv("processed_reviews.csv")
    text_analyzer_service_model1 = TextAnalyzerService(model_choice="obi/deid_roberta_i2b2")
    anonymized_texts = []
    for index, row in df.iterrows():
        text = row[0]
        entities_model1 = text_analyzer_service_model1.analyze_text(text)
        anonymized_text, req_dict = text_analyzer_service_model1.anonymize_text(text, entities_model1, operator="encrypt")
        anonymized_texts.append(anonymized_text.text)
    df['Anonymized_Text'] = anonymized_texts
    c = time.perf_counter()
    df.to_csv("output_anonymized.csv", index=False)
    


    # Step 4: Mask profanity
    df = pd.read_csv("output_anonymized.csv")
    masker = profanity_masker()
    df['Masked_Text'] = df['Anonymized_Text'].apply(lambda text: masker.mask_words(text))
    df.to_csv("output_masked.csv", index=False)
    d = time.perf_counter()


    # Step 5: Classify the text
    start_time = time.perf_counter()
    df = pd.read_csv("output_masked.csv")
    checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
    classifier = TextClassifier(checkpoint)
    df['Classification_Result'] = df['Masked_Text'].apply(lambda text: classifier.infer(text))
    df.to_csv("output_classified.csv", index=False)
    end_time = time.perf_counter()

    # Calculate and display the total time taken
    total_time = end_time - a
    
    preprocessing_duration = b-a
    anonymization_duration = c-b
    masking_duration = d-c
    classification_duration = end_time - start_time
   

    # Display the processed, anonymized, masked, and classified files
    st.write("### 🔎 Processed Reviews")
    st.write(f"Total Reviews : 1100")
    st.dataframe(pd.read_csv("processed_reviews.csv"))
    

    st.write("### 🎭 Anonymized Reviews")
    st.write(f"Model Used: obi/deid_roberta_i2b2")
    st.write(f"Total Reviews : 1100")
    st.dataframe(pd.read_csv("output_anonymized.csv"))

    st.write("### 🙊 Profanity Masked Reviews")
    st.write(f"Library Used: better_profanity")
    st.write(f"Total Reviews : 1100")
    st.dataframe(pd.read_csv("output_masked.csv"))

    st.write("### 📊 Classified Results")
    st.write(f"Model Used: distilbert-base-uncased-finetuned-sst-2-english")
    st.write(f"Total Reviews : 1100")
    st.dataframe(pd.read_csv("output_classified.csv"))
    
    steps_info = pd.DataFrame({
    'Step': [ 'PII Anonymization', 'Profanity Masking', 'Sentiment Classification'],
    'Time Taken (s)': [anonymization_duration, masking_duration, classification_duration],
    'Time Taken/review (s)': [anonymization_duration/1100, masking_duration/1100, classification_duration/1100],
    'Model Name': ['obi/deid_roberta_i2b2', 'better_profanity', 'distilbert-base-uncased-finetuned-sst-2-english'],
    'Links': ['https://huggingface.co/obi/deid_roberta_i2b2', 'https://pypi.org/project/better-profanity', 'https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english']
    })
    
    st.markdown("--------------------------------------------------------------------------------------------------------------------------------------------------")

    # Display the DataFrame using Streamlit's st.table function
    st.write("### 🧮 Metrics")
    st.table(steps_info)

    # Display the total time taken
    st.write(f"Total Time: {total_time:.2f} seconds")
    
    # st.write(f"Total Time: {total_time:.2f} seconds")
