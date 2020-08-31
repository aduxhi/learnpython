s1 = 'abcd' 
s2 = 'efghi'

def helpLaceStrings(s1, s2, out):
	if s1 == '':
	    print (out + s2)
	    return 1
	if s2 == '':			
	    return 2		
	else:
            helpLaceStrings(s1[1:], s2[1:], out+s1[0]+s2[0])

x = helpLaceStrings(s1, s2, '')

print (x)
