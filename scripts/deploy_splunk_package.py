from logging import error
import splunklib.client as client
import os
import argparse


def upload_ta(url, user, password, host, port):
    service = client.connect(
        host=host, port=port, username=user, password=password, verify=False
    )
    service.post(path_segment="apps/local", filename=True, name=url, update=True)
    service.logout()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str)
    parser.add_argument("--user", type=str)
    parser.add_argument("--password", type=str)
    parser.add_argument("--host", type=str)
    parser.add_argument("--port", type=str)
    args = parser.parse_args()
    upload_ta(args.url, args.user, args.password, args.host, args.port)


if __name__ == "__main__":
    main()
