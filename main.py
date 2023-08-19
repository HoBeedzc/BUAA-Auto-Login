import os
import argparse
import toml
from utils import auto_login, login_once
import time
import logging


def get_logger():
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s] - %(levelname)s - %(message)s')
    return logging


def get_args(logger):
    parser = argparse.ArgumentParser()
    parser.add_argument("-c",
                        "--config",
                        help="load config file or use osenv",
                        default="osenv")
    parser.add_argument("--auto-login",
                        help="auto login every 30 minutes",
                        action="store_true")
    args = parser.parse_args()
    logger.info(f"config: {args.config}")
    return args


def get_user(config, logger):
    username = None
    password = None
    if config == "osenv":
        username = os.environ["BUAA_USERNAME"]
        password = os.environ["BUAA_PASSWORD"]
    else:
        config = toml.load(config)
        username = config["username"]
        password = config["password"]
    logger.info(f"username: {username}")
    return username, password


def main():
    logger = get_logger()
    args = get_args(logger)
    user, pwd = get_user(args.config, logger)
    if args.auto_login:
        auto_login(user, pwd, logger)
    else:
        login_once(user, pwd, logger)


if __name__ == '__main__':
    main()
