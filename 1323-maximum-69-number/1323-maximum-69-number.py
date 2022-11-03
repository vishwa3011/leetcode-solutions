class Solution:
    def maximum69Number (self, num: int) -> int:
        
        if num == 6 or num == 9:
            return 9
        
        numbers_formed = []
        num_list = [int(x) for x in str(num)]
        nine = 9
        six = 6
        for i in range(len(num_list)):
            num_copy = num_list.copy()
            if num_copy[i] == 6:
                num_copy[i], nine = nine, num_copy[i]
            elif num_copy[i] == 9:
                num_copy[i], six = six, num_copy[i]
            
            numbers_formed.append(int(''.join(map(str, num_copy))))
        
        
        print(numbers_formed)
        return max(numbers_formed)

            