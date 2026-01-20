package main

import (
	"fmt"
	"lakshmi/multi"
	"math/rand/v2"
	"time"
)

func main() {
	var a int = 4
	var s string = "goog"

	var f float32 = 4.44
	var arr [4]int
	fmt.Println("values of a ,s ,f are ", a, ",", s, ",", f)
	fmt.Println(" 5 Multiples of 4 is equal to", multi.Mul(5, 4))

	//..............................for.........................//
	for i := 0; i < a; i++ {
		arr[i] = i
	}
	fmt.Println(arr)

	//..............................if..................//
	if a%2 == 0 {
		fmt.Println("a is even number")
	} else {
		fmt.Println("a is oddd number")
	}

	//...........................switch case....................//
	fmt.Println("Rainbow Colors")
	u := "v"
	switch u {
	case "v":
		fmt.Println("Violet")
		fallthrough
	case "i":
		fmt.Println("Indigo")
		fallthrough
	case "b":
		fmt.Println("Blue")
		fallthrough
	case "g":
		fmt.Println("Green")
		fallthrough
	case "o":
		fmt.Println("Orange")
		fallthrough
	default:
		fmt.Println("Red")
	}

	//.......................defer..................................................//
	for i := 5; i > 0; i-- {
		defer fmt.Println(i)
	}

	//......................pointers..............................................//
	q := 10
	p := &s
	h := *p
	fmt.Println(q, p, h)

	multi.Disp()

	multi.Dispp()
	multi.Factorial()
	multi.Wordcount()
	multi.Fibonocci()
	multi.Palindrome()

	//..........go routines
	go multi.Gethindi("नमस्ते (Namaste)")
	go multi.Getspanish("Hola")
	go multi.Gettelugu("హలో (Halo)")
	go multi.Gettamil("வணக்கம் (Vanakkam)")

	time.Sleep(3 * time.Second)

	ch := make(chan int)
	go Egg(ch)

	for i := range 10 {
		if i != 9 {
			ch <- rand.IntN(1000)
		} else {
			break
		}
	}

}
func Egg(ch1 chan int) {
	for i := range ch1 {
		fmt.Println(i)
	}
}
