# main.py - il primo server: a chi dice «ping» rispondiamo «pong»
from fastapi import FastAPI
# 1. creiamo l'applicazione, cioè il server
app = FastAPI()

# 2. quando arriva una richiesta GET all'indirizzo /ping, rispondiamo pong
@app.get("/pong") # /decoratore che serve a definire una rotta (route)
def ping():
    return {"risposta": "ping"}