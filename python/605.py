class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total = n
        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0:
                    if i+1 >= len(flowerbed):
                        flowerbed[i] = 1
                        total -= 1
                    elif flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        total -= 1
            elif i == len(flowerbed)-1:
                if flowerbed[i] == 0:
                    if i-1 < 0:
                        flowerbed[i] = 1
                        total -= 1
                    elif flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        total -= 1
            else:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    total -= 1
        return total <= 0
