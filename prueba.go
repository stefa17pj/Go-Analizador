// Codigo de prueba
package main

import "fmt"

func main() {
	//mapa
	map_1 := map[string]int{
		"Dog":    90,
		"Cat":    91,
		"Cow":    92,
		"Bird":   93,
		"Rabbit": 94,
	}
	fmt.Println(map_1)
	// for
	suma := 0
	for i := 0; i < 10; i++ {
    		suma += i
	}
	// array
	colors := [4]string{"blue", "red", "pink", "yellow"} 
	fmt.Println(colors) 
	fmt.Println(len(colors))
	fmt.Println(cap(colors))
	// operaciones arimeticas
	var x int = 4 + 5  
	var x int = 8 - 5 
	var x int = 3 * 4 
	var x int = 10 / 5 
	var x int = 16 % 2
}