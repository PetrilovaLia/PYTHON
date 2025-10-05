# program s nahodnymi cislami

import random

def hadz_dvomi_kockami():
    prva = random.randint(1, 6)
    druha = random.randint(1, 6)
    print('hodil si', prva, 'a', druha, 'a ich sucet je', prva + druha)

hadz_dvomi_kockami()
