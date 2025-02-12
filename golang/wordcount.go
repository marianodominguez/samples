package main

import (
	"strings"
)

func WordCount(s string) map[string]int {

	mapcount := make(map[string]int)

	for _, word := range strings.Fields(s) {
		times, present := mapcount[word]
		if present {
			mapcount[word] = times + 1
		} else {
			mapcount[word] = 1
		}
	}

	return mapcount
}

func main() {
	wc.Test(WordCount)
}
