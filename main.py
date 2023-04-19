import os
import argparse
import toml
from utils import auto_login
import time


def get_user(config):
    username = None
    password = None
    if config == "osenv":
        username = os.environ["BUAA_USERNAME"]
        password = os.environ["BUAA_PASSWORD"]
    else:
        config = toml.load(config)
        username = config["username"]
        password = config["password"]
    return username, password


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c",
                        "--config",
                        help="load config file or use osenv",
                        default="osenv")
    args = parser.parse_args()
    user, pwd = get_user(args.config)
    while True:
        print()
        print("=" * 80)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
        auto_login(user, pwd)
        print("=" * 80)
        print()
        time.sleep(60 * 30)  # 30 分钟检查一次


if __name__ == '__main__':
    main()
