import pandas as pd

class CSVProcessor:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.df = pd.read_csv(self.csv_file_path)

    def drop_columns(self, columns_to_drop):
        # Drop the specified columns
        self.df.drop(columns=columns_to_drop, inplace=True)

    def save_to_csv(self, output_file_path):
        # Save the updated DataFrame to a new CSV file
        self.df.to_csv(output_file_path, index=False)
        
    def get_dataframe(self):
        # Assuming the processed CSV is saved in a variable or a file
        # Read the processed CSV file back into a DataFrame
        return pd.read_csv(self.processed_csv_file_path)

if __name__ == "__main__":
    # Path to your CSV file
    csv_file_path = "reviews.csv"

    # List of columns to drop
    columns_to_drop = ['business_name', 'author_name', 'photo', 'rating_category'] # Replace with actual column names
    
    output_csv_file_path = "output.csv"

    # Create an instance of CSVProcessor
    processor = CSVProcessor(csv_file_path)

    # Drop the specified columns
    processor.drop_columns(columns_to_drop)

    # Save the updated DataFrame to a new CSV file
    processor.save_to_csv(output_csv_file_path)

    print(f"Updated CSV file saved as '{output_csv_file_path}'.")
