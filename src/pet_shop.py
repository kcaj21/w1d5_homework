# WRITE YOUR FUNCTIONS HERE

import pdb

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

def get_pets_sold (sold):
    return sold["admin"]["pets_sold"]

def increase_pets_sold(total, sold):
    total["admin"]["pets_sold"] =+ sold
    
def get_stock_count(count):
    return len(count["pets"])

def get_pets_by_breed(petshop, breed):
    answer = []
    for pet in petshop["pets"]:
        if pet["breed"] == breed:
            answer.append(breed)
    return answer

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
          pet_shop["pets"].remove(pet)
    return pet_shop

def add_pet_to_stock(pet_shop, new_pet):
    count = len(pet_shop["pets"])
    pet_shop["pets"].append(new_pet)
    return count

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop, pet, customer):
