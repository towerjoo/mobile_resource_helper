#!/usr/bin/env python
#coding: utf-8

"""
To help generate the resources to fit different resolution for iOS devices, 
and Android Devices.
"""
import sys, os
import Image
from optparse import OptionParser
class HelperBase(object):
    dpi_ratios = ()
    def __init__(self):
        self.warnings = []

    def handle_resources(self, res_dir, output, ready_to_process):
        self.ready_to_process = ready_to_process
        self.output = output
        self.res_dir = res_dir
        if not os.path.isdir(self.res_dir):
            print "The specified original resource directory is NOT a directory"
            return
        self.handle(self.res_dir)

    def is_image(self, filename):
        valid_suffix = ["png", "jpg", "jpeg", "gif"]
        for suffix in valid_suffix:
            if filename.endswith(suffix):
                return True
        return False

    def handle(self, res_dir):
        if not self.ready_to_process:
            return
        for item in os.listdir(res_dir):
            path = os.path.join(res_dir, item)
            if os.path.isdir(path):
                self.handle(path)
            else:
                self.do_handle(path)

    def output_name(self, name, ratio=1):
        """can be overrided to provide a different output name
        e.g for iOS, filename@2x.png, etc.
        """
        return name

    def do_handle(self, path):
        if not self.is_image(path):
            return
        for dpi_ratio in self.dpi_ratios:
            img = Image.open(path)
            target_width = img.size[0] * dpi_ratio[1]
            target_height = img.size[1] * dpi_ratio[1]
            target_res_folder = os.path.join(self.output, dpi_ratio[0], os.path.dirname(path))
            if os.path.exists(self.output) and not os.path.exists(target_res_folder):
                os.makedirs(target_res_folder)
            target_res_filename = os.path.join(target_res_folder, self.output_name(path.split(os.path.sep)[-1], dpi_ratio[1]))
            img.thumbnail((int(target_width), int(target_height)), Image.ANTIALIAS)
            print "%s is saved" % target_res_filename
            img.save(target_res_filename)

class AndroidHelper(HelperBase):
    dpi_ratios = (('drawable-ldpi',0.325),
                  ('drawable-mdpi',0.5),
                  ('drawable-hdpi',0.75),
                  ('drawable-xhdpi',1))

    def __init__(self):
        print "handling android resources ..."

class iPhoneHelper(HelperBase):
    dpi_ratios = (('iphone',0.5),
                  ('iphone-retina',1))

    def __init__(self):
        print "handling iPhone resources ..."

    def output_name(self, name, ratio):
        prefix, suffix = name.split(".")
        if ratio == 0.5:
            return "%s.%s" % (prefix, suffix)
        else:
            return "%s@2x.%s" % (prefix, suffix)


class iPadHelper(HelperBase):
    dpi_ratios = (('ipad',0.5),
                  ('ipad-retina',1))

    def __init__(self):
        print "handling iPad resources ..."

    def output_name(self, name, ratio):
        prefix, suffix = name.split(".")
        if ratio == 0.5:
            return "%s~ipad.%s" % (prefix, suffix)
        else:
            return "%s@2x~ipad.%s" % (prefix, suffix)

def handle_args():
    parser = OptionParser()
    parser.add_option("-d", "--dir", dest="res_dir", help="Directory of the original resources")
    parser.add_option("-o", "--output", dest="output", help="output of the handled resources(current dir as default)", default=".")
    parser.add_option("-p", "--platform", dest="platform", help="platform to generate(android or iPhone or iPad, 'all' as default)", default="all")

    (options, args) = parser.parse_args()
    if options.res_dir is None:
        parser.print_help()
        ready_to_process = False
        sys.exit(0)
    else:
        res_dir = options.res_dir
        output = options.output
        platform = options.platform
        ready_to_process = True
        if platform == "all":
            a = AndroidHelper()
            a.handle_resources(res_dir, output, platform)
            a = iPhoneHelper()
            a.handle_resources(res_dir, output, platform)
            a = iPadHelper()
            a.handle_resources(res_dir, output, platform)
        elif platform == "android":
            a = AndroidHelper()
            a.handle_resources(res_dir, output, platform)
        elif platform == "iPhone":
            a = iPhoneHelper()
            a.handle_resources(res_dir, output, platform)
        elif platform == "iPad":
            a = iPadHelper()
            a.handle_resources(res_dir, output, platform)

    
if __name__ == "__main__":
    handle_args()
        
        


