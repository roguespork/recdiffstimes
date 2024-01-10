import json

def parse_transcriptions(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    parsed_transcriptions = []
    if 'transcriptions' in data and isinstance(data['transcriptions'], list):
        for item in data['transcriptions']:
            parsed_item = {
                'start': item.get('start', 'Unknown'),
                'end': item.get('end', 'Unknown'),
                'text': item.get('text', '')
            }
            parsed_transcriptions.append(parsed_item)

    return parsed_transcriptions

def write_json_to_file(data, output_file_path):
    with open(output_file_path, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    import sys

    if len(sys.argv) < 3:
        print("Usage: python script.py <input_file_path> <output_file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    parsed_data = parse_transcriptions(input_file_path)
    write_json_to_file(parsed_data, output_file_path)
    print(f"Parsed data has been saved to {output_file_path}")

if __name__ == "__main__":
    main()
