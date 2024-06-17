import os
import sys
from PIL import Image, ImageOps

def main():
    file_name_in, file_name_out = get_filename(sys.argv)
    image_in = Image.open(file_name_in)
    shirt_mask = Image.open("shirt.png")
    size = shirt_mask.size

    im_fited = ImageOps.fit(image_in, size)

    im_fited.paste(shirt_mask, shirt_mask)
    im_fited.save(file_name_out)


def check_valid_extencions(file_name_1, file_name_2):
    if file_name_1 != file_name_2:
        sys.exit("Extensions are not the same")
    if file_name_1 == ".jpg" or file_name_1 == ".jpeg" or file_name_1 == ".png":
         return True

def check_paths_exist(directory_path_1, directory_path_2):
     if os.path.exists(directory_path_1):
        return True
     else:
          sys.exit(f"Directory {directory_path_1} does not exist")

def get_filename(argv):
    if len(argv) > 3:
            sys.exit("Too many command-line arguments")
    if len(argv) < 3:
            sys.exit("Too few command-line arguments")

    file_name_in  = argv[1]
    file_name_out = argv[2]

    in_ext = os.path.splitext(file_name_in)[-1]
    out_ex = os.path.splitext(file_name_out)[-1]

    if check_valid_extencions(in_ext, out_ex) and check_paths_exist(file_name_in, file_name_out):
        return (file_name_in, file_name_out)

if __name__ == "__main__":
    main()
