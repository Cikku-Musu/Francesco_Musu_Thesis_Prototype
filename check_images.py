from PIL import Image
import os

def check_images(s_dir, ext_list):
    bad_images = []
    for fldr in os.listdir(s_dir):
        sub_folder = os.path.join(s_dir, fldr)
        if os.path.isdir(sub_folder):
            for file in os.listdir(sub_folder):
                f_path = os.path.join(sub_folder, file)
                if os.path.isfile(f_path):
                    if file.split('.')[-1].lower() in ext_list:
                        try:
                            img = Image.open(f_path)
                            img.verify()  # Verify that it is, in fact, an image
                        except (IOError, SyntaxError) as e:
                            print('Bad file:', f_path)  # Print out the names of corrupt files
                            bad_images.append(f_path)
    return bad_images

exts = ['jpg', 'jpeg']  # Adjust file extensions as needed
bad_files = check_images(r'C:\\Users\\cikku\\Documents\\ThesisPrototype\\dataset', exts)
print('Corrupt image files:', bad_files)
