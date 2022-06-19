class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        '''
        No adjacent flowers
        
        1) traverse the flowerbed, if you reach 1 then skip the next bed and check if the next
        bed doesnt have any adjacent beds
        '''
        
        plant = 0
        
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                plant += 1
        else:
            for idx, bed in enumerate(flowerbed):
                if bed == 1:
                    idx += 1

                elif idx > 0 and idx < len(flowerbed) - 1:
                    if flowerbed[idx - 1] == 0 and flowerbed[idx + 1] == 0:
                        flowerbed[idx] = 1
                        plant += 1
                elif idx == 0:
                    if flowerbed[idx + 1] == 0:
                        flowerbed[idx] = 1
                        plant += 1
                elif idx == len(flowerbed) - 1 :
                    if flowerbed[idx - 1] == 0:
                        flowerbed[idx] = 1
                        plant += 1
        
        if plant >= n:
            return True
        
        return False
        