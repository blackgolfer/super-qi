class Cycle:
    '''
    Initialize the cycle. lst is a list of digits (elements of {0, ... n}, i.e. non negative integers) in the standard cycle notation.
    '''
    def __init__(self, lst):
        if(len(lst)>=2):
            self._last_element = lst[-1]                        #Last element in standard notation
            self._first_element = lst[0]                        #First element in standard notation

            # self._orbit maps elements that are not fixed under this cycles to its images
            # note, that self.self._last_element is mapped to self._first_element

            self._orbit = {lst[i]: lst[i+1] for i in range(0, len(lst)-1)}
            self._orbit[self._last_element] = self._first_element
            self._sequence = lst.copy();                        #This list represents the cycle in standard mathematical notation
        else:                           #In this case the cycle would be the identity. We don't want that
            raise Exception("Cannot initialize empty cycle")

    '''
    Returns the image of the element i
    If i is not contained in self._orbit, i is a fixed point
    '''
    def map(self, i):
        if not i in self._orbit:
            return i                #Fixed point
        return self._orbit[i]       #Else lookup


    '''
    We append the element i to the standard notation (i1 i2 ... in) -> (i1 i2 ... in i)
    '''
    def append(self, i):
        self._orbit[self._last_element] = i
        self._orbit[i] = self._first_element
        self._last_element = i
        self._sequence.append(i)

    '''
    Return the signum of this permutaiton
    '''
    def signum(self):
        if len(self._orbit)%2 == 0:
            return -1
        return 1
    
    def __str__(self):
        return "({})".format(" ".join([str(i) for i in self._sequence]))

    '''
    Returns true if the element i is a non-fixed point of this cycle (i.e. it is part of the orbit)
    '''
    def __contains__(self, i):
        return i in self._orbit




'''
Chech whether a given value table represents a permutation.
If value_table is a permutation s, we say s(i) := value_table[i]
Hence, value_table is a permutation if it contains every element from 0 to len(value_table)-1 exactly once
'''
def is_permutation(value_table):
    used_values = set()
    for i in value_table:
        if i<0 or i>=len(value_table) or i in used_values:
            return False
        used_values.add(i)

    return True


'''
Factor a permutation given by value_table (see for definition of associated permutaition above) into a set
of disjoint cycles.
'''
def factor_permutation(value_table):
    assert(is_permutation(value_table))
    used_values = set()
    cycles = []
    for (i, j) in enumerate(value_table):
        if i!=j and (not i in used_values):
            new_cycle = Cycle([i, j])
            used_values.add(i)
            used_values.add(j)
            k = j
            while not value_table[k] in new_cycle:
                new_cycle.append(value_table[k])
                used_values.add(value_table[k])
                k = value_table[k]
            cycles.append(new_cycle)

    return cycles


'''
Given a set of disjoint cycles (the list cycles), calculate where the element i is mapped by the product of all cycles.
Note, that the order in which the cycles are composed is irrelevant, since they are disjoint and thus commutate.
'''
def apply_cycles(cycles, i):
    j = i
    for cycle in cycles:
        j = cycle.map(j)

    return j

'''
Given a set of disjoint cycles (the list cylces), calculate the signum of the product of all cycles.
'''
def signum_cycles(cycles):
    s = 1
    for cycle in cycles:
        s*=cycle.signum()

    return s


'''
Use the formal definition of the signum to calculate it. THIS IS EXTREMELY INEFFICIENT!
'''
def signum_inefficient(permutation):
    assert(is_permutation(permutation))
    parities = 0
    for i in range(0, len(permutation)):
        for j in range(0, i):
            if permutation[i]<permutation[j]:
                parities += 1

    if parities%2 == 0:
        return 1

    return -1


'''
We do some testing here
'''
if __name__=="__main__":
    import random
    import time
    
    sigma = list(range(10000))
    random.shuffle(sigma)
    print("We will calculate the signum of a random permutation...")
    t1 = time.time()
    cycles = factor_permutation(sigma)
    s1 = signum_cycles(cycles)
    t2 = time.time()
    s2 = signum_inefficient(sigma)
    t3 = time.time()
    print("Time required using cycles: {0:.3f}s, Time required using naive method: {1:.3f}s".format(t2-t1, t3-t2))
    assert(s2 == s1)
    assert(sigma[3301] == apply_cycles(cycles, 3301))