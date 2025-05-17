function drop_tiles(op) {
    var svgns = "http://www.w3.org/2000/svg";
    let canvas_width = window.innerWidth * 0.99;
    let canvas_height = window.innerHeight * 0.99;
    let box_max = Math.max(canvas_width, canvas_height) / 10;
    let box_var = box_max * 0.8;
    let border = box_max;
    let color = 'Black';
    var tiles = document.getElementById('tiles');
    tiles.setAttribute('width', canvas_width);
    tiles.setAttribute('height', canvas_height);

    function drop_tile(x, y) {
      var tile = document.createElementNS(svgns,'rect');
      var w = box_max + Math.random() * 2 * box_var - box_var;
      var h = box_max + Math.random() * 2 * box_var - box_var;
      tile.setAttribute('width', w);
      tile.setAttribute('height', h);
      tile.setAttribute('x', x - w / 2);
      tile.setAttribute('y', y - h / 2);
      tile.setAttribute('fill', color);
      tile.setAttribute('opacity', Math.random() * op);
      document.getElementById('tiles').appendChild(tile );
    }

    let counter = 0;

    document.onmousemove = function(event) {
      if (counter++ < 4) {
        return;
      }
      counter = 0;

      drop_tile(event.clientX, event.clientY);
    }
}
