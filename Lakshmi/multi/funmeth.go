package multi

import (
	"fmt"
	"strings"
)

type student struct {
	name, school          string
	schoolid, marks, rank int16
}

func Dispp() {
	//creating map to count the repitive words in a string
	text := "Dont trouble the trouble, if you trouble the trouble, the trouble trouble you more trouble"
	words := strings.Fields(text)
	m := make(map[string]int)

	for _, i := range words {
		m[i]++

	}
	fmt.Println("Count of repititive words:-")
	for i, j := range m {
		fmt.Println(i, "-", j)
	}

	//giving pointers to function
	arr := [5]int{1, 2, 3, 4, 5}
	fmt.Println("before changing the array:", arr)
	multiarr(&arr)
	fmt.Println("ater changing the value of the array:")
	fmt.Println(arr)

	//method
	fmt.Println("using method to change the school name from svnbk to sbk school")
	s1 := student{name: "latha", school: "svbk", rank: 4, schoolid: 23455, marks: 566}
	s2 := student{name: "raju", school: "svbk", rank: 10, schoolid: 4555, marks: 526}
	s1.display()
	s2.display()
	fmt.Println(s1.name, s1.school, s1.schoolid, s1.rank)
	fmt.Println(s2.name, s2.school, s2.schoolid, s2.rank)

}

func (p *student) display() {
	p.school = "sbk school"

}
func multiarr(fun *[5]int) {
	(*fun)[2] = 5
	(*fun)[3] = 10
	(*fun)[4] = 15
}
