import os
import shutil


def compare_photos():
    file1 = r'G:\win 10\USB\2014'  # Photos to be checked and deleted.

    file2 = r'H:\Media\Photos+Video\2014 Needs Sorted'  # Primary location.
    dupphotos_file = os.path.join(file1, 'DUPLICATEPHOTOS')
    print(file1)

    for i in os.listdir(file1):
        img1 = (os.path.join(file1, i))
        img1_size = os.path.getsize(img1)
        for o in os.listdir(file2):
            img2 = (os.path.join(file2, o))
            img2_size = os.path.getsize(img2)
            if i == o and img1_size == img2_size:
                if not os.path.exists(dupphotos_file):
                    os.makedirs(dupphotos_file)
                print("Match at: " + img1 + " --and-- " + img2)
                shutil.move(img1, dupphotos_file)

    print("Completed!")


compare_photos()
