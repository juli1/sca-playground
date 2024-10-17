package main

import (
	"fmt"
	"github.com/osrg/gobgp/v3/pkg/packet/bgp"
)

func main() {
	fmt.Println("Hello, World!")
	b, err := bgp.ValidateUpdateMsg(nil, nil, true, false)
	
}
