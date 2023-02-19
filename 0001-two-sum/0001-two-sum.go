func twoSum(nums []int, target int) []int {
    hash := map[int]int{}
    
    for i, val := range nums {
        num := target-val
        
        if x, in := hash[num]; in {
            return []int{x, i}
        } else {
            hash[val] = i
        }
    }
    
    return []int{}
}