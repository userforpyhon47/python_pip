from fastapi import FastAPI

app = FastAPI()
CSV_FILE = "data.csv"

@app.get("/")
def get_data():
    return "This is a test"

@app.get("/test")
def get_data2():
    return "This is a test2"