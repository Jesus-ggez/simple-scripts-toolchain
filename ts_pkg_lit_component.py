from sys import argv as term_args


from templates._ts_pkg_lit_component import (
    component_template,
    model_template,
    css_template,
)

from utils import (
    __create_file_and_exit,
    __move_to,
    __main__,
)


@__main__
def main() -> None:
    for component_name in term_args[1:]:
        # src/components
        __move_to('components')
        __create_file_and_exit(
            name=component_name + '.ts',
            content=component_template
        )

        # src/models
        __move_to('models')
        __create_file_and_exit(
            name=component_name + '.ts',
            content=model_template,
        )

        # src/styles
        __move_to('styles')
        __create_file_and_exit(
            name=component_name + '.css',
            content=css_template,
        )
