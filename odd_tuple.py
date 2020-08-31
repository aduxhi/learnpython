def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    nTup = ()
    index = 0
    while   index < len(aTup):
        nTup += (aTup[index],)
        index += 2
    return nTup

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))
