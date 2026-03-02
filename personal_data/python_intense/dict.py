#Encontrar Elementos chave

def number_of_friends(user):
    user_id = user["id"]
    friend_ids = friendship[user_id]
    return len(friend_ids)

users = [
{"id" : 0, "name" : "Hero"},
{"id" : 1, "name" : "Carla"},
{"id" : 2, "name" : "Pedro"},
{"id" : 3, "name" : "João"},
{"id" : 4, "name" : "Maria"},
{"id" : 5, "name" : "Fernanda"},
{"id" : 6, "name" : "Roberto"},
{"id" : 7, "name" : "Geremias"},
{"id" : 8, "name" : "Rafael"},
]

friendship_pairs = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4)
                   (4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

#lista vazia para id de users
friendship = {user["id"]:[] for user in users} 

for i,j in friendship_pairs:
    friendship_pairs[i].append(j)
    friendship_pairs[j].append(i)

total_connections = sum(number_of_friends(users)
                        for user in users)

