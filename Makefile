web_dir = ./h-svenonious.github.io/tile-pile/

all: clean
	mkdir -p $(web_dir)
	cp src/throw_tiles.js $(web_dir)
	python src/build.py $(web_dir)

clean:
	rm -f $(web_dir)/*
