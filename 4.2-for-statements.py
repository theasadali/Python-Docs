words = ['cat', 'tie', 'milk', 'shoes', 'egg', 'blanket']

for w in words:
    print(f'{w}, {len(w)}')


users_dict = {
    'user1': 'active',
    'user2': 'inactive',
    'user3': 'inactive',
    'user4': 'active',
    'user5': 'inactive'
}
print("--printing user dic before")
print(users_dict)
for user,status in users_dict.copy().items():
    if status == 'inactive':
        del(users_dict[user])
        print("--printing user dic after")
        print(users_dict)
