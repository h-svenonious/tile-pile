'''
Tiles generator
'''

TILES_FILE_TEMPLATE = """<!DOCTYPE html>
<html>
<body>
    <svg id='tiles'></svg>
    <script src='throw_tiles.js'>
    </script>
    <script>
        throw_tiles({}, {});
    </script>
</body>
</html>
"""

INDEX_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
<title>tiles</title>
</head>
<body>
{}
</body>
</html>
"""

INDEX_LINKS_TEMPLATE = """
    <div style="position:absolute;left:{}px;top:{}px;">
        <iframe src="{}" height="100" width="100" style="border:none"></iframe>
        <a href="{}" style="position:absolute; top:0; left:0; display:inline-block; width:100px; height:100px; z-index:5;"></a>
    </div>
"""


# create pairs (N, op)
links = ""
for xx, nn in enumerate(range(10, 400, 80)):
    for yy, op in enumerate(range(1, 10, 2)):
        #print(f'({nn}, {op / 10})', end='')
        filename = f'tiles_{nn}_{op}.html'
        with open('web/' + filename, 'w') as _f:
            _f.write(TILES_FILE_TEMPLATE.format(nn, op / 10))
        links += INDEX_LINKS_TEMPLATE.format(xx * 100 + 10, yy * 100 + 10, filename, filename)

with open('web/index.html', 'w') as _f:
    _f.write(INDEX_TEMPLATE.format(links))
