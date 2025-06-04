from collections import Counter
import re

def parse_log_line(line):
    # Apache common log format pattern
    pattern = r'(?P<ip>\S+) \S+ \S+ \[(?P<date>.*?)\] "(?P<method>\S+)? (?P<url>\S+)? \S+" (?P<status>\d{3})'
    match = re.match(pattern, line)
    if match:
        return match.groupdict()
    return None

def analyze_log(file_path):
    ip_counter = Counter()
    date_counter = Counter()
    not_found_urls = []

    with open(file_path, 'r') as log_file:
        for line in log_file:
            parsed = parse_log_line(line)
            if parsed:
                ip_counter[parsed['ip']] += 1
                date = parsed['date'].split(':')[0]
                date_counter[date] += 1
                if parsed['status'] == '404':
                    not_found_urls.append(parsed['url'])

    print("\n--- Apache Log Analysis ---")
    print(f"Total requests: {sum(ip_counter.values())}")
    print("\nTop 5 IP addresses:")
    for ip, count in ip_counter.most_common(5):
        print(f"{ip}: {count} requests")

    print("\nRequests per day:")
    for date, count in sorted(date_counter.items()):
        print(f"{date}: {count} requests")

    print("\n404 Not Found URLs:")
    for url in not_found_urls[:10]:
        print(url)

# Run the analyzer
if __name__ == "__main__":
    analyze_log("access.log")
