"""===========================================================================================
* Name : srm_488_TheBoredomDivTwo.py
* Author: taikido
* Description: TopCoder SRM 488: Div2 L1 (Advanced Math, Encryption/Compression)
* Source: http://community.topcoder.com/stat?c=problem_statement&pm=11194
* Date: Tues.Dec.10.2013
*============================================================================================="""



class TheBoredomDivTwo:
    def find(self, n, m, j, b):
        friends = [0]* (n+m)
        
        for i in range(n):
            friends[i] = 1
        
        friends[j-1] = 1
        friends[b-1] = 1
        
        #print "Friends: ", friends
        return friends.count(1)
    
    
    
if __name__ == "__main__":
    s = TheBoredomDivTwo()
    
    n, m, j, b = 1, 1, 1, 2
    n, m, j, b = 2, 1, 1, 2
    n, m, j, b = 1, 2, 3, 2
    n, m, j, b = 4, 7, 7, 4
    print s.find(n,m,j,b)
    

    
    
