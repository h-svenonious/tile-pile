function throw_tiles(N, op) {
    let canvas_width = window.innerWidth * 0.95;
    let canvas_height = window.innerHeight * 0.95;
    let box_max = Math.max(canvas_width, canvas_height) / 10;
    let box_var = box_max * 0.999;
    let border = box_max;
    let color = 'Black';
    var tiles = document.getElementById('tiles');
    tiles.setAttribute('width', canvas_width);
    tiles.setAttribute('height', canvas_height);

    function throw_tile(delay_ms, n) {
        var svgns = "http://www.w3.org/2000/svg";
        var tile = document.createElementNS(svgns,'rect');
        var w = box_max + Math.random() * 2 * box_var - box_var;
        var h = box_max + Math.random() * 2 * box_var - box_var;
        tile.setAttribute('width', w);
        tile.setAttribute('height', h);
        tile.setAttribute('x',Math.random() * (canvas_width - w - 2 * border) +  border);
        tile.setAttribute('y',Math.random() * (canvas_height - h - 2 * border) +  border);
        tile.setAttribute('fill', color);
        tile.setAttribute('opacity', Math.random() * op);
        document.getElementById('tiles').appendChild(tile );

        if (n > 0) {
            if (delay_ms == 0) {
                throw_tile(delay_ms, n - 1);
            } else {
                setTimeout(throw_tile, delay_ms, delay_ms, n - 1);
            }
        }
    }

    throw_tile(Math.floor(5000 / N), N);
}
