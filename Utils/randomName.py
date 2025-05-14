import random
def RandomName() :
    constellation_name = ["Ari","Tau","Gem","Can","Leo","Vir","Lib","Sco","Sag","Cap","Aqu","Pis","Ori","Urs","Lyr"]
    constellation = random.choice(constellation_name)
    random_numbers = random.randint(0, 999)
    random_numbers_str = f"{random_numbers:03}"
    name = f"{constellation}{random_numbers_str}"
    return name

    
