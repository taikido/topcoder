"""===========================================================================================
* Name : srm_230_SortEstimate.py
* Author: taikido
* Description: TopCoder SRM 230: Div2 L2 or Div1 L1 (Math, Search)
* Source: http://community.topcoder.com/stat?c=problem_statement&pm=3561&rd=6519
* Date: Fri.Jan.10.2014
*============================================================================================="""

from math import log

class SortEstimate:    
    def p(self, x, target):
        return True if x >= target else False
    
    def howMany(self, c, time):
        #search for n
        low = c
        high = time
        max_steps = 100
        steps = 0
        
        while steps < max_steps:
        
            #n = (low + high)/2.0
            n = low + (high-low)/2.0
            x = c * (log(n, 2) ) * n  #x = c * (log(n+ 0.0001, 2) ) * n
            
            #print "[{0}]: n: {1}, x: {2}, low: {3}, high: {4}".format(steps, n, x, low, high)
            
            if self.p(x, time):
                high = n
            else:
                low = n
                
            steps += 1
            
        return low
                

    
def run_trivial_test_cases():
    #print log(4, 2) * 4
    #1*4*lg(4) = 4*2 = 8
    s = SortEstimate()
    
    #Test Case 0
    print s.howMany(1, 8)
    
    #Test Case 1
    print s.howMany(2, 16)
    
    #Test Case 2
    print s.howMany(37, 12392342) #23104.999312341137
    '''
    Returns: 23104.999312341137
    We can almost sort 23105 integers, but not quite.
    '''
    
    #Test Case 3
    print s.howMany(1, 2000000000) #Returns: 7.637495090348122E7    
        
if __name__ == "__main__":
    run_trivial_test_cases()


            
def test():
    #Problems
    #Case 1: low = high
    #Case 2: low > high
    '''
    System tests Failed on: (Need to Fix)
    Test Case 40: {1, 1}     Expected: 1.5596104694623691 Received: 1.0
    Test Case 42: {100, 1}   Expected: 1.0069076686081029 Received: 100
    '''
    s = SortEstimate()
    print s.howMany(37, 12392342) #23104.999312341137
    
    print "log(4,2): ", log(1+0.01,2)
    print "\n\n"
#     s = SortEstimate()
#     print s.howMany(1, 1)
#      
#     c = 1
#     n = 1.5596104694623691 #1.5596104694623691
#     time_val = c * log(n, 2) * n
#     print  time_val
    
    #Assumption: n is between c(lower) and t (upper)
#     
#     c = 100
#     n = 1.0069076686081029
#     print c * log(n, 2) * n
#     
#     print s.howMany(1, 100)    

