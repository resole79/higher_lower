import random
from art import *
from game_data import *


def random_player(list_of_vip):

    # data_len = len(list_of_vip) - 1

    choice_of_random_player = random.choice(list_of_vip)

    return choice_of_random_player


def define_player(vip):

    name = vip["name"]
    description = vip["description"]
    country = vip["country"]

    # vip_str = f"{name}, {description}, From: {country} "
    vip_str = f"{name}, {description}, From: {country}, {vip['follower_count']}"

    return vip_str


def compare(answer, vip1, vip2):
    get_answer = False
    if answer == "a":
        if vip1 >= vip2:
            get_answer = True
    elif answer == "b":
        if vip1 <= vip2:
            get_answer = True

    return get_answer


you_win = True
score = 0
player_a = random_player(data)
player_b = random_player(data)

while you_win:
    print(logo)

    while player_a == player_b:
        player_b = random_player(data)

    print(f"Player A: {define_player(player_a)}")
    print(vs)
    print(f"Player B: {define_player(player_b)}")

    ask_compare = input(f"Who has more follower? Type 'A' or 'B' : ").lower()
    followers_player_a = player_a["follower_count"]
    followers_player_b = player_b["follower_count"]
    # print(compare(ask_compare, followers_player_a, followers_player_b))
    if compare(ask_compare, followers_player_a, followers_player_b):
        print("You Win")
        player_a = player_b
        player_b = random_player(data)
        score += 1
    else:
        print("You Lose")
        you_win = False

    print(f"Your score is : {score}")
