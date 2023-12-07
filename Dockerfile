FROM python:3.10

ENV PORT 5004


WORKDIR /app

ENV GOOGLE_APPLICATION_CREDENTIALS my-project-49747-407407-a262cca152e5.json
COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .


RUN echo "$(gcloud secrets versions access latest --secret=q1_secret)" > /app/q1-key-file.json

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app