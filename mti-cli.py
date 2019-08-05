import argparse
import sys
import os
from mticli import Themer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""\
MTInstaller Command Line Interface Tool
---------------------------------------
This is the official version of the MTI
tool built for macthemes.co and the MTI
GUI. If you did not get this binary from
the official MTI site then it may be
malicious and contain bad code. Please
download the correct version by visiting
https://macthemes.co.""")
    parser.add_argument("-i", "--install", help="Install Theme", action="store_true")
    parser.add_argument("-u", "--uninstall", help="UnInstall Theme", action="store_true")
    parser.add_argument("-t", "--theme-bundle", help="Path To Theme Bundle")
    parser.add_argument("-c", "--check", help="Check If Theme Is Installed", action="store_true")
    parser.add_argument("-v", "--version", help="Check Version of mti-cli")
    args = parser.parse_args()
    if args.install:
        if args.uninstall:
            sys.exit('Cannot uninstall and install at same time!')
        if args.theme_bundle:
            theme_bundle = args.theme_bundle
        else:
            sys.exit('No Theme Bundle Specified!')
        theme = Themer(theme_bundle)
        file_count = theme.file_count()
        count = 0
        while count <= file_count - 1:
            theme.grab_new_app()
            theme.set_icon()
            count = count + 1
        os.system('sudo rm -rfv /Library/Caches/com.apple.iconservices.store; sudo find /private/var/folders/ \( -name com.apple.dock.iconcache -or -name com.apple.iconservices \) -exec rm -rfv {} \; >> /dev/null ; sleep 3;sudo touch /Applications/* ; killall Dock; killall Finder; echo Done')
    if args.uninstall:
        if args.install:
            sys.exit('Cannot uninstall and install at same time!')
        theme = Themer('')
        theme.uninstall()
        os.system('sudo rm -rfv /Library/Caches/com.apple.iconservices.store; sudo find /private/var/folders/ \( -name com.apple.dock.iconcache -or -name com.apple.iconservices \) -exec rm -rfv {} \; >> /dev/null ; sleep 3;sudo touch /Applications/* ; killall Dock; killall Finder; echo Done')
    if args.check:
        if args.install:
            sys.exit('Cannot Check and Install!')
        if args.uninstall:
            sys.exit('Cannot Check and Uninstall!')
        if args.theme_bundle:
            theme_bundle = args.theme_bundle
        else:
            sys.exit('No Theme Bundle Specified!')
        theme = Themer(theme_bundle)
        theme.check_installed()
        
