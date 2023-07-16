# Third party imports
from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

# Custom imports
from midlewares.jwt_bearer import JWTBearer
from services.movie_service import MovieService

# import database connection
from config.database import Session
from schemas.movie_schema import MovieSchema

# Create router app
movie_router = APIRouter()

# Endpoint for getting all movies
@movie_router.get("/movies", tags=["Movies"], response_model=List[MovieSchema], dependencies=[Depends(JWTBearer())])
def list_movies():
    result = MovieService(Session()).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


# Endpoint for getting movies by id
@movie_router.get("/movies/{id}", tags=["Movies"], response_model=MovieSchema)
def get_movie_by_id(id: int = Path(ge=1, le=100)):
    try:
        result = MovieService(Session()).get_movie(id)
        if not result:
            raise Exception
    except Exception:
        return JSONResponse(status_code=404, content={"Error": {"message": f"Cannot find movie_id {id}"}})
    else:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


# Endpoint for getting movies by query term
@movie_router.get("/movies/", tags=["Movies"], response_model=MovieSchema)
def get_movie_by_query(category: str = Query(min_length=2, max_length=15)):
    result = MovieService(Session()).query_movie(category)
    if not result:
        return JSONResponse(status_code=404, content={"Error": {"message": f"Cannot find query term by'{category}'"}})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


# Endpoint for creating movies
@movie_router.post("/movies/", tags=["Movies"], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def post_movie(movie: MovieSchema): # gets movie following MovieItem model
    try:
        MovieService(Session()).create_movie(movie)
    except Exception as exc:
       return {"Error": {"message": f"Cannot complete task! {exc}"}} 
    else:
        return {"Success": {"Message": "Movie created succesfully"}}


# Endpoint for updating a movie by id
@movie_router.put("/movies/{id}", tags=["Movies"], response_model=dict, dependencies=[Depends(JWTBearer())])
def put_movie(id: int, movie: MovieSchema):
    try:
       MovieService(Session()).update_movie(id, movie)
    except Exception as exc:
        return {"Error": {"message": f"Cannot complete task! {exc}"}} 
    else:
        return {"Success": {"Message": "Movie updated succesfully"}}


# Endpoint for deleting movie by id
@movie_router.delete("/movies/{id}", tags=["Movies"], response_model=dict, dependencies=[Depends(JWTBearer())])
def delete_movie(id: int):
    try:
        if not MovieService(Session()).delete_movie(id):
            raise Exception(f"Doesn´t exists movie {id}")
    except Exception as exc:
        return {"Error": {"message": f"Cannot complete task! {exc}"}} 
    else:
        return {"Success": {"message": f"Deleted movie_id {id}"}}