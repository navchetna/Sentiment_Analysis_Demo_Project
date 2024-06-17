from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from components.googlereviews import CSVProcessor
from components.PII.pii import TextAnalyzerService
from components.profanity_masker.main import profanity_masker
from components.sentiment_classifier.main import TextClassifier
import pandas as pd

app = FastAPI()

# Allowing CORS Headers
origins = ["http://localhost:3010", "*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# Root endpoint
@app.get('/')
async def root():
    return {'message': 'This is the root of the app'}

# Endpoint to upload file
@app.post('/upload')
async def upload(file: UploadFile = File(...)):
    try:
        # Read uploaded file
        contents = await file.read()
        with open("reviews.csv", "wb") as f:
            # Write contents of uploaded file to reviews.csv
            f.write(contents)
        return {"filename": file.filename}
    except Exception as e:
        # Handle errors during file upload
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to process CSV file
@app.get('/process_csv')
async def processCSV():
    try:
        # Process CSV file
        processor = CSVProcessor("reviews.csv")
        # Save processed data to processed_reviews.csv
        processor.save_to_csv("processed_reviews.csv")
        print("/process_csv: CSV processed successfully") #Log message
        return {"message": "CSV processed successfully"}
    except Exception as e:
        # Handle errors during CSV processing
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to anonymize CSV file
@app.get('/anonymise')
async def anonymise():
    try:
        # Read contents of processed_reviews.csv
        df = pd.read_csv("processed_reviews.csv")
        # Initialize TextAnalyzerService with specified model
        text_analyzer_service_model1 = TextAnalyzerService(model_choice="obi/deid_roberta_i2b2")
        anonymized_texts = []

        # Iterate over each row in the dataframe
        for _, row in df.iterrows():
            text = row[0]  # Extract the text from the first column
            # Analyze the text to identify entities
            entities_model1 = text_analyzer_service_model1.analyze_text(text)
            # Anonymize the text based on identified entities
            anonymized_text, _ = text_analyzer_service_model1.anonymize_text(text, entities_model1, operator="encrypt")
            # Append the anonymized text to the list
            anonymized_texts.append(anonymized_text.text)

        # Add the anonymized texts to the dataframe
        df['Anonymized_Text'] = anonymized_texts
        # Save the updated dataframe to output_anonymized.csv
        df.to_csv("output_anonymized.csv", index=False)
        print("/anonymise: Anonymization done successfully")  # Log message
        return {"message": "Anonymization done successfully"}
    except Exception as e:
        # Handle errors during anonymization
        raise HTTPException(status_code=500, detail=str(e))


# Endpoint to mask profanity in entries in CSV file
@app.get('/mask_profanity')
async def maskProfanity():
    try:
        # Read contents of output_anonymized.csv
        df = pd.read_csv("output_anonymized.csv")
        # Initialize profanity masker
        masker = profanity_masker()
        # Apply profanity masking to anonymized text
        df['Masked_Text'] = df['Anonymized_Text'].apply(lambda text: masker.mask_words(text))
        df.to_csv("output_masked.csv", index=False)
        print("/mask_profanity: Profanity masking done successfully") #Log message
        return {"message": "Profanity masking done successfully"}
    except Exception as e:
        # Handle errors during profanity masking
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to classify entries in CSV file
@app.get('/classify')
async def classify():
    try:
        # Read contents of output_masked.csv
        df = pd.read_csv("output_masked.csv")
        # Initialize text classifier with specified checkpoint
        checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
        classifier = TextClassifier(checkpoint)
        # Apply classification to masked text
        df['Classification_Result'] = df['Masked_Text'].apply(lambda text: classifier.infer(text))
        df.to_csv("output_classified.csv", index=False)
        print("/classify: Classification done successfully") #Log message
        return {"message": "Classification done successfully"}
    except Exception as e:
        # Handle errors during classification
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to download contents of CSV file
@app.get('/download')
async def download():
    # Specify the path of the file to download
    file_path = "output_classified.csv"
    return FileResponse(path=file_path, filename="output_classified.csv", media_type='text/csv')

# Endpoint to read data of CSV file
@app.get('/read-data')
async def readData():
    try:
        # Read contents of output_classified.csv
        df = pd.read_csv("output_classified.csv")
        # Convert dataframe to dictionary
        data = df.to_dict(orient='records')
        print("/read-data: Data read successfully") #Log message
        return data
    except Exception as e:
        # Handle errors during data reading
        raise HTTPException(status_code=500, detail=str(e))
