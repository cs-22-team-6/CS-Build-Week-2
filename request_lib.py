from decouple import config
import requests
from time import sleep


def room_init():
    """
    Init call to determine the room you are in. 
    """
    # curl request
    url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/'
    token = config('TOKEN')
    headers = {'Authorization': f'Token {token}'}
    r = requests.get(url, headers=headers)
    # get return data
    ret_data = r.json()
    # get cooldown
    cd = ret_data['cooldown']
    # sleep to prevent PEBCAK
    sleep(cd+1)
    # return JSON
    return ret_data

def move_north(direction):
    """
    Simple move function
    """
    # curl request
    url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/move/'
    token = config('TOKEN')
    headers = {"Content-Type": "application/json",
               'Authorization': f'Token {token}'}
    data = '{"direction":"n"}'
    r = requests.post(url, headers=headers, data=data)
    # get return data
    ret_data = r.json()
    # get cooldown
    cd = ret_data['cooldown']
    # sleep to prevent PEBCAK
    sleep(cd+1)
    # return JSON
    return ret_data

def move_south():
    """
    Simple move function
    """
    # curl request
    url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/move/'
    token = config('TOKEN')
    headers = {"Content-Type": "application/json",
               'Authorization': f'Token {token}'}
    data = '{"direction":"s"}'
    r = requests.post(url, headers=headers, data=data)
    # get return data
    ret_data = r.json()
    # get cooldown
    cd = ret_data['cooldown']
    # sleep to prevent PEBCAK
    sleep(cd+1)
    # return JSON
    return ret_data

def move_east():
    """
    Simple move function
    """
    # curl request
    url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/move/'
    token = config('TOKEN')
    headers = {"Content-Type": "application/json",
               'Authorization': f'Token {token}'}
    data = '{"direction":"e"}'
    r = requests.post(url, headers=headers, data=data)
    # get return data
    ret_data = r.json()
    # get cooldown
    cd = ret_data['cooldown']
    # sleep to prevent PEBCAK
    sleep(cd+1)
    # return JSON
    return ret_data

def move_west():
    """
    Simple move function
    """
    # curl request
    url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/move/'
    token = config('TOKEN')
    headers = {"Content-Type": "application/json",
               'Authorization': f'Token {token}'}
    data = '{"direction":"w"}'
    r = requests.post(url, headers=headers, data=data)
    # get return data
    ret_data = r.json()
    # get cooldown
    cd = ret_data['cooldown']
    # sleep to prevent PEBCAK
    sleep(cd+1)
    # return JSON
    return ret_data

def move(direction):
    """
    Refactored move function
    """
    # curl request
    url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/move/'
    token = config('TOKEN')
    headers = {"Content-Type": "application/json",
               'Authorization': f'Token {token}'}
    data = '{"direction":"'+direction+'"}'
    r = requests.post(url, headers=headers, data=data)
    # get return data
    ret_data = r.json()
    # get cooldown
    cd = ret_data['cooldown']
    # sleep to prevent PEBCAK
    sleep(cd+1)
    # return JSON
    return ret_data

def wise_move(direction, room):
    """
    Wise move function
    """
    # curl request
    room = str(room)
    url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/move/'
    token = config('TOKEN')
    headers = {"Content-Type": "application/json",
               'Authorization': f'Token {token}'}
    data = '{"direction":"'+direction+'", "next_room_id": "'+room+'"}'
    r = requests.post(url, headers=headers, data=data)
    # get return data
    ret_data = r.json()
    # get cooldown
    cd = ret_data['cooldown']
    # sleep to prevent PEBCAK
    sleep(cd+1)
    # return JSON
    return ret_data

def fly(direction):
    """
    Fly Function. Needs power
    """
    # curl request
    url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/fly/'
    token = config('TOKEN')
    headers = {"Content-Type": "application/json",
               'Authorization': f'Token {token}'}
    data = '{"direction":"'+direction+'"}'
    r = requests.post(url, headers=headers, data=data)
    # get return data
    ret_data = r.json()
    # get cooldown
    cd = ret_data['cooldown']
    # sleep to prevent PEBCAK
    sleep(cd+1)
    # return JSON
    return ret_data

def dash(direction, room_list):
    """
    Dash function. Needs power
    """
    # get number of rooms
    n_rooms = str(len(room_list))
    # make sure we get strings
    rooms = [str(item) for item in room_list]
    # turn into 1 string
    rooms = ",".join(rooms)
    # # curl request
    url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/dash/'
    token = config('TOKEN')
    headers = {"Content-Type": "application/json",
               'Authorization': f'Token {token}'}
    data = '{"direction":"'+direction+'", "num_rooms":"'+n_rooms+'", "next_room_ids": "'+rooms+'"}'
    r = requests.post(url, headers=headers, data=data)
    # get return data
    ret_data = r.json()
    # get cooldown
    cd = ret_data['cooldown']
    # sleep to prevent PEBCAK
    sleep(cd+1)
    # return JSON
    return ret_data

def take_item(item):
    """
    Pickup item
    """
    # curl request
    url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/take/'
    token = config('TOKEN')
    headers = {"Content-Type": "application/json",
               'Authorization': f'Token {token}'}
    data = '{"name":"'+item+'"}'
    r = requests.post(url, headers=headers, data=data)
    # get return data
    ret_data = r.json()
    # get cooldown
    cd = ret_data['cooldown']
    # sleep to prevent PEBCAK
    sleep(cd+1)
    # return JSON
    return ret_data

