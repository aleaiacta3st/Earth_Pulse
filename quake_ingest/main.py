from fetcher import fetch_earthquake_data 
from parser import parse_data 
from db import save_earthquakes, init_db
import asyncio 

async def ingest_data_loop():
    try:
        await init_db() #create database before entering the loop
        while True:
            data=await fetch_earthquake_data()
            parsed_data=parse_data(data)
            await save_earthquakes(parsed_data)
            await asyncio.sleep(300)
    except Exception as e:
        print(f"error: {e}")
        return []
    
if __name__ == "__main__":
    asyncio.run(ingest_data_loop())