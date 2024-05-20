from googlereviews import CSVProcessor
import pandas as pd
from PII.pii import TextAnalyzerService
from profanity_masker.main import profanity_masker
from sentiment_classifier.main import TextClassifier
import time
# Step 1: Use CSVProcessor to drop columns and save the processed file
start_time = time.perf_counter()
csv_file_path = "reviews.csv"
processor = CSVProcessor(csv_file_path)
columns_to_drop = ['business_name', 'author_name', 'photo', 'rating_category']
processor.drop_columns(columns_to_drop)
# Assuming the save_to_csv method exists and saves the processed file
processor.save_to_csv("processed_reviews.csv")
# -----------------------------------------------------------------------------------------
# Step 2: Read the processed file back into a DataFrame
df = pd.read_csv("processed_reviews.csv")

# Continue with DataFrame manipulations...
text_analyzer_service_model1 = TextAnalyzerService(model_choice="obi/deid_roberta_i2b2")
anonymized_texts = []
for index, row in df.iterrows():
    text = row[0] # Assuming the first column is the one you want to anonymize

    # Analyze text with the chosen model
    entities_model1 = text_analyzer_service_model1.analyze_text(text)

    # Anonymize text
    anonymized_text, req_dict = text_analyzer_service_model1.anonymize_text(text, entities_model1, operator="encrypt")
    anonymized_texts.append(anonymized_text.text)

df['Anonymized_Text'] = anonymized_texts 

# Save the updated DataFrame to a new CSV file
df.to_csv("output_anonymized.csv", index=False)
# ---------------------------------------------------------------------------------------------
df = pd.read_csv("output_anonymized.csv")

    # Initialize the profanity masker
masker = profanity_masker()

    # Define a function to apply the profanity masking to each entry in a given column
def mask_profanity(text):
    return masker.mask_words(text)

    # Apply the profanity masking to the specified column
df['Masked_Text'] = df['Anonymized_Text'].apply(mask_profanity)  

    # Save the DataFrame to a new CSV file
df.to_csv("output_masked.csv", index=False)
# ----------------------------------------------------------------------------------------------

df = pd.read_csv("output_masked.csv")

    # Initialize the text classifier
checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
classifier = TextClassifier(checkpoint)

    # Define a function to apply the text classification to each entry in a given column
def classify_text(text):
        return classifier.infer(text)

    # Define the column number to apply the classification
column_number = 3  # Change this to the column number where the text is located (0-based index)

    # Apply the text classification to the specified column

df['Classification_Result'] = df.iloc[:, column_number].apply(classify_text)
end_time = time.perf_counter()
total_time = end_time - start_time

    # Print the total time taken for classification
print("Total Time: ", "%.2f" % total_time, " seconds")

    # Save the DataFrame to a new CSV file
df.to_csv("output_classified.csv", index=False)