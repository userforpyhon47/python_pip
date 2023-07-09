from pydantic import BaseModel, Field

class User(BaseModel):
    username: str 
    passwd: str

class MovieItem(BaseModel):
    id: int = Field(default=0)
    title: str = Field(min_length=5, max_length=30, default="Movie title here")
    overview: str = Field(min_length=5, max_length=120, default="Movie overview here")
    year: int = Field(default=1900, le=2022)
    rating: float = Field(default=10.0, le=10, ge=0)
    category: str = Field(min_length=5, max_length=60, default="Movie category here")