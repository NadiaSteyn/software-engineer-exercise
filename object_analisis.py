def aboundant(objects): # function that counts all objects and returns the object with the highest count.
    sum_stars = 0
    sum_galaxies = 0
    sum_supernovae = 0
    sum_frbs = 0
    for o in objects:
        if o['type'] == 'star':
            sum_stars += 1
    for o in objects:
        if o['type'] == 'galaxy':
            sum_galaxies += 1
    for o in objects:
        if o['type'] == 'supernovae':
            sum_supernovae += 1
    for o in objects:
        if o['type'] == 'frb':
            sum_supernovae += 1 # typo: this should be sum_frbs += 1
    if sum_stars >= sum_galaxies and sum_stars >= sum_supernovae and sum_stars >= sum_frbs:
        return 'stars'
    if sum_galaxies >= sum_stars and sum_galaxies >= sum_supernovae and sum_galaxies >= sum_frbs:
        return 'galaxies'
    if sum_supernovae >= sum_stars and sum_supernovae >= sum_galaxies and sum_supernovae >= sum_frbs:
        return 'supernovae'
    if sum_frbs >= sum_stars and sum_frbs >= sum_galaxies and sum_frbs >= sum_supernovae:
        return 'frbs'
# re-organise the layout of the functions and the given example data.
input = """
[
    {
        "type": "star",
        "name": "alpha-centaurus",
        "redshift": 0
    },
    {
        "type": "nebula",
        "name": "crab",
        "redshift": 0
    },
    {
        "type": "galaxy",
        "name": "sombrero",
        "redshift": 0
    }
]
"""
# don't use keywords as variable names ('input')
import json # used to parse a valid JSON string and convert it into a Python Dictionary.
print(aboundant(json.loads(input)))
# problem with this function: if two or more objects have the same count, the function will only return the first of these objects. Need to write a test.

def farthest(objects): # function that returns the object with the highest redshift.
    highest_redshift = None
    for o in objects:
        if highest_redshift is None or o["redshift"] < highest_redshift: # problem: this symbol should be ">", not "<".
            highest_redshift = o["redshift"]
    for o in objects:
        if o["redshift"] == highest_redshift:
            return o

print(farthest(json.loads(input)))
# as with the first function, this function will only return one result even if two or more objects have equally high redshifts.
# need to write a test.