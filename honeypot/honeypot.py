import configuration
import thread_http, thread_https, thread_ssh
import argparse
import threading


def get_args():
    parser = argparse.ArgumentParser(description='Python honeypot')
    parser.add_argument('--prod', action='store_true')
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    print("Starting the server.")
    threads = []
    if args.prod:
        print("Server started in production mode.")
        configuration.init('prod')
    else:
        print("Server started in dev mode.")
        configuration.init('dev')
    # Create thread list with all honepot services
    threads.append(threading.Thread(target=thread_ssh.start_ssh_honeypot))
    threads.append(threading.Thread(target=thread_http.start_http_honeypot))

    threads.append(threading.Thread(target=thread_https.start_https_honeypot))
    # Start threads
    for thread in threads:
        thread.start()
