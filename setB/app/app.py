import os
from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host=os.environ.get("REDIS_HOST", "localhost"), port=6379, decode_responses=True)


@app.route("/")
def home():
    return f"Service ready for {os.environ.get('STUDENT', 'unknown')}"


@app.route("/visit")
def visit():
    count = r.incr("visits")
    return f"Visit count: {count}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    #Sadaf Iqbal
    #Changes made
