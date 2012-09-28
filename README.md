Mobile Resource Helper
======================


![Logo](https://raw.github.com/towerjoo/mobile_resource_helper/master/helper_logo.png)

change resources to predefined DPIs automatically to ease the mobile development.


### Dependency

This script only depends on [PIL][PIL].


### How to Use

You need to run this script in commandline(Terminal for Mac/Linux, Dos for Win).

1. Open the commandline tool
2. go to the root directory which contains this script
3. run *python handle_resources.py -h* to know how to use

check [source][source] to get the help.

### Parameters explanation

**Usage: handle_resources.py [options]**

1. -d, --dir  Directory of the original resources
2. -o, --output output of the handled resources(current dir as default)
3. -p, --platform platform to generate(android or iPhone or iPad, 'all' as default)

### Use Case

Suppose you've gotten some high-DPI resources located in $RES dir, and wants
to convert them to fit the android's differnt DPI needs, so you can:

*python handle_resources -p android -d $RES -o $OUT*

After running, processed resources will go to $OUT directory. 

Note: replace the $RES and $OUT with the real path when your running..
 


[PIL]:http://www.pythonware.com/products/pil/
[source]:https://github.com/towerjoo/mobile_resource_helper/blob/master/handle_resources.py
