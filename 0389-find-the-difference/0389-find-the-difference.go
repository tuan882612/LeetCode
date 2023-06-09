func findTheDifference(s string, t string) byte {
    var count int
    
    for _, val := range s + t {
        count ^= int(val)
    }
    
    return byte(count)
}