def drop_treasure(item):
    """
    Drop item
    """
    # curl request
    url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/drop/'
    token = config('TOKEN')
    headers = {"Content-Type": "application/json",
               'Authorization': f'Token {token}'}
    data = '{"name":"'+item+'"}'
    r = requests.post(url, headers=headers, data=data)
    # get return data
    ret_data = r.json()
    # get cooldown
    cd = ret_data['cooldown']
    # sleep to prevent PEBCAK
    sleep(cd+1)
    # return JSON
    return ret_data

def get_player_status():
    """
    gets player attributes and inventory
    """
    # curl request
    url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/status/'
    token = config('TOKEN')
    headers = {"Content-Type": "application/json",
               'Authorization': f'Token {token}'}
    r = requests.post(url, headers=headers)
    # get return data
    ret_data = r.json()
    # get cooldown
    cd = ret_data['cooldown']
    # sleep to prevent PEBCAK
    sleep(cd+1)
    # return JSON
    return ret_data  

def equip(name):
    """
    NEED TO TEST
    """
    # curl request
    url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/wear/'
    token = config('TOKEN')
    headers = {"Content-Type": "application/json",
               'Authorization': f'Token {token}'}
    data = '{"name":"'+[name]+'"}'
    r = requests.post(url, headers=headers, data=data)
    # get return data
    ret_data = r.json()
    # get cooldown
    cd = ret_data['cooldown']
    # sleep to prevent PEBCAK
    sleep(cd+1)
    # return JSON
    return ret_data

def unequip(name):
    """
    NEED TO TEST
    """
    # curl request
    url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/undress/'
    token = config('TOKEN')
    headers = {"Content-Type": "application/json",
               'Authorization': f'Token {token}'}
    data = '{"name":"'+[name]+'"}'
    r = requests.post(url, headers=headers, data=data)
    # get return data
    ret_data = r.json()
    # get cooldown
    cd = ret_data['cooldown']
    # sleep to prevent PEBCAK
    sleep(cd+1)
    # return JSON
    return ret_data

def examine(name):
    """
    Examine player or item
    """
    # curl request
    url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/'
    token = config('TOKEN')
    headers = {"Content-Type": "application/json",
               'Authorization': f'Token {token}'}
    data = '{"name":"'+name+'"}'
    r = requests.post(url, headers=headers, data=data)
    # get return data
    ret_data = r.json()
    # get cooldown
    cd = ret_data['cooldown']
    # sleep to prevent PEBCAK
    sleep(cd+1)
    # return JSON
    return ret_data

def sell_treasure(treasure):
    """
    Sell tresure at the shop
    """
    # curl request
    url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/'
    token = config('TOKEN')
    headers = {"Content-Type": "application/json",
               'Authorization': f'Token {token}'}
    data = '{"name":"'+treasure+'", "confirm": "yes"}'
    r = requests.post(url, headers=headers, data=data)
    # get return data
    ret_data = r.json()
    # get cooldown
    cd = ret_data['cooldown']
    # sleep to prevent PEBCAK
    sleep(cd+1)
    # return JSON
    return ret_data

def pray():
    """
    pray at a shrine
    """
    # curl request
    url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/pray/'
    token = config('TOKEN')
    headers = {"Content-Type": "application/json",
               'Authorization': f'Token {token}'}
    r = requests.post(url, headers=headers)
    # get return data
    ret_data = r.json()
    # get cooldown
    cd = ret_data['cooldown']
    # sleep to prevent PEBCAK
    sleep(cd+1)
    # return JSON
    return ret_data

def change_name(name):
    """
    Change player name. Must be at special shrine
    """
    # curl request
    url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/'
    token = config('TOKEN')
    headers = {"Content-Type": "application/json",
               'Authorization': f'Token {token}'}
    data = '{"name":"'+name+'"}'
    r = requests.post(url, headers=headers, data=data)
    # get return data
    ret_data = r.json()
    # get cooldown
    cd = ret_data['cooldown']
    # sleep to prevent PEBCAK
    sleep(cd+1)
    # return JSON
    return ret_data

def carry(name):
    """
    NEED TO TEST
    """
    # curl request
    url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/carry/'
    token = config('TOKEN')
    headers = {"Content-Type": "application/json",
               'Authorization': f'Token {token}'}
    data = '{"name":"'+[name]+'"}'
    r = requests.post(url, headers=headers, data=data)
    # get return data
    ret_data = r.json()
    # get cooldown
    cd = ret_data['cooldown']
    # sleep to prevent PEBCAK
    sleep(cd+1)
    # return JSON
    return ret_data

def receive(name):
    """
    NEED TO TEST
    """
    # curl request
    url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/wear/'
    token = config('TOKEN')
    headers = {"Content-Type": "application/json",
               'Authorization': f'Token {token}'}
    data = '{"name":"'+[name]+'"}'
    r = requests.post(url, headers=headers, data=data)
    # get return data
    ret_data = r.json()
    # get cooldown
    cd = ret_data['cooldown']
    # sleep to prevent PEBCAK
    sleep(cd+1)
    # return JSON
    return ret_data