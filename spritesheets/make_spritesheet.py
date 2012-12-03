#!/usr/bin/env python
#coding: utf-8

"""
To help make spritesheets for mobile devices. The spritesheets can be used
by cocos2d-iphone or cocos2d-x framework.

## Credits

Author: Zhu Tao<zhutao.iscas@gmail.com>
Blog: http://towerjoo.github.com

## How To Use

run *python make_spritesheet.py -h* to show the help
"""
import Image, ImageDraw
import os, sys
from optparse import OptionParser

DEFAUlT_CANVAS_WIDTH = 1024 # default canvas width in px, which will be used to calculate the canvas height needed

skeleton = \
"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>texture</key>
	<dict>
		<key>width</key>
		<integer>%(canvas_width)s</integer>
		<key>height</key>
		<integer>%(canvas_height)s</integer>
	</dict>
	<key>frames</key>
	<dict>
    %(content)s
    </dict>
</dict>
</plist>"""
item_skeleton = """
		<key>%(key)s</key>
		<dict>
			<key>x</key>
			<integer>%(x)d</integer>
			<key>y</key>
			<integer>%(y)d</integer>
			<key>width</key>
			<integer>%(width)d</integer>
			<key>height</key>
			<integer>%(height)d</integer>
			<key>offsetX</key>
			<real>0</real>
			<key>offsetY</key>
			<real>0</real>
			<key>originalWidth</key>
			<integer>%(width)d</integer>
			<key>originalHeight</key>
			<integer>%(width)d</integer>
		</dict>
"""

def is_image(filename):
    suffixes = ["png", "jpg", "gif"]
    for s in suffixes:
        if filename.endswith(s):
            return True

    return False

def gen_file_name(config, i):
    FILENAME_PATTERN = config.get("FILENAME_PATTERN")
    start_index = config.get("start_index")
    end_index = config.get("end_index")
    FILENAME_LEN = config.get("FILENAME_LEN")
    CHECK_FILENAME_LEN = config.get("CHECK_FILENAME_LEN")

    filename = FILENAME_PATTERN % i
    if CHECK_FILENAME_LEN and len(filename) < FILENAME_LEN:
        filename = "0" * (FILENAME_LEN - len(filename)) + filename
    return filename

        
    

def do_process(res_dir, config):
    ITEM_WIDTH = config.get('ITEM_WIDTH')
    ITEM_HEIGHT = config.get('ITEM_HEIGHT')
    SPACING = config.get('SPACING')
    TEXTURE = config.get('TEXTURE')
    PLIST = config.get('PLIST')
    FILENAME_PATTERN = config.get("FILENAME_PATTERN")
    start_index = config.get("start_index")
    end_index = config.get("end_index")
    FILENAME_LEN = config.get("FILENAME_LEN")
    CHECK_FILENAME_LEN = config.get("CHECK_FILENAME_LEN")

    files = [gen_file_name(config, i) for i in range(start_index, end_index+1)]
    num = len(files)

    cols = DEFAUlT_CANVAS_WIDTH / ITEM_WIDTH
    #if DEFAUlT_CANVAS_WIDTH % ITEM_WIDTH != 0:
    #    cols += 1
    rows = num / cols
    if num % cols != 0:
        rows += 1
    CANVAS_HEIGHT = rows * ITEM_HEIGHT
    CANVAS_WIDTH = DEFAUlT_CANVAS_WIDTH

    size = CANVAS_WIDTH, CANVAS_HEIGHT
    im = Image.new("RGBA", size, color=255)

    out = ""
    i = 0
    for c in range(cols):
        for r in range(rows):
            if i >= num: break
            box = (c * ITEM_WIDTH, r * ITEM_HEIGHT)
            image = files[i]
            print "%s is processed" % image
            path = os.path.join(res_dir, image)
            pim = Image.open(path)
            pim.thumbnail((ITEM_WIDTH, ITEM_HEIGHT), Image.ANTIALIAS)   # make it in the right size
            im.paste(pim, box)
            dic = {
                "key" : image,
                "x" : c * ITEM_WIDTH,
                "y" : r * ITEM_HEIGHT,
                "width" : ITEM_WIDTH,
                "height" : ITEM_HEIGHT,
                }
            out += item_skeleton % dic
            i += 1
    im.save(os.path.join(res_dir, TEXTURE))
    out_dic = {
        "canvas_height" : CANVAS_HEIGHT,
        "canvas_width" : CANVAS_WIDTH,
        "content" : out,
    }
    out = skeleton % out_dic
    fh = open(os.path.join(res_dir, PLIST), "w")
    fh.write(out)
    fh.close()

        
def handle_args():
    parser = OptionParser()
    parser.add_option("-d", "--dir", dest="res_dir", help="Directory of the original resources")
    parser.add_option("-c", "--config", dest="config", help="Config for the processing")

    (options, args) = parser.parse_args()
    res_dir, config = options.res_dir, options.config
    if res_dir and config:
        pass
    else:
        print "-d and -c cannot be null"
        parser.print_help()
        sys.exit(0)
    fh = open(config)
    codes = fh.read()
    fh.close()
    exec(codes)
    do_process(res_dir, CONFIG)

        
if __name__ == "__main__":
    handle_args()





