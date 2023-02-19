func twoSum(nums []int, target int) []int {
    hash := map[int]int{}
    
    for i, val := range nums {
        num := target-val
        
        if _, found := hash[num]; found {
            return []int{hash[num], i}
        } else {
            hash[val] = i
        }
    }
    
    return []int{}
}