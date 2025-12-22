from datetime import datetime, timedelta
import csv

requests = [
    ("2025-12-16 10:00:01", "user1"),
    ("2025-12-16 10:00:10", "user1"),
    ("2025-12-16 10:00:20", "user1"),
    ("2025-12-16 10:00:30", "user1"),
    ("2025-12-16 10:00:40", "user1"),
    ("2025-12-16 10:00:50", "user1"),  # BLOCKED
    ("2025-12-16 10:01:10", "user1"),  # ALLOWED
    ("2025-12-16 10:00:05", "user2"),
]

def rate_limiter(requests):
    user_requests = {}
    results = []

    for time_str, user in requests:
        now = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

        user_requests.setdefault(user, [])
        window_start = now - timedelta(minutes=1)

        user_requests[user] = [t for t in user_requests[user] if t >= window_start]

        if len(user_requests[user]) < 5:
            user_requests[user].append(now)
            results.append((time_str, user, "ALLOWED", ""))
        else:
            results.append((time_str, user, "BLOCKED", "Rate limit exceeded"))

    return results

def main():
    results = rate_limiter(requests)

    with open("output.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "user", "status", "reason"])
        writer.writerows(results)

    for r in results:
        print(r)

if __name__ == "__main__":
    main()
