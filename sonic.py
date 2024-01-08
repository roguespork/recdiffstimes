import csv
import feedparser
import sys
import json

# Function takes in the string of iTunes_duration and parses it out to read as seconds.

def parse_duration(duration_str):
    parts = duration_str.split(':')
    parts = [int(part) for part in parts]

    if len(parts) == 3:  # HH:MM:SS format
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    elif len(parts) == 2:  # MM:SS format
        return parts[0] * 60 + parts[1]
    elif len(parts) == 1:  # seconds
        return parts[0]
    else:
        return 0  # Default to 0 if format is unknown

def parse_podcast_rss(rss_url, csv_file_name, json_file_name):
    # Parse the RSS feed
    print('Running the parser...')
    feed = feedparser.parse(rss_url)

    # List to store episode data. Note: this is primarily used for the JSON file; it can be removed if that is no longer required.
    episodes = []

    # Create a CSV file with the specified name
    with open(csv_file_name, 'w', newline='', encoding='utf-8') as csvfile:
        print('Writing to CSV...')
        writer = csv.writer(csvfile)
        writer.writerow(['Episode Number', 'Episode Name', 'Episode Length (Seconds)'])

        # Iterate over each entry (episode) in the feed
        for i, entry in enumerate(feed.entries, start=1):
            episode_number = i
            episode_name = entry.title
            episode_length_str = entry.get("itunes_duration", "0")
            episode_length_sec = parse_duration(episode_length_str)

            # Write episode details to the CSV
            writer.writerow([episode_number, episode_name, episode_length_sec])

            # Add episode data to the list
            episodes.append({
                'Episode Number': episode_number,
                'Episode Name': episode_name,
                'Episode Length (Seconds)': episode_length_sec
            })

    # Write data to a JSON file
    with open(json_file_name, 'w', encoding='utf-8') as jsonfile:
        print('Writing to JSON...')
        json.dump(episodes, jsonfile, indent=4)

    print('Success!')

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python script_name.py <rss_url> <csv_file_name> <json_file_name>")
        sys.exit(1)

    rss_url = sys.argv[1]
    csv_file_name = sys.argv[2]
    json_file_name = sys.argv[3]
    parse_podcast_rss(rss_url, csv_file_name, json_file_name)
