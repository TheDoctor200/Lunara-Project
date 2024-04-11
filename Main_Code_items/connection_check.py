import requests
import time

def check_internet_connection():
    try:
        requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def main():
    while True:
        if check_internet_connection():
            print("1")
        else:
            print("2")
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    main()

# Comment on if statements:
# 1 = Internet conn. present
# 2 = offline