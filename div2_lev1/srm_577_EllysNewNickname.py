"""===========================================================================================
* Name : srm_577_EllysNewNickname.py
* Author: taikido
* Description: TopCoder SRM 577: Div2 L1 (Simulation, String Manipulation)
* Source: http://community.topcoder.com/stat?c=problem_statement&pm=12459
* Date: Tues.Dec.10.2013
*============================================================================================="""

class EllysNewNickname:
    
    def isVowel(self, letter):
        vowels = ('a', 'e', 'i', 'o', 'u', 'y')
        if letter in vowels:
            return True
        else:
            return False
        
    def getLength(self, nickname):
        c = nickname[0]
        count = 1
        
        for i in range(1, len(nickname)):
            if self.isVowel(nickname[i]) and self.isVowel(c):
                continue
            else:
                count += 1
                c = nickname[i]
                
        return count
    
    
if __name__ == "__main__":
    e = EllysNewNickname()    
    print e.getLength("esprit")
    