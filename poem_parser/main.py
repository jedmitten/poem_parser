import json
import click

from poem_parser import poetryminute as pm


@click.command()
def main():
    poetry_minute = pm.get_poems()
    print(json.dumps(poetry_minute, indent=4, sort_keys=True))


if __name__ == '__main__':
    main()
