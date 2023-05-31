import os


class DirectoryPrinter:
    def __init__(self, path):
        self.path = path
    
    def print_dir(self, padding=''):
        if os.path.isdir(self.path):
            print(padding + '📂 ' + os.path.basename(self.path) + ':')
            padding = padding + ' '
            files = os.listdir(self.path)
            files.sort()
            for i, filename in enumerate(files):
                new_path = os.path.join(self.path, filename)
                if os.path.isdir(new_path):
                    if i == len(files) - 1:
                        new_padding = padding + '  '
                    else:
                        new_padding = padding + '┣ '
                    self.__class__(new_path).print_dir(new_padding + ' ')
                else:
                    if i == len(files) - 1:
                        print(padding + '┗ 📜 ' + filename)
                    else:
                        print(padding + '┣ 📜 ' + filename)
        else:
            print('Directory not found')
