import graphene

from user_type import User
from user_data import users


class CreateUser(graphene.Mutation):
    class Arguments:
        id = graphene.String()
        name = graphene.String()
        email = graphene.String()

    user = graphene.Field(lambda: User)

    def mutate(root, info, id, name, email):
        user = User(id=id, name=name, email=email)
        users.append({
            "id": id,
            "name": name,
            "email": email
        })
        return CreateUser(user=user)


class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.String()
        name = graphene.String()
        email = graphene.String()

    user = graphene.Field(lambda: User)

    def mutate(root, info, id, name, email):
        user = User(id=id, name=name, email=email)
        old_user = list(filter(lambda user: user["id"] == id, users))[0]
        users.remove(old_user)
        users.append({
            "id": id,
            "name": name,
            "email": email
        })
        return UpdateUser(user=user)


class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.String()

    user = graphene.Field(lambda: User)

    def mutate(root, info, id):
        old_user = list(filter(lambda user: user["id"] == id, users))[0]
        user = User(id=old_user["id"], name=old_user["name"], email=old_user["email"])
        users.remove(old_user)
        return DeleteUser(user=user)
