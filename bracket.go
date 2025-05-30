package main
import "fmt"

/*
	n! = n * n-1 * n-2 * n-3 * n-(n-1)
	2n!/(n! (n+1)!)
	Catlalin numbers are lowkey strange, its based on the Math dielma of solving the max no of valid arrangements of parentheses, but this can also found in binary tress

	Cn+1 = n SIGMA k=0 Ck * Cn-k
*/

func recurse(n int) int{
	if n == 0 {
		// fmt.Println("base case reached ->")
		return 1
	}
	
	nth_sum := 0
	for i := 0; i < n; i++ {
		nth_sum += recurse(i) * recurse(n-1 - i)
		fmt.Printf("left side-> %d\n right side-> %d\n", i, n-i-1)
		// fmt.Println(nth_sum)
	}

	return nth_sum
}

func main() {
	total := recurse(4)
	fmt.Println("total nth_sum below")
	fmt.Println(total)
}
