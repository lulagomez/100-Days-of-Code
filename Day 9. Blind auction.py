# OLD CODE (New code proposal below)
# ********


#  from replit import clear

# from art import logo
# print(logo)
# dict = {}

# def add_list():
#     again = True
#     while again == True:
#         name = input("What's your name? ")
#         bid = int(input("Whats your bid? $"))
#         dict[name] = bid
#         ag = input("Is there another bid? yes/no: ")
#         if ag == "yes":
#             clear()
#             again = True
#         else:
#             clear()
#             again = False
    
# add_list()

# winner = 0
# for item in dict:
#     print(dict[item])
#     if dict[item] > winner:
#         winner = dict[item]
#         print(winner)
# for key in dict:
#     if dict[key] == winner:
#         print(f"The winner is {key} with ${dict[key]}")        


dict = {}

def add_bid():
    again = True
    while again == True:
        name = input("What's your name? ")
        bid = int(input("Whats your bid? $"))
        dict[name] = bid
        ag = input("Is there another bid? yes/no: ")
        if ag == "yes":
            again = True
        else:
            again = False
    
add_bid()

# We transform the dict's keys into lists. 
# We use max to get the max value in the values' list, then use index to get it's position and use this to retrieve the winner (matching max bid and participant)
print(f"The winner is: {list(dict.keys())[list(dict.values()).index(max(list(dict.values())))]}")