#!/bin/bash

for j in $(seq -f %03.0f 9 25); do
	echo ${j}
	python sky_eclp_planets.py planets_${j} ${j}
done

convert -delay 20 -loop 0 planets*.png planets.gif
