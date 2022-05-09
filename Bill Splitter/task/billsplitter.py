party_dict = {}
friend_list = []

print("Enter the number of friends joining the party:")
num_friends = int(input())
if num_friends <= 0:
    print("No one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    for i in range(num_friends):
        friend_list.append(input())
    party_dict = dict.fromkeys(friend_list, 0)
    print(party_dict)


