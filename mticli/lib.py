import os
from pathlib import PurePath
import xmltodict
import sys
import json

class Themer:
    
    def __init__(self, folder_path):
        self.folder_path = os.path.realpath(folder_path)
        self.current_app = ""
        self.temp_used_packages = []

    def grab_new_app(self):
        for path, subdirs, files in os.walk(self.folder_path):
            for name in files:
                new_path = str(PurePath(path, name))
                if '.png' in new_path:
                    path_split = new_path.split('/')
                    for i in path_split:
                        if '.png' in i:
                            if i not in self.temp_used_packages:
                                self.current_app = i.replace('.png', '')
                                self.temp_used_packages.append(i)
                                return
    def set_icon(self):
        if os.path.exists('/System/Applications/{}.app'.format(self.current_app)):
            # print('bins/fileicon "/System/Applications/{}.app" "{}"'.format(self.current_app, os.path.realpath(self.folder_path + '/' + self.current_app + '.png')))
            os.system('bins/fileicon set "/System/Applications/{}.app"'.format(self.current_app))
        elif os.path.exists('/Applications/{}.app'.format(self.current_app)):
            os.system('bins/fileicon set "/Applications/{}.app"'.format(self.current_app))
        else:
            print('User Missing Application: %s' % self.current_app)
    
    def unset_icon(self):
        if os.path.exists('/System/Applications/{}.app'.format(self.current_app)):
            # print('bins/fileicon "/System/Applications/{}.app" "{}"'.format(self.current_app, os.path.realpath(self.folder_path + '/' + self.current_app + '.png')))
            os.system('bins/fileicon rm "/System/Applications/{}.app"'.format(self.current_app))
        elif os.path.exists('/Applications/{}.app'.format(self.current_app)):
            os.system('bins/fileicon rm "/Applications/{}.app"'.format(self.current_app))

                        

    def file_count(self):
        path, dirs, files = next(os.walk(self.folder_path))
        new_files = []
        for i in files:
            if '.DS_Store' not in i:
                print('Found Application: %s' % i.replace('.png', ''))
                new_files.append(i)
        return len(new_files)
    
    def check_installed(self):
        with open(self.folder_path + '/' + 'info.plist', 'r') as info:
            xml_dict = xmltodict.parse(str(info.read()))
            info.close()
        result = json.loads(json.dumps(xml_dict))
        try:
            installed = result['plist']['dict']['true']
            sys.exit(0)
        except KeyError:
            sys.exit(1)