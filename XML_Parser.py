import argparse
import json
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

def element_to_dictionary(elem):
    node = dict(elem.attrib)

    for child in elem:
        child_dictionary = element_to_dictionary(child)
        tag = child.tag

        if tag in node:
            if not isinstance(node[tag], list):
                node[tag] = [node[tag]]
            node[tag].append(child_dictionary)
        else:
            node[tag] = child_dictionary

    text = (elem.text or "").strip()

    if text:
        node["text"] = text

    return node

def parse_xml_file(path: Path) -> dict:
    xml_bytes = path.read_bytes()
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError as e:
        raise SystemExit(f"XML parse error in {path}: {e}") from e
    
    return {root.tag: element_to_dictionary(root)}

def main():
    parser = argparse.ArgumentParser(description="Parse an XML file into a nested dictionary (attributes + elements).")
    parser.add_argument("xml_path", metavar="XML_PATH", type=Path, help="Path to XML file.")
    parser.add_argument("-o", "--out", metavar="OUTPUT_FILE", type=Path, default=None, help="Optional path to write JSON output.")
    args = parser.parse_args()

    if not args.xml_path.exists():
        raise SystemExit(f"File not found: {args.xml_path}")
    
    result = parse_xml_file(args.xml_path)

    if args.out:
        args.out.write_text(json.dumps(result, indent=2), encoding="utf-8")
        print(f"Wrote JSON to: {args.out}")
    else:
        json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
        print()

        
if __name__ == "__main__":
    main()