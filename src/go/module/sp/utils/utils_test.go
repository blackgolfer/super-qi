package utils

import "testing"

func TestLineSpace(t *testing.T) {
	n := 9
	tt := LineSpace(-1, 1, n)
	zero := n / 2
	if tt[int(zero)] != 0.0 {
		t.Fatalf("odd num failed: (%d,%f)", zero, tt[zero])
	}
	n = 10
	zero = n / 2
	tt = LineSpace(-1, 1, n)
	if tt[zero] <= 0.0 {
		t.Fatalf("even num failed (%d,%f)", zero, tt[zero])
	}
}
