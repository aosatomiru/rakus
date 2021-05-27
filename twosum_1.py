def twoSum() :
    
    import re
    
    text = input()

    empty,num,tarege=re.split('nums = |, target = ',text)
    
    nums=eval(num)
    
    tareget=int(tarege)
    
    element = 0
    
    while element<= len(nums)-2:
        
        for i in (element+1,len(nums)-1):
            
            if nums[element]+nums[i]==tareget:
                
                print('[' + str(element) + ',' + str(i) + ']')
                
                break
            
            
            
            else:
                                
                pass
                
        element+=1
        
twoSum()