# -*- coding: utf-8 -*-

"""Console script for just_a_package."""

import click


@click.command()
def main(args=None):
    """Console script for just_a_package."""
    click.echo("Replace this message by putting your code into "
               "just_a_package.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


if __name__ == "__main__":
    main()
