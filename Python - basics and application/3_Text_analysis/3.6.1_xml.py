from xml.etree import ElementTree as et
from xml.etree.ElementTree import Element

in_xml = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'
colors = {"red": 0, "green": 0, "blue": 0 }

root = et.fromstring(in_xml)

def get_children(elem: Element, lvl: int):
    colors[elem.attrib.get("color")] += lvl
    for el in elem:
        get_children(el, lvl + 1)
    return colors

res = get_children(root, 1)
print(*res.values())
