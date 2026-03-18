import os


from typing import Callable


from _ts_ini_templates import counter_model, counter_component, counter_style


__move_to: Callable = os.chdir
__exec: Callable = os.system
__create_dir: Callable = os.mkdir


def __create_and_move_back(name: str, content: str, move_to: str) -> None:
    __move_to(move_to)
    with open(name, 'w') as item:
        item.write(content)
    __move_to('..')


def _fill_fold_struct() -> None:
    __move_to('src')

    __create_and_move_back(
        content=counter_component,
        move_to='components',
        name='xCounter.ts',
    )

    __create_and_move_back(
        content=counter_model,
        name='counter.ts',
        move_to='models',
    )

    __create_and_move_back(
        content=counter_style,
        name='counter.css',
        move_to='styles',
    )
    __move_to('..')


def _alloc_index_in_root() -> None:
    __move_to('src')
    __exec('mv index.css ..')
    __move_to('..')


def _clean_src() -> None:
    __exec('rm -r src/*')


def _create_main_ts() -> None:
    template: list[str] = [
        "import { XCounter } from './src/components/xCounter';",
        '',
        '',
        'declare global {',
        '    interface HTMLElementTagNameMap {',
        "        'x-counter': XCounter;",
        '    }',
        '}',
    ]
    with open('main.ts', 'w') as main_ts:
        main_ts.writelines(t + '\n' for t in template)


def _create_fold_structure() -> None:
    __move_to('src')

    __create_dir('components')
    __create_dir('models')
    __create_dir('styles')

    __move_to('..')


def _fmt_index_html() -> None:
    old_doc: list[str] = []

    double_space: str = '  '

    with open('index.html', 'r') as index:
        for line in index.readlines():
            striped_starts: Callable = line.strip().startswith

            if striped_starts('<link'):
                line = line.replace('./src/', '')

            if striped_starts('<script'):
                line = line.replace('src/my-element', 'main')

            if striped_starts('<my-element'):
                line = line.replace('my-element', 'x-counter></x-counter')

            if striped_starts('</my-element') or striped_starts('<h1'):
                continue

            old_doc.append(
                line.replace(
                    double_space,
                    double_space*2
                )
            )

    with open('index.html', 'w') as index:
        index.writelines(old_doc)


def main() -> None:
    _alloc_index_in_root()
    _clean_src()
    _create_fold_structure()
    _fill_fold_struct()
    _create_main_ts()
    _fmt_index_html()


if __name__ == '__main__':
    main()
