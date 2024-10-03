import sys
from datetime import datetime, timezone


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def main():
    utc_date_time = datetime.now(timezone.utc)
    print(f'{utc_date_time = }')

    utc_just_date = datetime.now(timezone.utc).date()
    print(f'{utc_just_date = }')

    print(f'UTC  year: {utc_just_date.year}, month: {utc_just_date.month}, day: {utc_just_date.day}')


if __name__ == '__main__':
    print(f'Python version {get_python_version()}')
    main()
