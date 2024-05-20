from main import TextClassifier
import pandas as pd
import time

if __name__ == "__main__":
    # Load the CSV file
    df = pd.read_csv("/home/develop/Project/profanity_masker/output_masked.csv")

    # Initialize the text classifier
    checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
    classifier = TextClassifier(checkpoint)

    # Define a function to apply the text classification to each entry in a given column
    def classify_text(text):
        return classifier.infer(text)

    # Define the column number to apply the classification
    column_number = 3  # Change this to the column number where the text is located (0-based index)

    # Apply the text classification to the specified column
    start_time = time.perf_counter()
    df['Classification_Result'] = df.iloc[:, column_number].apply(classify_text)
    end_time = time.perf_counter()
    total_time = end_time - start_time

    # Print the total time taken for classification
    print("Total Time: ", "%.2f" % total_time, " seconds")

    # Save the DataFrame to a new CSV file
    df.to_csv("output_classified.csv", index=False)

