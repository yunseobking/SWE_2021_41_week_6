# initial version
def twoSum(nums: list[int], target: int) -> list[int]:
    
    a=0
    b=1
    while a != len(nums)-1 :
        b=a+1
        while b != len(nums):
            if nums[a] + nums[b] == target :
                return [a,b]
            b+=1
        a+=1