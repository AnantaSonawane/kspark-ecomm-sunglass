from fastapi import FastAPI
from sunglass import Sunglass

app = FastAPI()
sunglass_list = []

@app.get("/")
def home():
    print(f"home:{home} inside home function")
    return {"message": "Welcome to the Ananta's Sunglass shop!"}


@app.post("/new-sunglass")
def add_new_sunglass(sunglass: Sunglass):
    print(f"inside add new sunglass method")
    sunglass_list.append(sunglass.dict())
    return sunglass_list

@app.get("/sunglass")
async def get_sunglass():
    print(f"Inside get_sunglass function...")
    return {"available_sunglass": sunglass_list}
