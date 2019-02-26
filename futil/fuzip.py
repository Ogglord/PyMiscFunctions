from io import BytesIO, open
from zipfile import ZipFile, ZIP_DEFLATED
from tempfile import gettempdir,_RandomNameSequence
from os import path

class Zip():
    def __init__(self, config):
        self.config = config
        self.randomname = _RandomNameSequence()


    def gettempfile(self):
        return path.join(self.config.TMP_FOLDER,self.randomname.__next__() + ".zip")

    def zipfiles(self, fileasarray):
        tmpzip = self.gettempfile()

        zip_buffer = BytesIO()
        with ZipFile(zip_buffer, "a", ZIP_DEFLATED, False) as zip_file:
            for file_name, data in fileasarray:
                zip_file.writestr(file_name, data.getvalue())
        with open(tmpzip, 'wb') as f:
            f.write(zip_buffer.getvalue())
        print("Successfully zipped files to temp file")
        return tmpzip

