def generate_par(string):
    possible = set()
    for i in range(len(string)):
        possible.add( string[:i] + "()"+ string[i:] )
    possible.add(string+"()")
    return possible
  

def helper(n, s):
    if(n == 0): 
        return s
    else:
        frontier = set()
        for a in s:
            frontier = frontier.union( generate_par(a) )
            
        
        return helper(n-1, frontier)

    
def parentesis(n):
    return helper(n, set(["()"]))
    
def main():
    n = 5
    print( len(parentesis(n-1)) )


if __name__ == '__main__':
    main()