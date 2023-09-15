from graphene import ObjectType
from user_data import users


class Query(ObjectType):
    def resolve_get_user(root, info, id):
        return list(filter(lambda user: user["id"] == id, users))[0]

    def resolve_get_users(root, info):
        return users
