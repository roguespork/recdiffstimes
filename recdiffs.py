import sys
import csv
import feedparser

def parse_podcast_rss(rss_url):
    feed = feedparser.parse(rss_url)

    with open('podcast_episodes.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Episode Number', 'Episode Name', 'Episode Length'])

        for i, entry in enumerate(feed.entries, start=1):
            episode_number = i
            episode_name = entry.title
            episode_length = entry.get("itunes_duration", "Unknown")

            writer.writerow([episode_number, episode_name, episode_length])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 recdiffs.py <rss_url>")
        sys.exit(1)
    
    rss_url = sys.argv[1]
    parse_podcast_rss(rss_url)