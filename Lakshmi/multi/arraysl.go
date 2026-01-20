package multi

import (
	"fmt"
)

type address struct {
	name, Housenum, streetname, city, state string
	pincode, phonenum                       int64
}

func Disp(){
	var ar [3]string
	ar[0] = "HeyBeautiful"
	fmt.Println(ar, "\n")
	a := address{name: "prateek goud", streetname: "gandhi chowk", Housenum: "5-66",
		city: "Mumbai", state: "Maharastra", pincode: 48759779, phonenum: 9823883446}
	fmt.Println("Address")
	fmt.Println("Name:"+a.name, "\n", "Housenumber:"+a.Housenum, "\n", "StreetName:"+a.streetname, "\n", "City:"+a.city, "\n", "State:"+a.state, "\n", "Pincode:", a.pincode, "\n", "Phone:", a.phonenum)

	b := [8]int{4, 5, 6, 8, 9, 10, 58, 88}
	sumev, sumodd := 0, 0

	for i := range 8 {
		if i%2 == 0 {
			sumev += b[i]
		} else {
			sumodd += b[i]
		}
	}
	fmt.Println("sumeve: ", sumev)
	fmt.Println("sumodd: ", sumodd)

	s := []int{1, 4, 5}
	fmt.Println(len(s), cap(s))
	s = append(s, 8)
	fmt.Println(s)
	fmt.Println(len(s), cap(s))
	l := make([]int, 5, 6)
	l[0] = 2
	l[1] = 3
	l = append(l, 5, 4, 3)
	fmt.Println(l)
	slice := l[2:7]
	fmt.Println(slice)

}
