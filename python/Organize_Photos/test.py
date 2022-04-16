
from exiftool import ExifToolHelper
with ExifToolHelper() as et:
    for d in et.get_metadata("G:\\BackupPictures\\10 a cc muir\\CIMG0646.JPG"):
        print(d["SourceFile"])
        print(d["File:FileName"])
        print(d["File:FileModifyDate"])
        print(d["File:MIMEType"])
        # print(d[""])
        # print(d[""])
        # print(d[""])
        # for k, v in d.items():
        #     print(f"{k} = {v}")