import xml.etree.ElementTree as ET
import json

xml_file = "/workspaces/datataggging2/Regulations/CUI/CUI-32-2002.xml"
output_json = "/workspaces/datataggging2/Regulations/CUI/CUI-32-2002_acronyms.json"

tree = ET.parse(xml_file)
root = tree.getroot()

# Find the Appendix section
acronyms = {}
for fp in root.findall(".//FP-1"):
    text = fp.text.strip()
    if "—" in text:
        acronym, definition = text.split("—", 1)
        acronyms[acronym.strip()] = definition.strip()

with open(output_json, "w") as f:
    json.dump(acronyms, f, indent=2)

print(f"Extracted {len(acronyms)} acronyms to {output_json}")