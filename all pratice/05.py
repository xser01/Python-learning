class List:
    def remove_(self, integer_list, values_list):
        rezults = []                  
        values_set=set(values_list)     #we can use set rather than list
                                        #because set will be quicker than list in word'in or not in'
        for num in integer_list:        #in the for cycle,it can't use insert/remove/pop/del/clear
            if num not in values_set:
                rezults.append(num)
        return rezults