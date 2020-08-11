import os
from datetime import datetime
import shutil




def sort_year():
    file = r'G:\win 10\USB'

    for i in os.listdir(file):
        mod_date = os.path.getmtime(os.path.join(file, i))
        create_date = os.path.getctime(os.path.join(file, i))
        if mod_date < create_date:
            folder = datetime.utcfromtimestamp(mod_date).strftime('%B %Y')
        else:
            folder = datetime.utcfromtimestamp(create_date).strftime('%B %Y')
        year = folder.split( )
        if not os.path.exists(os.path.join(file, year[1])):
            os.makedirs(os.path.join(file, year[1]))
        shutil.move(os.path.join(file, i), os.path.join(file, year[1]))

sort_year()