import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="2shiori17", age=21)


schema = strawberry.Schema(Query)
# TODO(2shiori17): https://github.com/strawberry-graphql/strawberry/issues/2711#issuecomment-1507607945
graphql_app = GraphQLRouter[object, object](schema)

api = FastAPI()
api.include_router(graphql_app, prefix="/graphql")
