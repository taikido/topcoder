"""===========================================================================================
* Name : srm_284_TruckLoads.py
* Author: taikido
* Description: TopCoder SRM 284: Div2 L1 (Recursion, Simple Math)
* Source: http://community.topcoder.com/stat?c=problem_statement&pm=6011
* Date: Tues.Dec.10.2013
*============================================================================================="""

class Truckloads:
    truckCount = 0
    def numTrucks(self, numCrates, loadSize):
        self.helper(numCrates, loadSize)
        return self.truckCount
        
    def helper(self, numCrates, loadSize):
        if numCrates <= loadSize:
            self.truckCount += 1
        else:
            if ((numCrates % 2) != 0):
                self.helper(numCrates/2 + 1, loadSize)
                self.helper(numCrates/2, loadSize)
            else:
                self.helper(numCrates/2 , loadSize)
                self.helper(numCrates/2, loadSize)

            
            
if __name__ == "__main__":
    t = Truckloads()
    print t.numTrucks(15, 1)