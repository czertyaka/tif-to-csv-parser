.DEFAULT_GOAL=example
.PHONY: example clean

example:
	./tif-to-csv-parser.py example.tif 1201

clean:
	@rm -f *.csv rsmpld*