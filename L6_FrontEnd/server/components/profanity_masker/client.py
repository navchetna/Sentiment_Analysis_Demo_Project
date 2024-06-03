from main import profanity_masker
import pandas as pd

if __name__ == "__main__":
    # Load the CSV file
    df = pd.read_csv("/home/develop/Project/PII/output_anonymized.csv")

    # Initialize the profanity masker
    masker = profanity_masker()

    # Define a function to apply the profanity masking to each entry in a given column
    def mask_profanity(text):
        return masker.mask_words(text)

    # Apply the profanity masking to the specified column
    df['Masked_Text'] = df['Anonymized_Text'].apply(mask_profanity)  # Replace 'Column_Name' with the actual column name

    # Save the DataFrame to a new CSV file
    df.to_csv("output_masked.csv", index=False)
