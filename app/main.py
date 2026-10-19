from fastapi import FastAPI

#server create.
app = FastAPI(title = "Student API")

@app.get("/")
def home():
    return{
        "message" : "Welcome to student API"
    }
@app.get("/health")
def home2():
    return{
        "message" : "server is healthy"
    }