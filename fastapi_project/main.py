# Third party imports
from fastapi import FastAPI

# Custom imports
from midlewares.error_handler import ErrorHandler
from routers.movie_router import movie_router
from routers.user_router import user_router


# import database connection
from config.database import engine, Base

# Create database tables for the database engine
Base.metadata.create_all(bind=engine)

# Create application
app = FastAPI()
app.add_middleware(ErrorHandler) # Add error handler to avoid app crashing
app.include_router(user_router) # Add movie router
app.include_router(movie_router) # Add movie router

# Configure Swagger API title and version
app.title = "Documentation for my API"
app.version = "0.1"
