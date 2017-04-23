class SignAdder:

    def __init__(self, filename):
        self.mysign = "\nFile was edited by Eugene Leonov\n"
        self.signed_file = filename

    def __enter__(self):
        try:
            print("Trying add sign to file: ", self.signed_file)
            self.file = open(self.signed_file, 'a')
        except PermissionError as e:
            print("Permission denied. Try sign another file")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.write(self.mysign)
        print('Sign added to file')
        self.file.close()

with SignAdder('qwe1.txt') as sa:
    sa.write("qweqwe")


