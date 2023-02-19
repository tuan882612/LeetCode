func twoSum(nums []int, target int) []int {
    hash := make(map[int]int)
    
    for i, val := range nums {
        num := target-val
        
        if x, found := hash[num]; found {
            return []int{x, i}
        } else {
            hash[val] = i
        }
    }
    
    return []int{}
}