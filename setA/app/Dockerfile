FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Agar aapki file ka naam apps.py hai:
COPY apps.py .

EXPOSE 5000

# Agar entry point apps.py hai toh yahan bhi wahi dein:
CMD ["python", "apps.py"]