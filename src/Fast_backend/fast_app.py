from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

filtered_content = [
    {
    "link": "https://vk.com/sergeyiss?w=wall-101948711_41719",
    "platform_source_enum": "vk",
    "source": "https://vk.com/sergeyiss",
}
]

source = ["https://vk.com/sergeyiss"]

# another_content = {
#     "link" : "https://vk.com/sergeyiss?w=wall-220432188_284",
#     "platform_source_enum": "vk",
#     "source": "https://vk.com/sergeyiss",
# }




@app.get("/asd", summary="Главная ручка", tags=["Основные ручки"])
def main():
    return "Hello World!"


@app.get("/filtered_content", summary="Получить отфильрованный контент", tags=["Ручки конента"])
def get_filter_contents():
    return filtered_content


class NewContent(BaseModel):
    link: str | None
    platform_source_enum: str
    source: str



@app.post("/filtered_content", summary="Добавить отфильтрованный контент", tags=["Ручки конента"])
def create_content(another_content: NewContent):
    filtered_content.append(another_content)
    return {"sucsess" : filtered_content}



if __name__ == "__main__":
    uvicorn.run("fast_app:app", reload=True)