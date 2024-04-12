import click
from docaitor.core.data_loader import DataLoader
from docaitor.core.output_generator import OutputGenerator
from docaitor.core.data_merge import merge_data


@click.group()
@click.version_option()
def cli(): ...


@click.command()
@click.option("-o", "--output-file", required=True, help="name of the output file")
@click.option(
    "-i", "--input-file", multiple=True, required=True, help="name of the input file(s)"
)
@click.option("-t", "--template-file", required=True, help="name of the template file")
@click.option(
    "-d",
    "--template-directory",
    default=".",
    help="directory where templates are located",
)
@click.option("-v", "--verbose", count=True, help="verbosity level")
@click.option(
    "--debug", is_flag=True, default=False, help="turn on debugging information"
)
def generate(
    output_file: str,
    input_file: list[str],
    template_file: str,
    template_directory: str,
    verbose: int,
    debug: bool,
):
    data_list = [DataLoader(i).load() for i in input_file]
    data = merge_data(data_list)

    with open(output_file, "wt") as fp:
        OutputGenerator(data, template_file, template_directory, fp).generate()


cli.add_command(generate)
