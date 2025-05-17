index_web_dir = ./h-svenonious.github.io
tile_pile_web_dir = ./h-svenonious.github.io/tile-pile/
tile_trail_web_dir = ./h-svenonious.github.io/tile-trail

all: clean pile trail index

index:
	python3 src/build_index.py $(index_web_dir)

pile:
	mkdir -p $(tile_pile_web_dir)
	cp src/throw_tiles.js $(tile_pile_web_dir)
	python3 src/build_tile_pile.py $(tile_pile_web_dir)

trail:
	mkdir -p $(tile_trail_web_dir)
	cp src/trail.html $(tile_trail_web_dir)/index.html
	cp src/drop_tiles.js $(tile_trail_web_dir)/drop_tiles.js

clean:
	rm -f $(tile_pile_web_dir)/*
	rm -f $(tile_trail_web_dir)/*
