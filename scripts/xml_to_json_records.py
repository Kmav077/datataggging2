import xml.etree.ElementTree as ET
import json

xml_file = "/workspaces/datataggging2/Regulations/National-controls/Regulations/National Controls/security-controls-2001.xml"
output_json = "/workspaces/datataggging2/Regulations/National-controls/Regulations/National Controls/security-controls-2001.json"

def elem_to_dict(elem):
    d = {}
    # Add attributes if present
    if elem.attrib:
        d.update({f"@{k}": v for k, v in elem.attrib.items()})
    # Add children
    children = list(elem)
    if children:
        child_dict = {}
        for child in children:
            child_result = elem_to_dict(child)
            if child.tag not in child_dict:
                child_dict[child.tag] = []
            child_dict[child.tag].append(child_result)
        for k, v in child_dict.items():
            # If only one child, don't use a list
            if len(v) == 1:
                d[k] = v[0]
            else:
                d[k] = v
    # Add text if present
    text = (elem.text or '').strip()
    if text:
        d["#text"] = text
    return d

tree = ET.parse(xml_file)
root = tree.getroot()
data = {root.tag: elem_to_dict(root)}

with open(output_json, "w") as f:
    json.dump(data, f, indent=2)

print(f"Full XML converted to {output_json}")