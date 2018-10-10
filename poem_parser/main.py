import click

from poem_parser import poetryminute as pm


@click.command()
def main():
    pm.get_page_by_dir(pm.DATE)


if __name__ == '__main__':
    main()
