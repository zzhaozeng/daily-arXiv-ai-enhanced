from pydantic import BaseModel, Field

class Structure(BaseModel):
  task: str = Field(description="describe the task in this paper in one sentence")
  motivation: str = Field(description="describe the motivation in this paper")
  method: str = Field(description="method of this paper")
  result: str = Field(description="result of this paper")
  conclusion: str = Field(description="conclusion of this paper")