FROM python:3.10

WORKDIR /usr/app

COPY PII/requirements.txt ./

RUN pip install -r requirements.txt

COPY profanity_masker/requirements.txt ./

RUN pip install -r requirements.txt

COPY sentiment_classifier/requirements.txt ./

RUN pip install -r requirements.txt

RUN pip install streamlit

COPY . /usr/app/

EXPOSE 8000

CMD [ "streamlit", "run", "streamlit.py", "--server.port", "8000" ]