package utils

func LineSpace(a, b float64, n int) []float64 {
	err := n <= 1
	if err {
		panic(err)
	}
	dt := (b - a) / float64(n-1)
	t := make([]float64, n)
	t[0] = a
	for i := 1; i < n; i++ {
		t[i] = t[i-1] + dt
	}
	return t
}
