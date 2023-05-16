import "strconv"

func isPalindrome(x int) bool {
    text := strconv.Itoa(x)
    l := len(text)
    
    for i, j := 0, l - 1; i < j; i, j = i + 1, j - 1 {
        if text[i] != text[j] {
            return false
        }
    }
    return true
}