import os
import shutil
import glob
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from exiftool import ExifToolHelper


def getMonth(month):
    months = {
        '01':'January',
        '02':'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }

    return months.get(month, 'Month not found')

def checkPath(path):
    # If it does not exist
    if os.path.exists(path) == False:
        os.makedirs(path)
    # If it exists
    else:
        pass


with open("ReorganizeErrors.txt","r") as file_text:
    lines = file_text.readlines()
    for line in lines:
        try:
            image_trim = line.split("** ")[1] 
            image_obj = image_trim.split("\n")[0]

            # exif = {}
            
            with ExifToolHelper() as et:
                for d in et.get_metadata(image_obj):
                    file_type = d["File:MIMEType"]
                    if "video" in file_type:
                        # print(d["SourceFile"])
                        # print(d["File:FileName"])
                        # print(d["File:FileModifyDate"])
                        # print("\n")
                        image_date_time = d['File:FileModifyDate']
                        year = image_date_time.split(":")[0]
                        month = getMonth(image_date_time.split(":")[1])
                        image_name = d['File:FileName']
                        directory = '{}{}\\{}'.format('E:\\Video\\',year,month)
                        # print(directory)
                        checkPath(directory)
                        original = '{}'.format(d["SourceFile"])
                        # print(original)
                        target = '{}\\{}'.format(directory,image_name)
                        # print(target)

                        shutil.copy(original, target)
                    else:
                        image_date_time = d['File:FileModifyDate']
                        year = image_date_time.split(":")[0]
                        month = getMonth(image_date_time.split(":")[1])
                        image_name = d['File:FileName']
                        directory = '{}\\{}\\{}'.format('E:\\UnkownTypes',year,month)
                        checkPath(directory)

                        original = '{}'.format(d["SourceFile"])
                        # print(original)
                        target = '{}\\{}'.format(directory,image_name)
                        # print(target)

                        shutil.copy(original, target)
                        
        except Exception as e:
            print(e)