import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    print(item.dict(), type(item.dict()))
    # print(**item.dict)
    func(**item.dict())
    return {"item_id": item_id, **item.dict()}


def func(name,description,price,tax):
    print(name,description,price,tax)

if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000)
