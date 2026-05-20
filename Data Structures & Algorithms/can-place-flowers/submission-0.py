class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)): 
         if i == 0:
          left = 0
         else:
          left = flowerbed[i-1]
 

         if i == len(flowerbed)-1:
          right = 0
         else:
            right = flowerbed[i+1]
        
         if left==0 and flowerbed[i] == 0 and right==0:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return n <=0