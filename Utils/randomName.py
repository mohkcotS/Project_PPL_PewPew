import random
def RandomName() :
    constellation_name = ["ari","tau","gem","can","leo","vir","lib","sco","sag","cap","aqu","pis","ori","urs","lyr"]
    constellation = random.choice(constellation_name)
    random_numbers = random.randint(0, 999)
    random_numbers_str = f"{random_numbers:03}"
    name = f"{constellation}{random_numbers_str}"
    return name

    
