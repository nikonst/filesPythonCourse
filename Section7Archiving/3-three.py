import shutil

# shutil.make_archive(base_name, format, root_dir)
shutil.make_archive('data/backup', 'tar', 'somefolder')

shutil.unpack_archive('data/backup.tar','extractfolder/')