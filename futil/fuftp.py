# Download files from FTP
from ftplib import FTP, all_errors as ftp_errors
from os import path
from io import open
from contextlib import closing

class FtpClient():
    def __init__(self, config):
        self.config = config
        self.host = self.config.FTP_HOST

    ### Downloads all files in the FTP folder - specified in appconfig to temp folder
    def download_all(self):
        downloadedfiles = []

        ftp = FTP(self.config.FTP_HOST)
        with closing(ftp):
            try:
                ftp.port = self.config.FTP_PORT
                ftp.login(user=self.config.FTP_USERNAME, passwd=self.config.FTP_PWD)

                ## change working directory if needed
                if self.config.FTP_DIR != None:
                    ftp.cwd(self.config.FTP_DIR)
                
                files = []
                ## list all files in directory
                ftp.retrlines("LIST {}".format(self.config.FTP_FILTER), files.append)
                if len(files) > 0:
                    for f in files:
                        words = f.split(None, 8)
                        filename = words[-1].lstrip()
                        print(filename)
                         ## download
                        file = open(path.join(self.config.TMP_FOLDER, filename), 'wb')
                        ftp.retrbinary('RETR '+ filename, file.write)
                        downloadedfiles.append(file.name)
                        print("File downloaded from FTP to {}".format(file.name))
                else:
                    print("No files matching filter")

               
            except ftp_errors as e:
                raise e 

        return downloadedfiles

        

