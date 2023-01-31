### Multiple For Loops
dict_1={'AAA1': 11, 'AAA2': 12, 'AAA3': 13}
dict_2={'BBB1': 21, 'BBB2': 22, 'BBB3': 23}
dict_3={'CCC1': 31, 'CCC2': 32, 'CCC3': 33}

import itertools

for a,b,c in itertools.product(dict_1, dict_2, dict_3):
    print (a,b,c)
