package signal

type Interval struct {
	final int
	least int
	data  []float64
}

func (i *Interval) At(n int) float64 {
	o := -i.least
	return i.data[o+n]
}

func NewInterval(data []float64, least int, final int) *Interval {
	if err := least > 0; err == true {
		panic(err)
	}
	n := 1 + final - least
	if n > 0 {
		i := make([]float64, n)
		o := -least
		if n <= len(data) {
			for k := least; k <= final; k++ {
				i[o+k] = data[o+k]
			}
		}
		return &Interval{final, least, i}
	} else {
		return nil
	}
}
