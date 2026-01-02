class Solution:
    def bestClosingTime(self, customers: str) -> int:
        min_penalty = 10**7
        index = None
        
        Y_count = customers.count("Y")
        N_count = 0
        for i in range(len(customers)):
            penalty = Y_count + N_count 
            
            if penalty < min_penalty:
                min_penalty = penalty
                index = i
            
            if customers[i] == "N":
                N_count +=1
            else:
                Y_count -=1

        penalty = Y_count + N_count 
        
        if penalty < min_penalty:
            min_penalty = penalty
            index = i + 1

        return index