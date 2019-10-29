"""Baekjoon Online Judge No.2448

11th Printing Stars, in Python

INPUT: N, N=3*2**k, k<=10
ex input: 24

OUTPUT: Return N line of star prints
ex output: 
                       *                        
                      * *                       
                     *****                      
                    *     *                     
                   * *   * *                    
                  ***** *****                   
                 *           *                  
                * *         * *                 
               *****       *****                
              *     *     *     *               
             * *   * *   * *   * *              
            ***** ***** ***** *****             
           *                       *            
          * *                     * *           
         *****                   *****          
        *     *                 *     *         
       * *   * *               * *   * *        
      ***** *****             ***** *****       
     *           *           *           *      
    * *         * *         * *         * *     
   *****       *****       *****       *****    
  *     *     *     *     *     *     *     *   
 * *   * *   * *   * *   * *   * *   * *   * *  
***** ***** ***** ***** ***** ***** ***** *****
"""


def print_stars(n):
	"""Print stars"""

	arr = ['  *  ', ' * * ', '*****']
	k = 0

	while 3*(2**k) <= n:
		if k > 0:
			bottom = []
			upper = []

			for i in range(len(arr)):
				bottom.append(arr[i]+' '+arr[i])
			for j in range(len(arr)):
				upper.append(3*(2**(k-1))*' '+ arr[j]+3*(2**(k-1))*' ')
			arr = upper + bottom
		k += 1
	return arr


# If runs:
if __name__ == "__main__":
	n = int(input())
	arr = print_stars(n)

	for line in arr:
		print(line)





