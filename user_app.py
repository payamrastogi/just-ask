import graphene
from user_mutation import CreateUser, UpdateUser, DeleteUser
from user_query import Query
from user_type import User


class MyMutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()


class MyQuery(Query):
    user = graphene.Field(User)
    get_user = graphene.Field(User, id=graphene.String())
    get_users = graphene.List(User)


schema = graphene.Schema(query=MyQuery, mutation=MyMutations)

# result = schema.execute(
#     '''
#     mutation {
#         createUser(id: "1", name: "John Doe", email : "john@gmail.com"){
#             user {
#                 id
#                 name
#             }
#         }
#     }
#     '''
# )
#
# print(result.data)


result = schema.execute(
    '''
    mutation {
        updateUser(id: "1", name: "John Doe", email : "john@outlook.com"){
            user {
                id
                name
            }
        }
    }
    '''
)

print(result.data)

result = schema.execute(
    '''
    query {
        getUsers {
            id
            email
        }
    }
    '''
)

print(result.data)


result = schema.execute(
    '''
    query {
        getUser(id: "1") {
            id
            email
        }
    }
    '''
)

print(result.data)
