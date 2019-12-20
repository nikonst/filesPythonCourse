# https://docs.python.org/3.8/library/pathlib.html?highlight=path#module-pathlib
# TO BE LEFT OUT?????
'''

Path.is_dir()¶

    Return True if the path points to a directory (or a symbolic link pointing to a directory), False if it points to another kind of file.

    False is also returned if the path doesn’t exist or is a broken symlink; other errors (such as permission errors) are propagated.

Path.is_file()

    Return True if the path points to a regular file (or a symbolic link pointing to a regular file), False if it points to another kind of file.

    False is also returned if the path doesn’t exist or is a broken symlink; other errors (such as permission errors) are propagated.


Path.iterdir()

    When the path points to a directory, yield path objects of the directory contents:
    >>>

    >>> p = Path('docs')
    >>> for child in p.iterdir(): child
    ...
    PosixPath('docs/conf.py')
    PosixPath('docs/_templates')
    PosixPath('docs/make.bat')
    PosixPath('docs/index.rst')
    PosixPath('docs/_build')
    PosixPath('docs/_static')
    PosixPath('docs/Makefile')

Path.mkdir(mode=0o777, parents=False, exist_ok=False)
Path.rename(target)
Path.replace(target)
    Rename this file or directory to the given target, and return a new Path instance pointing to target. If target points to an existing file or directory, it will be unconditionally replaced.

Path.rmdir()
    Remove this directory. The directory must be empty.
Path.touch(mode=0o666, exist_ok=True)
    Create a file at this given path. If mode is given, it is combined with the process’ umask value to determine the file mode and access flags. If the file already exists, the function succeeds if exist_ok is true (and its modification time is updated to the current time), otherwise FileExistsError is raised.




'''