from fastapi import FastAPI 
from fastapi.responses import HTMLResponse
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    print("Starting up...")
    yield
    # Shutdown actions
    print("Shutting down...")   


app = FastAPI(lifespan=lifespan)    

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello, World!</h1>"

