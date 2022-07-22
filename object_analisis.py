import json # used to parse a valid JSON string and convert it into a Python Dictionary.

def get_most_common_object(objects):
    '''
    Function that counts each type of object and returns the most common object(s).
    '''
    abundant_dict = {'star':0,
                     'galaxy':0,
                     'supernovae':0,
                     'frb':0}

    for obj in objects: # one for loop instead of 4, to incerase performance
        if obj['type'] in list(abundant_dict.keys()):
            abundant_dict[obj['type']] += 1
        else: 
            print(f"Object {obj} has unknown type {obj['type']}")
    
    max_value = max(abundant_dict.values())
    most_common_objects = [key for key, value in abundant_dict.items() if value == max_value] # list comprehension is faster than for loops
    return most_common_objects


def farthest(objects): # function that returns the object with the highest redshift.
    highest_redshift = None
    for o in objects:
        if highest_redshift is None or o["redshift"] < highest_redshift: # problem: this symbol should be ">", not "<".
            highest_redshift = o["redshift"]
    for o in objects:
        if o["redshift"] == highest_redshift:
            return o


# Execute the following code only if the file was run directly, and not imported.
if __name__ == '__main__':
    
    # don't use keywords as variable names ('input')
    data = """
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
        
    print(get_most_common_object(json.loads(data)),'\n') # function optimised
    
    print(farthest(json.loads(data)))
    # as with the first function, this function will only return one result even if two or more objects have equally high redshifts.
    # need to write a test.
