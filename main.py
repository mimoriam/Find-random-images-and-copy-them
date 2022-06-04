import os
import shutil
import glob
import random
import re
import shelve


def main():
    username = os.getlogin()
    extension = ["png", "jpg", "jpeg"]
    files = []
    img_dir = f"C:\\Users\\{username}\\Desktop\\Images"
    document_folder_to_be_created = f"C:\\Users\\{username}\\Documents\\AAA0"
    sh = shelve.open(f"C:\\Users\\{username}\\AppData\\Roaming\\counter")

    inp = int(input("Enter the number of pictures: "))

    os.chdir(img_dir)

    [files.extend(glob.glob("*." + e)) for e in extension]
    print(files)

    if os.path.exists(f"{document_folder_to_be_created}"):
        src = os.path.realpath(f"{document_folder_to_be_created}")
        counter = re.sub("^(.+?)AAA", "", src)
        counter = int(counter)
        if sh.get("counter") == None:
            sh["counter"] = counter + 1

        sh["counter"] = sh.get("counter") + 1
        os.rename(
            f"{document_folder_to_be_created}",
            f"{document_folder_to_be_created}{((sh.get('counter')))}",
        )

    if not os.path.exists(document_folder_to_be_created):
        os.makedirs(document_folder_to_be_created)

    total_files = len(files) - 1

    for i in range(inp):

        findRandFiles = random.randint(0, total_files)
        if os.path.exists(f"{document_folder_to_be_created}"):
            shutil.copyfile(
                f"{img_dir}\\{files[findRandFiles]}",
                f"{document_folder_to_be_created}\\{files[findRandFiles]}",
            )

    sh.close()


if __name__ == "__main__":
    main()
