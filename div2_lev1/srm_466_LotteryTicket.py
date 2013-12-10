"""===========================================================================================
* Name : srm_466_LotteryTicket.py
* Author: taikido
* Description: TopCoder SRM 466: Div2 L1 (Brute Force, Recursion)
* Source: http://community.topcoder.com/stat?c=problem_statement&pm=10860&rd=14150
* Date: Tues.Dec.10.2013
*============================================================================================="""

class LotteryTicket:
    
    def sub(self, so_far, rest, subsets):
        if (len(rest) == 0):
            subsets.append(so_far)
        else:
            self.sub(so_far + (rest[0],), rest[1:], subsets)
            self.sub(so_far, rest[1:], subsets)
        
    def buy(self, price, b1, b2, b3, b4):        
        subsets = []
        so_far = ()
        rest = (b1, b2, b3, b4)
        self.sub(so_far, rest, subsets)
        
        for i in range(len(subsets)):
            if sum(subsets[i]) == price:
                return "POSSIBLE"
            
        return "IMPOSSIBLE"
    
    
def main():    
    #Test Case 1
    l = LotteryTicket()
    price = 10
    b1, b2, b3, b4 = 1, 5, 10, 50    
    print l.buy (price, b1, b2, b3, b4)

main()