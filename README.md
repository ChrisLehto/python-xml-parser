# Python XML Parser

A simple Python CLI tool for parsing XML files into nested dictionaries and JSON.  
Handles attributes, repeated elements, and text content gracefully.

## Features
- Converts XML into a nested Python dictionary
- Preserves attributes and text content
- Groups repeated tags into lists
- CLI supports printing to console or writing to JSON file

## Usage Examples
# Print parsed XML to console
python XML_Parser.py sample.xml

# Write parsed output to a JSON file
python XML_Parser.py sample.xml -o parsed.json
