FROM python:3.11-slim
WORKDIR C:\Users\User\devops-mid-starter\setB\app
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]
