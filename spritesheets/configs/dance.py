CONFIG = {
    "ITEM_WIDTH" : 128,   # each item's width, in px
    "ITEM_HEIGHT" : 128,  # each item's height, in px
    "SPACING" : 0,    # spacing between 2 items, in px

    "TEXTURE" : "dance1.png", # output texture's name(spritesheet's name)
    "PLIST" : "dance1.plist", # output coordinate's name
    "FILENAME_PATTERN" : "00%d.png",   # file name pattern, will be used for generate the real file name using index
    "FILENAME_LEN" : 9,   # file name length, will add "0" to the beginning of the filename if, CHECK_FILENAME_LEN is True and filename's length is less than FILENAME_LEN
    "CHECK_FILENAME_LEN" : True,   #    whether need to check the filename length 
    "start_index" : 50,  # start index, include
    "end_index" : 150,   # end index, include
}

