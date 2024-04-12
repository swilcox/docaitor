import jinja2
from typing import IO


class OutputGenerator:
    def __init__(
        self, data: dict, template_file: str, template_dir: str, output_stream: IO
    ):
        # TODO: explore options on the FileSystemLoader re: search paths
        # - we could optionally inject a whole directory where we'll mess with templates
        # -
        self._data = data
        self._output_stream = output_stream
        self._template_file = template_file
        self._template_dir = template_dir
        # TODO: move environment part up here maybe?

    def generate(self):
        jinja_environment = jinja2.environment.Environment(
            loader=jinja2.loaders.FileSystemLoader(self._template_dir)
        )
        template = jinja_environment.get_template(self._template_file)
        # maybe we should use .generate instead of .render
        self._output_stream.write(template.render(**self._data))
