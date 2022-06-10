from app.core import Parser
from config import DRIVER_PATH


def main():
    parser = Parser('--headless', DRIVER_PATH)
    parser.run()


if __name__ == '__main__':
    main()