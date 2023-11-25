import os
import shutil
import glob
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from exiftool import ExifToolHelper
from datetime import datetime




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
    if not os.path.exists(path):
        os.makedirs(path)
    # If it exists
    else:
        pass


def main():
    # Open a file
    rootdir = 'D:\\PUT_NEW_IMAGES_HERE'
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if os.path.isfile(os.path.join(subdir, file)):
                # print(os.path.join(subdir, file))
                try:
                    exif = {}
                    extension = file.split('.')[1]
                    file_path = os.path.join(subdir, file)
                    
                    if extension.upper() not in ['JPG','PNG','WEBP']:
                        with ExifToolHelper() as et:
                            for d in et.get_metadata(file_path):
                                image_date_time = d['File:FileModifyDate']
                                year = image_date_time.split(":")[0]
                                month = getMonth(image_date_time.split(":")[1])
                                image_name = d['File:FileName']
                                directory = '{}{}\\{}'.format('D:\\Video\\',year,month)
                                # print(directory)
                                checkPath(directory)
                                original = '{}'.format(d["SourceFile"])
                                # print(original)
                                target = '{}\\{}'.format(directory,image_name)
                                # print(target)
                                shutil.move(original, target)
                    
                    else:
                        image = Image.open(file_path)
                        # print(image.getexif().items())
                        
                        for tag, value in image.getexif().items():
                            if tag in TAGS:
                                exif[TAGS[tag]] = value 
                        if 'DateTime' in exif:
                            image_date_time = exif['DateTime']
                        else:
                            creation_time = os.path.getctime(file_path)
                            image_date_time = datetime.fromtimestamp(creation_time).strftime('%Y:%m:%d %H:%M:%S')

                        image.close()
                        year = image_date_time.split(":")[0]
                        month = getMonth(image_date_time.split(":")[1])
                        image_split_path = file_path.split('\\')
                        image_name = image_split_path[len(image_split_path) - 1]
                        
                    
                        directory = '{}{}\\{}'.format('D:\\Photos\\',year,month)
                        
                        checkPath(directory)
                        original = f'{file_path}'
                        
                        target = f'{directory}\\{image_name}'
                        
                        
                        shutil.move(original, target)
                        
                except Exception as e:
                    print(f"Error: {e} for object {file_path}");
                    # pass
                    

   


if __name__ == "__main__":
    main()