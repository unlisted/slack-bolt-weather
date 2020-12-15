FROM python:3.9-slim
WORKDIR /app
COPY . ./
RUN pip install requests google-cloud-secret-manager slack-bolt

CMD python app.py
