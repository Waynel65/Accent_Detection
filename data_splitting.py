'''
    TODO: 
    reading img files from test_img2 folder
    split into three folders: english, spanish, arabic
    iterate through all files:
        if file_name contains of one of the language above:
            put file into its related folder
    ## not differentiating test and train just yet (we can do this manually I think)
'''

import glob
import os
import shutil

def extract_eng_speakers(input_file_path, output_file_path, lang):
    counter = 0
    for name in glob.glob(input_file_path + lang + '*.png'):
        counter += 1
        folder_name_length = len(input_file_path)
        # print(folder_name_length)
        img_name = name[folder_name_length:]
        shutil.move(name, output_file_path + img_name)
    
    print(counter)
    return


def main():
    input_path = 'test_img2/'
    eng_output_path = 'train_and_test_img/english/'

    extract_eng_speakers(input_path, eng_output_path,'english')
    
    return
if __name__ == "__main__":
    main()