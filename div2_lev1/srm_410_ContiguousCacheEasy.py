"""===========================================================================================
* Name : srm_410_ContiguousCacheEasy.py
* Author: taikido
* Description: TopCoder SRM 410: Div2 L1 (Brute Force, Simulation)
* Source: http://community.topcoder.com/stat?c=problem_statement&pm=9729
* Date: Mon.Oct.13.2014
*============================================================================================="""

class ContiguousCacheEasy:
    def bytesRead(self, n, k, addresses):
        bytes_read = 0
        range_start = 0
        range_end = k-1
        for byte in addresses:
            if byte > range_end:
                bytes_read += (byte - range_end) if ((byte - range_end) < k) else k
                range_end = byte
                range_start = range_end - k + 1
            elif byte < range_start:
                bytes_read += (range_start - byte) if ((range_start - byte) < k) else k
                range_start = byte
                range_end = range_start + k - 1
        return bytes_read
    
    
if __name__ == "__main__":    
    # Test Case 1
    n = 100
    k = 5
    addresses = (6, 0, 3, 20, 22, 16)
    
    problem = ContiguousCacheEasy()
    print problem.bytesRead(n, k, addresses)