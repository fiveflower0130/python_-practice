import math
import os
import random
import re
import sys

# Complete the pangrams function below.


def pangrams(s):
    clean_s = s.replace(' ', '')
    clean_s = clean_s.lower()
    if clean_s.isalpha():
        if len(set(clean_s)) >= 26:
            return "pangram"
        else:
            return "not pangram"
    else:
        return "not pangram"

# test lib
# NOVmETKPTbYu ftZPEykhjgF GGkdGjWGwW skjPJsea dtwdqcr DERCUgxOxrRgDQbdzL IZjyXs
# YaCoVaGAaXxrzUvZ ZaHyacbUZCZUbZxzAYb YefxAwV yyABAdVatYazC TuyYYedxSf aA XBvSg EvYcl badDxvaZXWCyCUAaZvJcyc YdVbDYAdObgc FeCyxpdXxffubDbGAbFBxnzzT WzZ WcBZAaYCgYzseZb PYXbswxchtYIedhyaXtvzVxZSwWBLxxEaAaYAfGzybZzQo AH tCBcszyXZaAgwzYB QdVZBvwzAYbwwAVysxCRdTTT bXzxtWwyXZebEBYNBaDCLbZbwsEAB YTFBAcD bybU axAZAhhay ZkWydfxyGAeAYaZlabazUZssGTBcCXBr dWs XzyZAEzAAZyclC bCGzPfXcCccAFyvazX ZzYAB zAbsuCZADkeWwUuAbaZ zWCtYzgZZBzXXD c VsrbEaG aYYFZJBUlW iXqZxxswaWTJvb Y xuwebj CF zyZYZVdYYdaRyZ bTatyzYZw wVfaZEZauyZ A yo afJeCBAyVDXWBbAxYBzYyiNuWxBbexEcbeVaAqYz XAjawBzEqDzaafz bTaUaAzWYBxXWZzbazbUwYhqCdV DdzyWafztJajczbt CtYVVfzBgdtvXEGyBxy bdZz C xtczZ SZVfW ZCAx aZYDaa cCyZuVUEBGZ ACbawWXdxxLXa EawAgzOABYFbzTf TszVYaDc fACydzZYdAazSaaygBAYbGzdz yyYBYa Vasay xAz A AVWeYXY aTdYCcZIVxxHcWazZyaWaeYZybYUVZ Bu zXwgACWwzXzBaCwAVddb YB aYBBoGXUAcBZPbzVUGtX DeVduXZGXXtOBwagbXZAcDZIDZvTzA yyuUb AZ


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
