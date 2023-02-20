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
class Query:
  @strawberry.field
  def nested(self) -> Nested:
    return Nested(another_level=AnotherLevel())

  @strawberry.field
  async def value(self) -> bool:
    return True


schema = strawberry.Schema(query=Query)
