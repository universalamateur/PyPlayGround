
#!/usr/bin/python3

import os, sys
from PIL import Image

def run_Files(folder):
    # Do something with task here
    if not os.path.exists(folder[1]):
        os.makedirs(folder[1])
        print("Directory {} Created".format(folder[1]))
    print("Handling in: {} to : {}".format(folder[0], folder[1]))
    for root, directories, files in os.walk(folder[0], topdown=False):
        for name in files:
            filename=os.path.join(root, name)
            print("Source: {}".format(filename))
            f, ending_original_file = os.path.splitext(name)
            target=os.path.join(folder[1], f)
            print("Target: {}".format(target))
            try:
                with Image.open(filename) as im:
                    out = im.convert("RGB")
                    out.rotate(90).resize((128,128)).save(target, "JPEG")
            except OSError:
                print("cannot convert", filename)


def main():
    src = os.path.join(os.path.expanduser("~"), "images")
    #target = os.path.abspath(os.path.join(os.sep, 'opt', 'icons'))
    target = os.path.join(os.path.expanduser("~"),"opt", "icons")
    print(src)
    print(target)
    folders = []
    for root, _dir, files in os.walk(src):
        for name in _dir:
          folders.append([os.path.join(root, name), os.path.join(target, name)])
        folders.append([os.path.join(root), os.path.join(target)])
    print(folders)
    for elem in folders:
        run_Files(elem)


if __name__ == "__main__":
    main()