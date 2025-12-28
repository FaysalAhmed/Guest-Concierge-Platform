FROM python:3.12 

WORKDIR /usr/src/app

RUN pip install fastapi uvicorn[standard] python-dotenv pydantic-settings

RUN pip install httpx python-multipart "pydantic[email]"

CMD sleep infinity 

