#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20110902
#  @date          20140714
#  @brief         This program can copy, compress files to another target place.

import sys
import os
from datetime import datetime
import time
import tarfile

# ex. D:\\mywiki\\dokuwiki\\data
SOURCE_PATH = os.path.join("D:", os.path.sep,
                           "mywiki", "dokuwiki", "data")
SOURCE_DIR = ('pages', 'media')

# ex. D:\\Dropbox
TARGET_PATH = os.path.join("D:", os.path.sep,
                           "Dropbox")
TARGET_DIR = ('com_sharing',)

### 7zip cmd mode ###
# a: add file
# -mhe: hide filename
# -t7z: compress to 7zip
# -p: password

# ex. D:\\7zip\\7z.exe a -mhe -t7z -pyour_pwd
COMPRESSION_MAIN = os.path.join("D:", os.path.sep,
                                "7zip", "7z.exe") + " a -mhe -t7z -pmy_pwd"
DEFAULT_OUTPUT = 'pages'

def __compression(compress_type, compress_input, compress_output):
    """
    @desc   compression files/directories by compression format.

    @param  (String) gzip or 7zip
            (Tuple) Waiting to compress files/directories absoulte path
            (String) Output absolute path
    """
    if compress_type == 'gzip':
        tar = tarfile.open("%s.tar.gz" % compress_output, "w:gz")
        for source in compress_input:
            tar.add(source, arcname=source.split(os.sep)[-1])

        tar.close()
    elif compress_type == '7zip':
        cmd = "{0} \"{1}\" {2}".format(COMPRESSION_MAIN,
                                       compress_output, " ".join(compress_input))
        os.system(cmd)
    else:
        print("No found this compression type.")

def main(compress_type, output):
    """
    @desc   main function

    @param  (String) gzip or 7zip
            (String) Compress output path (absolute)
    """
    today = datetime.now().strftime('%y-%m-%d')

    for output_dir in TARGET_DIR:
        input_path = []
        for backup_folder in SOURCE_DIR:
            input_path.append(os.path.join(SOURCE_PATH, backup_folder))

        output_path = os.path.join(TARGET_PATH, output_dir,
                                   "%s(%s)" % (output, today))

        __compression(compress_type.lower(), input_path, output_path)

        time.sleep(2)

if __name__ == '__main__':
    """
    @desc   Get arguments and Run compression procedure
    """

    compress_output = ''
    if len(sys.argv) > 2:
        compress_output = sys.argv[2]
    else:
        compress_output = DEFAULT_OUTPUT

    if len(sys.argv) > 1:
        compress_type = sys.argv[1]
    else:
        compress_type = '7zip'              # gzip or 7zip

    main(compress_type, compress_output)
