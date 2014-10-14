"""===========================================================================================
* Name : srm_400_GrabbingTaxi.py
* Author: taikido
* Description: TopCoder SRM 441: Div2 L1 (Simple Search, Iteration)
* Source: http://community.topcoder.com/stat?c=problem_statement&pm=8753
* Date: Wed.Dec.11.2013
*============================================================================================="""

class GrabbingTaxi:
    def minTime(self, tXs, tYs, gX, gY, walkTime, taxiTime):
        minT = 1000000000        
        for i in range(len(tXs)):            
            #walk to a taxi stand and then to drive in taxi to office
            totalTime = (abs(tXs[i]) * walkTime) + (abs(tYs[i]) * walkTime) + (abs(tXs[i] - gX) * taxiTime) + (abs(tYs[i] - gY) * taxiTime)
            if totalTime < minT:
                minT = totalTime
                
        
        #Time to just walk there
        totalTime = (abs(gX) * walkTime) + (abs(gY) * walkTime)
        if totalTime < minT:
                minT = totalTime
                
        return minT
    
if __name__ == "__main__":
    s  = GrabbingTaxi()
    
    print s.minTime((), (), 3, 3, 10, 2) #50
    print s.minTime((-2, -2), (0, -2), -4, -2, 15, 3) #42
    print s.minTime((3,), (0,), 5, 0, 10, 20) #50
    print s.minTime((34, -12, 1, 0, 21, -43, -98, 11, 86, -31), (11, 5, -68, 69, -78, -49, -36, -2, 1, 70), -97, -39, 47, 13) #2476
    print s.minTime((82, -60, 57, 98, 30, -67, 84, -42, -100, 62), (-7, 90, 53, -56, -15, -87, 22, -3, -61, -30), 21, 15, 53, 2) #1908



    
    