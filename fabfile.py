import os

from fabric.api import local, settings
from fabric.context_managers import hide


def abs_path(relative_path, base_dir=os.path.dirname(__file__)):
    """
    Make relative paths absolute to the project directory.
    """
    return os.path.abspath(os.path.join(base_dir, relative_path))


def find_files(path, suffixes=None, exclude_dirs=None):
    if not os.path.exists(path):
        return []

    exclude_dirs = exclude_dirs or []
    found_files = []

    def include_file(filename, suffixes):
        return any([filename.endswith('.' + suffix) for suffix in suffixes])

    for root, dirs, files in os.walk(path):
        for exclude_dir in set(dirs) & set(exclude_dirs):
            dirs.remove(exclude_dir)
        found_files.extend([os.path.join(root, file) for file in files
                            if include_file(file, suffixes)])
    return found_files


def pylint():
    flake8_command = 'flake8 --ignore=E501'
    flake8_command += ',W503,E731,E265,E123,E126,F403,E266'
    py_root = abs_path('assetbankauth')

    all_files = find_files(py_root, ['py'], exclude_dirs=['migrate', 'migrations'])
    all_files.append('fabfile.py')
    if all_files:
        all_files_for_cmd = "'" + "' '".join(all_files) + "'"
        with settings(hide('aborts', 'running')):
            local('%s %s' % (flake8_command, all_files_for_cmd))
