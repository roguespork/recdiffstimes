import sys
import csv
import feedparser

def parse_duration(duration_str):
    """Convert iTunes duration string to seconds."""
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


def parse_podcast_rss(csv_file_name, rss_url):
    feed = feedparser.parse(rss_url)

    with open(csv_file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Episode Number', 'Episode Name', 'Episode Runtime', 'Episode Length'])

        for i, entry in enumerate(feed.entries, start=1):
            episode_number = i
            episode_name = entry.title
            episode_length_str = entry.get("itunes_duration", "0")
            episode_length_sec = parse_duration(episode_length_str)

            writer.writerow([episode_number, episode_name, episode_length_str, episode_length_sec])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 recdiffs.py <rss_url>")
        sys.exit(1)
    
    csv_file_name = sys.argv[1]
    rss_url = sys.argv[2]
    parse_podcast_rss(csv_file_name, rss_url)