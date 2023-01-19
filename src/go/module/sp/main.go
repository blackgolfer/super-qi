package main

import (
	"fmt"

	"super-qi/sp/signal"
	"super-qi/sp/utils"
)

func main() {
	fmt.Println("Hello, Modules!")

	// utils.LineSpace
	fmt.Printf("---------------------\n")
	fmt.Printf("   utils.LineSpace   \n")
	fmt.Printf("---------------------\n")
	t := utils.LineSpace(-1, 1, 4)
	for i, j := range t {
		fmt.Printf("t[%d]=%f\n", i, j)
	}
	// signal.Interval
	fmt.Printf("--------------------\n")
	fmt.Printf("   signa.Interval   \n")
	fmt.Printf("--------------------\n")
	data := make([]float64, 0)
	i := signal.NewInterval(data, -4, 4)
	for j := -4; j <= 4; j++ {
		fmt.Printf("i[%d]=%f\n", j, i.At(j))
	}
}
