#Use Python 3.9 image
FROM python:3.9

#Set working directory
WORKDIR /app

#Install required dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

#Copy code file into container
COPY . .

# Start flask app
CMD ["python", "app.py"]
