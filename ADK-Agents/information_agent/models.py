from pydantic import BaseModel, Field


class StateOutput(BaseModel):
    name: str = Field(description="Name of user.")
    fav_color: str = Field(description="Favourite color of user.")
    fav_subject: str = Field(description="Favourite subject of user.")
