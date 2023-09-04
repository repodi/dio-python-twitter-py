from typing import List

import uvicorn
from fastapi import FastAPI
from src.ConfigurationLoader import ConfigurationLoader as configuration

from src.responses import TrendItem
from src.services import get_trends, save_trends

app = FastAPI()


@app.get("/trends", response_model=List[TrendItem])
def get_trends_route():
    return get_trends()


if __name__ == "__main__":
    trends = get_trends()

    print(trends) 

    if not trends:
        save_trends()

    HOST = configuration.get_value(section="UVICORN",key="host")
    PORT = configuration.get_value(section="UVICORN",key="port")
    uvicorn.run(app, host=HOST, port=int(PORT))
