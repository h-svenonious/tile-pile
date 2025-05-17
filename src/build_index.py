'''
Index generator
'''
import sys

INDEX = """<!DOCTYPE html>
<html>
<head>
<title>h svenonious</title>
<style>
    body {{
        font-family: courier;
        color: Black;
    }}
    a {{
        font-family: courier;
        color: Black;
    }}
    a:hover {{
        color: White;
        background: GRAY;
    }}
    t {{
        font-family: courier;
        color: Black;
    }}
    t:hover {{
        color: White;
        background: GRAY;
    }}
</style>
</head>
<body>
  {}
</body>
</html>
"""

BODY = """
..........................
..........................
..........................
..........................
........ TILES ...........
.......... PILE ..........
........... TRAIL ........
..........................
..........................
..........................
..........................
"""

class Link:
    def __init__(self, name, target):
        self.name = name
        self.link = "<a href='{}'>{}</a>".format(target, name)
    def replace(self, text, placeholder):
        assert(len(placeholder) == len(self.name))
        return text.replace(placeholder, self.link)

def modify_name(name):
    new_name = ""
    for c in name:
        new_name += "<t>" + c + "</t>"
    return new_name

if __name__ == '__main__':
    web_dir = sys.argv[1]

    BODY = BODY.replace("\n", "", 1)
    BODY = BODY.replace("\n", "<br>")
    BODY = BODY.replace(".", "<t>.</t>")
    BODY = BODY.replace("-", "<t>-</t>")
    BODY = BODY.replace(" ", "<t>&nbsp</t>")
    #print(BODY)

    BODY = BODY.replace("TILES", modify_name("tiles"))

    # create links
    pile = Link("pile", "tile-pile/index.html")
    trail = Link("trail", "tile-trail/index.html")
    BODY = pile.replace(BODY, "PILE")
    BODY = trail.replace(BODY, "TRAIL")

    # change color
    INDEX = INDEX.replace("GRAY", "#EEEEEE")

    with open(web_dir + '/index.html', 'w') as _f:
        _f.write(INDEX.format(BODY))
