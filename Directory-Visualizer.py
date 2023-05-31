import os


class DirectoryTreePrinter:
    def __init__(self, root_path, prefix='', folder_prefix='┗ ', file_prefix='┗ ', print_files=True):
        self.root_path = root_path
        self.prefix = prefix
        self.folder_prefix = folder_prefix
        self.file_prefix = file_prefix
        self.print_files = print_files

    def print(self):
        self._print_directory_tree(self.root_path, self.prefix, self.folder_prefix, self.file_prefix, self.print_files)

    def _print_directory_tree(self, root_path, prefix, folder_prefix, file_prefix, print_files):
        if os.path.isdir(root_path):
            files = []
            folders = []
            for file in os.listdir(root_path):
                full_path = os.path.join(root_path, file)
                if os.path.isdir(full_path):
                    folders.append(file)
                elif os.path.isfile(full_path) and print_files:
                    files.append(file)

            folders.sort()
            for i, folder in enumerate(folders):
                last = i == (len(folders) - 1)
                if last:
                    new_prefix = prefix + folder_prefix
                    new_prefix_indent = '   '
                else:
                    new_prefix = prefix + '┣ ' + folder_prefix[1:]
                    new_prefix_indent = '┃  '

                print(prefix + folder_prefix + '📂 ' + folder)
                self._print_directory_tree(
                    os.path.join(root_path, folder),
                    prefix=new_prefix + new_prefix_indent,
                    folder_prefix=folder_prefix + ' ┃ ',
                    file_prefix=file_prefix + '   ',
                    print_files=print_files
                )

            if print_files:
                files.sort()
                for i, file in enumerate(files):
                    last = i == (len(files) - 1) and not folders
                    if last:
                        new_prefix = prefix + file_prefix
                    else:
                        new_prefix = prefix + '┣ ' + file_prefix[1:]
                    print(new_prefix + '📜 ' + file)

        elif os.path.isfile(root_path) and print_files:
            print(prefix + file_prefix + '📜 ' + os.path.basename(root_path))
