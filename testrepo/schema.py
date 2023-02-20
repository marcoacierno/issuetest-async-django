from dataclasses import dataclass
import strawberry

@strawberry.type
class AnotherLevel:
  @strawberry.field
  async def result(self) -> bool:
    return False


@strawberry.type
class Nested:
  another_level: AnotherLevel

@strawberry.type
class User:
  id: int

  @strawberry.field
  async def name(self) -> str:
    return f'Name {self.id}'

@dataclass
class OtherUserObject:
  id: int


@strawberry.type
class Query:
  @strawberry.field
  async def users(self) -> list[User]:
    return [
      OtherUserObject(id=id)
      async for id in UsersCounter()
    ]

  @strawberry.field
  def nested(self) -> Nested:
    return Nested(another_level=AnotherLevel())

  @strawberry.field
  async def value(self) -> bool:
    return True


schema = strawberry.Schema(query=Query)

class UsersCounter:
    def __init__(self):
        self.end = 5
        self.start = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.start < self.end:
            self.start += 1
            return self.start
        else:
            raise StopAsyncIteration
