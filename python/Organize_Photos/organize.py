import os
import shutil
import glob
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS



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


def main():
    # Open a file
    path = r"G:\\"


    
    rootdir = 'G:\\'
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if os.path.isfile(os.path.join(subdir, file)):
                # print(os.path.join(subdir, file))
                try:
                    exif = {}
                    image_path = os.path.join(subdir, file)
                    image = Image.open(image_path)
                    
                    for tag, value in image.getexif().items():
                        if tag in TAGS:
                            exif[TAGS[tag]] = value
                    image_date_time = exif['DateTime']
                    image.close()
                    year = image_date_time.split(":")[0]
                    month = getMonth(image_date_time.split(":")[1])
                    image_split_path = image_path.split('\\')
                    image_name = image_split_path[len(image_split_path) - 1]
                    # print(year, month, image_name)
                
                    directory = '{}{}\\{}'.format('E:\\',year,month)
                    # print(directory)
                    checkPath(directory)
                    original = '{}'.format(image_path)
                    # print(original)
                    target = '{}\\{}'.format(directory,image_name)
                    # print(target)

                    shutil.copy(original, target)
                except Exception as e:
                    print(f"Error: {e} for object {image_path}");
                    # pass
                    

   


if __name__ == "__main__":
    main()