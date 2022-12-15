#!/usr/bin/env python
try:
    import os
    import zipfile
    import sys
    import os.path
    import time
    import datetime
    import psutil
    import random
except ImportError:
    print("Einige Module fehlen. Möchten Sie diese installieren? (y/n)")
    answer = input()
    if answer == 'y':
        import pip
        pip.main(['install', 'os'])
        pip.main(['install', 'zipfile'])
        pip.main(['install', 'sys'])
        pip.main(['install', 'os.path'])
        pip.main(['install', 'time'])
        pip.main(['install', 'datetime'])
        pip.main(['install', 'psutil'])
        pip.main(['install', 'random'])
        os.system("cls")
        print(
            "Die Module wurden erfolgreich installiert. Das Skript wird nun neu gestartet.")
        time.sleep(2)
        os.system("cls")
        os.system("python EzPiz.py")
    else:
        print("Das Skript wird beendet.")
        time.sleep(2)
        exit()
    
# ==================================================================================================
# ==================================================================================================
# ====================================== INFO TXT ==================================================
# ==================================================================================================
# ==================================================================================================
# EzPiz Menu
# By: wolFzk1nD
Version = "0.0.1 aplha"
skName = os.path.basename(__file__)

#Info text :)
info = f'''
EzPiz Menu
by wolFzk1nD
Version: {Version}

THIS IS A ALPHA VERSION, SO THERE MIGHT BE BUGS AND ERRORS
YOU HAVE TO RUN THIS WITH ADMIN RIGHTS, OR IT WILL NOT WORK

Originally created for the Raspberry Pi using Raspian OS (Debianbased)

Menu provides a simple way to manage your Pi's / Servers Files, run scripts and commands.
Inside Manager menu, you can use shortcuts to navigate through the menu.
e.X: type 'fast' instead of the index number to fast travel to a custom path.

Type X to toggle between always showing files and folders ON/OFF

Type D to toggle between showing the Designmode on ASCIIS ON/OFF

Type 0 or q to go back one step in the menu.

Manager = Manage Files and Folders
    fast            = Fast Travel to a custom path
    list            = List all files in current path
    find            = Find a file or folder by name
    create          = Create a file or folder
    read            = Read a file
    rename          = Rename a file/s or folder/s
    move            = Move a file/s or folder/s
    copy            = Copy a file/s or folder/s
    delete          = Delete a file/s or folder/s
    zip             = Zip a file/s or folder/s
    unzip           = Unzip a zipfile
    ch              = Change current path into folder in current path
    rsync           = Create a Backup of a file or folder to custom path

Scripts = Run Scripts
    Add your own paths to the script_path variable to add them into the menu.
    Add extensions if it's not in the list for extensions.
    Scripts will be always run as ROOT, due this script is run as ROOT.
    
Admin/Commands = Run Commands
    Add your own commands to the custom_cmd variable to add them into the menu.
    
Monitor Stats = Switch to a mode, that only shows the stats window and refresh every X seconds.

5. and 6. are just fpr faster access, Fast Travel and RSYNC Backup

Show all ASCII colormodes = Prints out a example for all colormodes for ASCII arts


This script is still in development and is for sure not the best code!
I am a learner, not a pro coder, so please be patient with me.
If you have improvements, feel free to let me know or share your version of the code

This project has been created for personal use, but i decided to share it with the world.

Thanks to all,
w0lFzk1nD
14/12/2022'''

# ==================================================================================================
# ==================================================================================================
# =======================================SETTINGS===================================================
# ==================================================================================================
# ==================================================================================================

#Here you will setup your paths and files.
#You can also change the look of the ascii arts and toggle the 2 options ON/OFF

# EzPiz Menu
# By: wolFzk1nD
Version = "0.0.1 aplha"
skName = os.path.basename(__file__)

global logo_mode
global title_mode
global show_mode
global show_files
# Change this to change the look of the ascii art (r: random, 1-5 randomstages, 5 highest)
# r 1 2 3 4 5 blizzard acid hacker love death raw rainbow gay circus ocean forest space romance night desert sunset neon
logo_mode = "raw"
title_mode = "hacker"
show_mode = False
show_files = False


# current path to script file
path_to_menuscript = os.path.dirname(os.path.realpath(__file__)) + skName

# Custom path for fast travel and file stuff
# Customize as you want
P_vault = "/mnt/usb1/ELEMENTS/"
P_home = "/home/pi/"
U_home = "/mnt/unraid/"
paths = ["/etc/",
         P_vault,
         P_vault + "Programming",
         P_vault + "Programming/subscripts",
         P_vault + "Programming/bckps",
         P_vault + "Programming/bckps/Bots",
         P_vault + "Programming/bckps/Projects",
         P_vault + "Programming/ghub",
         P_vault + "Programming/Programming/0Pi_Stuff/",
         P_vault + "Grail",
         P_vault + "Grail/Mount",
         P_vault + "Alpha_Shares",
         P_home,
         P_home + "Desktop",
         P_home + "backup",
         U_home,
         U_home + "Projects",
         U_home + "Bots"]

# ADMIN Custom Commands
custom_cmd = ['df -h',
              'lsblk',
              'top',
              'htop',
              'screen -AmdS void',
              'screen -r void',
              'screen -S void -X quit',
              'screen -ls',
              'nano /etc/bash.bashrc',
              'sudo mount -t cifs //192.168.191.40/Unraid /mnt/unraid -o username=wolf,password=wolfskind']

# Custom script paths
script_path = "/mnt/usb1/ELEMENTS/Programming/"
filetypes = {'sh': 'bash', 'py': 'python3', 'js': 'node'}
filenames = ['subscripts/void.sh',
             'subscripts/voidkill.sh',
             'subscripts/voidcon.sh',
             'subscripts/Pass_Gen.py',
             'subscripts/guesser.js',
             'subscripts/OKA_FILES/fischen/sort.js',
             'subscripts/OKA_FILES/Pets/average.js',
             'subscripts/mass_renamer.py',
             'subscripts/pass_gen.py',
             'subscripts/comDevShare.py',
             'subscripts/pythonlab.py',
             'ydownload.py']

# List of files to backup
vault = "/mnt/usb1/ELEMENTS/"
backup_data = [vault + "Programming/EzPiz.py",
               vault + "Programming/ydownload.py",
               vault + "Programming/subscripts/mass_renamer.py",
               vault + "Programming/bckps/Grafana/",
               vault + "Programming/subscripts/",
               ]
# Paths to backup to
destinations = ["/home/pi/backup/",
                vault + "Programming/bckps/rsync/",
                vault + "Programming/bckps/Projects/",
                '/mnt/unraid/bckup/rsync/']

# Super cool ascii arts, its recommended to minimize this, when working in the Code
asciis = {
    'logo': '''\n@@@@@@@@  @@@@@@@@  @@@@@@@   @@@  @@@@@@@@  \n@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@@@@@@  \n@@!            @@!  @@!  @@@  @@!       @@!  \n!@!           !@!   !@!  @!@  !@!      !@!   \n@!!!:!       @!!    @!@@!@!   !!@     @!!    \n!!!!!:      !!!     !!@!!!    !!!    !!!     \n!!:        !!:      !!:       !!:   !!:      \n:!:       :!:       :!:       :!:  :!:       \n :: ::::   :: ::::   ::        ::   :: ::::  \n: :: ::   : :: : :   :        :    : :: : :  \n\n  >=======[ VERSION: ''' + Version + ''' ]=======<\n''',

    'main': '''@@@@@@@@@@    @@@@@@   @@@  @@@  @@@  \n@@@@@@@@@@@  @@@@@@@@  @@@  @@@@ @@@  \n@@! @@! @@!  @@!  @@@  @@!  @@!@!@@@  \n!@! !@! !@!  !@!  @!@  !@!  !@!!@!@!  \n@!! !!@ @!@  @!@!@!@!  !!@  @!@ !!@!  \n!@!   ! !@!  !!!@!!!!  !!!  !@!  !!!  \n!!:     !!:  !!:  !!!  !!:  !!:  !!!  \n:!:     :!:  :!:  !:!  :!:  :!:  !:!  \n:::     ::   ::   :::   ::   ::   ::  \n :      :     :   : :  :    ::    :   \n ''',

    'manager': '''  @@@@@@@@@@   @@@  @@@   @@@@@@@@  @@@@@@@   \n@@@@@@@@@@@  @@@@ @@@  @@@@@@@@@  @@@@@@@@  \n@@! @@! @@!  @@!@!@@@  !@@        @@!  @@@  \n!@! !@! !@!  !@!!@!@!  !@!        !@!  @!@  \n@!! !!@ @!@  @!@ !!@!  !@! @!@!@  @!@!!@!   \n!@!   ! !@!  !@!  !!!  !!! !!@!!  !!@!@!    \n!!:     !!:  !!:  !!!  :!!   !!:  !!: :!!   \n:!:     :!:  :!:  !:!  :!:   !::  :!:  !:!  \n:::     ::    ::   ::   ::: ::::  ::   :::  \n :      :    ::    :    :: :: :    :   : :\n\n          MANAGE FILES / FODLERS''',

    'bash': '''@@@@@@@        @@@    @@@@@@   @@@  @@@  \n@@@@@@@@      @@@@   @@@@@@@   @@@  @@@  \n@@!  @@@     @@!@!   !@@       @@!  @@@  \n!@   @!@    !@!!@!   !@!       !@!  @!@  \n@!@!@!@    @!! @!!   !!@@!!    @!@!@!@!  \n!!!@!!!!  !!!  !@!    !!@!!!   !!!@!!!!  \n!!:  !!!  :!!:!:!!:       !:!  !!:  !!!  \n:!:  !:!  !:::!!:::      !:!   :!:  !:!  \n :: ::::       :::   :::: ::   ::   :::  \n:: : ::        :::   :: : :     :   : :\n\n          RUN CUSTOM SCRIPTS''',

    'admin': ''' @@@@@@   @@@@@@@   @@@@@@@@@@   @@@  @@@  @@@  \n@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@  @@@@ @@@  \n@@!  @@@  @@!  @@@  @@! @@! @@!  @@!  @@!@!@@@  \n!@!  @!@  !@!  @!@  !@! !@! !@!  !@!  !@!!@!@!  \n@!@!@!@!  @!@  !@!  @!! !!@ @!@  !!@  @!@ !!@!  \n!!!@!!!!  !@!  !!!  !@!   ! !@!  !!!  !@!  !!!  \n!!:  !!!  !!:  !!!  !!:     !!:  !!:  !!:  !!!  \n:!:  !:!  :!:  !:!  :!:     :!:  :!:  :!:  !:!  \n::   :::   :::: ::  :::     ::    ::   ::   ::  \n :   : :  :: :  :    :      :    :    ::    :\n\n          CONSOLE COMMANDS''',

    'rsync': '''@@@@@@@    @@@@@@   @@@ @@@  @@@  @@@   @@@@@@@  \n@@@@@@@@  @@@@@@@   @@@ @@@  @@@@ @@@  @@@@@@@@  \n@@!  @@@  !@@       @@! !@@  @@!@!@@@  !@@       \n!@!  @!@  !@!       !@! @!!  !@!!@!@!  !@!       \n@!@!!@!   !!@@!!     !@!@!   @!@ !!@!  !@!       \n!!@!@!     !!@!!!     @!!!   !@!  !!!  !!!       \n!!: :!!        !:!    !!:    !!:  !!!  :!!       \n:!:  !:!      !:!     :!:    :!:  !:!  :!:       \n::   :::  :::: ::      ::     ::   ::   ::: :::  \n :   : :  :: : :       :     ::    :    :: :: :\n\n          CREATE BACKUPS''',

    'find': '''@@@@@@@@  @@@  @@@  @@@  @@@@@@@   \n@@@@@@@@  @@@  @@@@ @@@  @@@@@@@@  \n@@!       @@!  @@!@!@@@  @@!  @@@  \n!@!       !@!  !@!!@!@!  !@!  @!@  \n@!!!:!    !!@  @!@ !!@!  @!@  !@!  \n!!!!!:    !!!  !@!  !!!  !@!  !!!  \n!!:       !!:  !!:  !!!  !!:  !!!  \n:!:       :!:  :!:  !:!  :!:  !:!  \n ::        ::   ::   ::   :::: ::  \n :        :    ::    :   :: :  : \n\n          FIND FILES/FOLDERS''',

    'copy': ''' @@@@@@@  @@@@@@@   @@@@@@@  @@@                   @@@@@@@  \n@@@@@@@@  @@@@@@@@  @@@@@@@  @@@                  @@@@@@@@  \n!@@       @@!  @@@    @@!    @@!          @@!     !@@       \n!@!       !@!  @!@    !@!    !@!          !@!     !@!       \n!@!       @!@!!@!     @!!    @!!       @!@!@!@!@  !@!       \n!!!       !!@!@!      !!!    !!!       !!!@!@!!!  !!!       \n:!!       !!: :!!     !!:    !!:          !!:     :!!       \n:!:       :!:  !:!    :!:     :!:         :!:     :!:       \n ::: :::  ::   :::     ::     :: ::::              ::: :::  \n :: :: :   :   : :     :     : :: : :              :: :: :\n\n          COPY FILES/FOLDERS''',

    'delete': '''@@@ @@@  @@@@@@@@  @@@@@@@@  @@@@@@@  \n@@@ @@@  @@@@@@@@  @@@@@@@@  @@@@@@@  \n@@! !@@  @@!       @@!         @@!    \n!@! @!!  !@!       !@!         !@!    \n !@!@!   @!!!:!    @!!!:!      @!!    \n  @!!!   !!!!!:    !!!!!:      !!!    \n  !!:    !!:       !!:         !!:    \n  :!:    :!:       :!:         :!:    \n   ::     :: ::::   :: ::::     ::    \n   :     : :: ::   : :: ::      :\nDELETE FILES/FOLDERS''',

    'rename': '''@@@@@@@   @@@@@@@@  @@@  @@@   @@@@@@   @@@@@@@@@@   @@@@@@@@  \n@@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  \n@@!  @@@  @@!       @@!@!@@@  @@!  @@@  @@! @@! @@!  @@!       \n!@!  @!@  !@!       !@!!@!@!  !@!  @!@  !@! !@! !@!  !@!       \n@!@!!@!   @!!!:!    @!@ !!@!  @!@!@!@!  @!! !!@ @!@  @!!!:!    \n!!@!@!    !!!!!:    !@!  !!!  !!!@!!!!  !@!   ! !@!  !!!!!:    \n!!: :!!   !!:       !!:  !!!  !!:  !!!  !!:     !!:  !!:       \n:!:  !:!  :!:       :!:  !:!  :!:  !:!  :!:     :!:  :!:       \n::   :::   :: ::::   ::   ::  ::   :::  :::     ::    :: ::::  \n :   : :  : :: ::   ::    :    :   : :   :      :    : :: ::\n\n          REANME FILE / FOLDER''',

    'move': '''@@@@@@@@@@    @@@@@@   @@@  @@@  @@@@@@@@  \n@@@@@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@@  \n@@! @@! @@!  @@!  @@@  @@!  @@@  @@!       \n!@! !@! !@!  !@!  @!@  !@!  @!@  !@!       \n@!! !!@ @!@  @!@  !@!  @!@  !@!  @!!!:!    \n!@!   ! !@!  !@!  !!!  !@!  !!!  !!!!!:    \n!!:     !!:  !!:  !!!  :!:  !!:  !!:       \n:!:     :!:  :!:  !:!   ::!!:!   :!:       \n:::     ::   ::::: ::    ::::     :: ::::  \n :      :     : :  :      :      : :: ::\n MOVE FILE / FOLDER''',

    'fasttravel': '''@@@@@@@@   @@@@@@    @@@@@@   @@@@@@@           \n@@@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@           \n@@!       @@!  @@@  !@@         @@!             \n!@!       !@!  @!@  !@!         !@!             \n@!!!:!    @!@!@!@!  !!@@!!      @!!             \n!!!!!:    !!!@!!!!   !!@!!!     !!!             \n!!:       !!:  !!!       !:!    !!:             \n:!:       :!:  !:!      !:!     :!:             \n ::       ::   :::  :::: ::      ::             \n :         :   : :  :: : :       :              \n \n         @@@@@@@  @@@@@@@   @@@  @@@  @@@       \n         @@@@@@@  @@@@@@@@  @@@  @@@  @@@       \n           @@!    @@!  @@@  @@!  @@@  @@!       \n           !@!    !@!  @!@  !@!  @!@  !@!       \n           @!!    @!@!!@!   @!@  !@!  @!!       \n           !!!    !!@!@!    !@!  !!!  !!!       \n           !!:    !!: :!!   :!:  !!:  !!:       \n           :!:    :!:  !:!   ::!!:!    :!:      \n            ::    ::   :::    ::::     :: ::::  \n            :      :   : :     :      : :: : : \n\n          FAST TRAVEL TO CUSTOM PATHS''',

    'txt': ''' @@@@@@@  @@@@@@@   @@@@@@@@   @@@@@@   @@@@@@@  @@@@@@@@  \n@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@  @@@@@@@@  \n!@@       @@!  @@@  @@!       @@!  @@@    @@!    @@!       \n!@!       !@!  @!@  !@!       !@!  @!@    !@!    !@!       \n!@!       @!@!!@!   @!!!:!    @!@!@!@!    @!!    @!!!:!    \n!!!       !!@!@!    !!!!!:    !!!@!!!!    !!!    !!!!!:    \n:!!       !!: :!!   !!:       !!:  !!!    !!:    !!:       \n:!:       :!:  !:!  :!:       :!:  !:!    :!:    :!:       \n ::: :::  ::   :::   :: ::::  ::   :::     ::     :: ::::  \n :: :: :   :   : :  : :: ::    :   : :     :     : :: ::   \n\n          CREATE FILE / FOLDER''',

    'read': '''@@@@@@@   @@@@@@@@   @@@@@@   @@@@@@@   \n@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  \n@@!  @@@  @@!       @@!  @@@  @@!  @@@  \n!@!  @!@  !@!       !@!  @!@  !@!  @!@  \n@!@!!@!   @!!!:!    @!@!@!@!  @!@  !@!  \n!!@!@!    !!!!!:    !!!@!!!!  !@!  !!!  \n!!: :!!   !!:       !!:  !!!  !!:  !!!  \n:!:  !:!  :!:       :!:  !:!  :!:  !:!  \n::   :::   :: ::::  ::   :::   :::: ::  \n :   : :  : :: ::    :   : :  :: :  :   \n\n          READ KONTEXT OF A FILE''',

    'dir': ''' @@@@@@@  @@@  @@@  @@@@@@@   @@@  @@@@@@@   \n@@@@@@@@  @@@  @@@  @@@@@@@@  @@@  @@@@@@@@  \n!@@       @@!  @@@  @@!  @@@  @@!  @@!  @@@  \n!@!       !@!  @!@  !@!  @!@  !@!  !@!  @!@  \n!@!       @!@!@!@!  @!@  !@!  !!@  @!@!!@!   \n!!!       !!!@!!!!  !@!  !!!  !!!  !!@!@!    \n:!!       !!:  !!!  !!:  !!!  !!:  !!: :!!   \n:!:       :!:  !:!  :!:  !:!  :!:  :!:  !:!  \n ::: :::  ::   :::   :::: ::   ::  ::   :::  \n :: :: :   :   : :  :: :  :   :     :   : :  \n\n          CHANGE DIRECTORY''',

    'zip': '''@@@@@@@@  @@@  @@@@@@@   \n@@@@@@@@  @@@  @@@@@@@@  \n     @@!  @@!  @@!  @@@  \n    !@!   !@!  !@!  @!@  \n   @!!    !!@  @!@@!@!   \n  !!!     !!!  !!@!!!    \n !!:      !!:  !!:       \n:!:       :!:  :!:       \n :: ::::   ::   ::       \n: :: : :  :     :        \nZIP FILES/FOLDERS''',

    'unzip': '''@@@  @@@  @@@  @@@  @@@@@@@@  @@@  @@@@@@@   \n@@@  @@@  @@@@ @@@  @@@@@@@@  @@@  @@@@@@@@  \n@@!  @@@  @@!@!@@@       @@!  @@!  @@!  @@@  \n!@!  @!@  !@!!@!@!      !@!   !@!  !@!  @!@  \n@!@  !@!  @!@ !!@!     @!!    !!@  @!@@!@!   \n!@!  !!!  !@!  !!!    !!!     !!!  !!@!!!    \n!!:  !!!  !!:  !!!   !!:      !!:  !!:       \n:!:  !:!  :!:  !:!  :!:       :!:  :!:       \n::::: ::   ::   ::   :: ::::   ::   ::       \n : :  :   ::    :   : :: : :  :     :        \n\n          UNZIP ZIPFILE''',

    'bye0': '''\n              *         *      *         *\n          ***          **********          ***\n       *****           **********           *****\n     *******           **********           *******\n   **********         ************         **********\n  ****************************************************\n ******************************************************\n********************************************************\n********************************************************\n********************************************************\n ******************************************************\n  ********      ************************      ********\n   *******       *     *********      *       *******\n     ******             *******              ******\n       *****             *****              *****\n          ***             ***              ***\n            **             *              **\n              __________\n              \______   \___.__. ____.\n               |    |  _<   |  |/ __ \.\n               |    |   \.\___  \  ___/.\n               |______  // ____|\___  >.\n                      \/ \/         \/.''',

    'bye1': '''\n       ,-""""""-.\n     /\j__/\  (  \`--.\n     \`@_@'/  _)  >--.`.\n    _{.:Y:_}_{{_,'    ) )\n   {_}`-^{_} ```     (_/\n       __________\n       \______   \___.__. ____.\n        |    |  _<   |  |/ __ \.\n        |    |   \.\___  \  ___/.\n        |______  // ____|\___  >.\n               \/ \/         \/.''',

    'bye2': '''\n@@@@@@@   @@@ @@@  @@@@@@@@  \n@@@@@@@@  @@@ @@@  @@@@@@@@  \n@@!  @@@  @@! !@@  @@!       \n!@   @!@  !@! @!!  !@!       \n@!@!@!@    !@!@!   @!!!:!    \n!!!@!!!!    @!!!   !!!!!:    \n!!:  !!!    !!:    !!:       \n:!:  !:!    :!:    :!:       \n :: ::::     ::     :: ::::  \n:: : ::      :     : :: ::   ''',

    'bye3': '''\n @@@@@@@  @@@ @@@   @@@@@@   \n@@@@@@@@  @@@ @@@  @@@@@@@@  \n!@@       @@! !@@  @@!  @@@  \n!@!       !@! @!!  !@!  @!@  \n!@!        !@!@!   @!@!@!@!  \n!!!         @!!!   !!!@!!!!  \n:!!         !!:    !!:  !!!  \n:!:         :!:    :!:  !:!  \n ::: :::     ::    ::   :::  \n :: :: :     :      :   : :''',

    'bye4': '''\n     @@!    !@@  \n      !@!  @!!   \n@!@    !@@!@!    \n!@!  @!@!@!!@!!  \n:!:    !: :!!    \n      :!:  !:!   \n:!:  :::    :::  \n ::              \n::''',

    'bye5': '''\n            \n            __,__\n   .--.  .-"     "-.  .--.\n  / .. \/  .-. .-.  \/ .. \.\n | |  '|  /   Y   \  |'  | |\n | \   \  \ 0 | 0 /  /   / |\n  \ '- ,\.-"`` ``"-./, -' /\n   `'-' /_   ^ ^   _\ '-'`\n       |  \._   _./  |\n       \   \ `~` /   /\n        '._ '-=-' _.'\n           '~---~''',

    'bye6': '''\n         ||\n         ||\n        _;|\n       /__3\n      / /||\n     / / // .--.\n     \ \// / (OO)\n      \//  |( _ )\n      // \__/`-'\__\n     // \__      _ \.\n _.-'/    | ._._.|\ \.\n(_.-'     |      \ \ \.\n   .-._   /    o ) / /\n  /_ \ \ /   \__/ / /\n    \ \_/   / /  E_/\n     \     / /\n      `-._/-' ''',

    'bye7': '''\n                _\n            ,.-" "-.,\n           /   ===   \.\n          /  =======  \.\n       __|  (o)   (0)  |__      \n      / _|    .---.    |_ \         \n     | /.----/ O O \----.\ |       \n      \/     |     |     \/        \n      |                   |            \n      |                   |           \n      |                   |          \n      _\   -.,_____,.-   /_         \n  ,.-"  "-.,_________,.-"  "-.,\n /          |       |          \  \n|           l.     .l           | \n|            |     |            |\nl.           |     |           .l             \n |           l.   .l           | \,     \n l.           |   |           .l   \,    \n  |           |   |           |      \,  \n  l.          |   |          .l        |\n   |          |   |          |         |\n   |          |---|          |         |\n   |          |   |          |         |\n   /"-.,__,.-"\   /"-.,__,.-"\"-.,_,.-"\.\n  |            \ /            |         |\n  |             |             |         |\n   \__|__|__|__/ \__|__|__|__/ \_|__|__/ ''',

    'bye8': '''\n      |\      _,,,---,,_\nZZZzz /,`.-'`'    -.  ;-;;,_\n     |,4-  ) )-,_. ,\ (  `'-'\n    '---''(_/--'  `-'\_)  ''',

    'bye9': '''\n   .       .         \n     \`-"'"-'/\n      } 6 6 {       \n     =.  Y  ,=   \n   (""-'***`-"")  \n    `-/     \-'            \n     (  )-(  )===' \n      ""   ""''',

    'bye10': '''\n                                               .--.\n                                               `.  \.\n                                                 \  \.\n                                                  .  \.\n                                                  :   .\n                                                  |    .\n                                                  |    :\n                                                  |    |\n  ..._  ___                                       |    |\n `."".`````'""--..___                              |    |\n ,-\  \             ""-...__         _____________/    |\n / ` " '                    `""""""""                  .\n \                                                      L\n (>                                                      \.\n/                                                         \.\n\_    ___..---.                                            L\n  `--'         '.                                           \.\n                 .                                           \_\n                _/`.                                           `.._\n             .'     -.                                             `.\n            /     __.-Y     /''''''-...___,...--------.._            |\n           /   _."    |    /                ' .      \   '---..._    |\n          /   /      /    /                _,. '    ,/           |   |\n          \_,'     _.'   /              /''     _,-'            _|   |\n                  '     /               `-----''               /     |\n                  `...-'                                       `...-''',

    'bye11': '''\n                  __,,,,_\n       _ __..-;''`--/'/ /.',-`-.\n   (`/' ` |  \ \ \\ / / / / .-'/`,_\n  /'`\ \   |  \ | \| // // / -.,/_,'-,\n /<7' ;  \ \  | ; ||/ /| | \/    |`-/,/-.,_,/')\n/  _.-, `,-\,__|  _-| / \ \/|_/  |    '-/.;.\'\n`-`  f/ ;      / __/ \__ `/ |__/ |\n     `-'      |  -| =|\_  \  |-' |\n           __/   /_..-' `  ),'  //\n       fL ((__.-'((___..-'' \__.''',

    'bye12': '''\n _\n( \.\n \ \.\n / /                |\\.\n/ /     .-`````-.   / ^`-.\n\ \    /         \_/  {|} `o\n \ \  /   .---.   \\ _  ,--'\n  \ \/   /     \,  \( `^^^\n   \   \/\      (\  )\n    \   ) \     ) \ \.\n     ) /__ \__  ) (\ \___\n    (___)))__))(__))(__)))''',

    'bye13': '''\n           .'\   /`.\n         .'.-.`-'.-.`.\n    ..._:   .-. .-.   :_...\n  .'    '-.(o ) (o ).-'    `.\n :  _    _ _`~(_)~`_ _    _  :\n:  /:   ' .-=_   _=-. `   ;\  :\n:   :|-.._  '     `  _..-|:   :\n :   `:| |`:-:-.-:-:'| |:'   :\n  `.   `.| | | | | | |.'   .'\n    `.   `-:_| | |_:-'   .'\n      `-._   ````    _.-'\n          ``-------''''',

    'bye14': '''\n                        _\n                       | \.\n                       | |\n                       | |\n  |\                   | |\n /, ~\                / /\nX     `-.....-------./ /\n ~-. ~  ~              |\n    \             /    |\n     \  /_     ___\   /\n     | /\ ~~~~~   \ |\n     | | \        || |\n     | |\ \       || )\n    (_/ (_/      ((_/''',

    'bye15': '''\n                                               ,w.\n                                             ,YWMMw  ,M  ,\n                        _.---.._   __..---._.'MMMMMw,wMWmW,\n                   _.-""        """           YP"WMMMMMMMMMb,\n                .-' __.'                   .'     MMMMW^WMMMM;\n    _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;\n ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\.\n,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,\nWMMm__,-'.'     /      _.\      F"""-+,,   ;_,_.dMMMMMMMM[,_ / `=_}\n"^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|\n           /   .'            ; ;         )  )`{  \ `"^W^`,   \  :\n          /  .'             /  (       .'  /     Ww._     `.  `"\n         /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,\n        (--, )                `,_ / `) \/"")      ^"      `-, -;"\:\n         `"""                    `"""   `"'                  `---"''',

    'bye16': '''\n ._       __          ____\n;  `\--,-' /`)    _.-'    `-._\n \_/    ' | /`--,'            `-.     .--....____\n  /                              `._.'           `---...\n  |-.   _      ;                        .-----..._______)\n,,\q/ (q_>'_...                      .-'\n===/ ; _.-'~~-             /       ,'\n`""`-'_,;  `""         ___(       |\n         \         ; /'/   \      \.\n          `.      //' (    ;`\    `\.\n          / \    ;     `-  /  `-.  /\n         (  (;   ;     (__/    /  /\n          \,_)\  ;           ,'  /\n  .-.          |  |           `--'\n ("_.)-._     (__,> ''',

    'bye17': '''\n-  -   -     -   -   --   -    -     - -   -  _  -    -  -      -  - -  -  -  -\n=-   - =- = - =  -  =- =   _.----~~~~~~-----..__ =   =-   -=-  - = =  -=--  = -\n=#-=  =-# - == ##= -__..------~~~~-     .._     ~~-. #== -#- = =-  ##=-= =#- -\n#===#==___.--.--~~~~     --~~~~---~ __  ~~----.__   ~~~~~~~---...._____#== =##=\n##(~~~~_..----~       ~~--=< O >- .----. -< O >=--~~             ..   .)#=#=##=\n###~-..__..--         ..  ___-----_...__-----___        _.  ~-=___..-~#########\n##==#===#==`   _    ..   (     " :_.}{._; " "   )      _-     '==#=##=====#=#==\n=#-==-== =# \   ~~-      `   " " __###__  ""    '    -~     .'==-=#===#- -=- #=\n-= == -=  -= `-._  ~-.    _`--~~~VvvvvVV~~---'_     ~..    _. #= =  =  ==# - ==\n = -==  - = - == -.     `~##\(            )/###~' .     _.~    -=- = -= -=- -\n= -  -= -   - -    -    `.###\#    {     #/####.'    _-~  - =  - - -  -    = -\n -    -       -  -  -_    -####    !     #####-  ..    -    -       -   -   - -\n                      -._  ~.###   }     ###-~ ___.-~\n                         ~-  \##  / "   ##.~ /~                      \n                           \ |###  "   ###' /   \n                            \`/\#######/\' ;                               \n                             ~-.^^^^^^^ .-~                                    \n                                ~~~~~~~~''',

    'bye17': '''\n ,\/~~~\_                            _/~~~~\.\n |  ---, `\_    ___,-------~~\__  /~' ,,''  |\n | `~`, ',,\`-~~--_____    ---  - /, ,--/ '/'\n  `\_|\ _\`    ______,---~~~\  ,_   '\_/' /'\n    \,_|   , '~,/'~   /~\ ,_  `\_\ \_  \_\'\n    ,/   /' ,/' _,-'~~  `\  ~~\_ ,_  `\  `\.\n  /@@ _/  /' ./',-                 \       `@,\n  @@ '   |  ___/  /'  /  \  \ '\__ _`~|, `, @@\n/@@ /  | | ',___  |  |    `  | ,,---,  |  | `@@,\n@@@ \  | | \ \O_`\ |        / / O_/' | \  \  @@@\n@@@ |  | `| '   ~ / ,          ~     /  |    @@@\n`@@ |   \ `\     ` |         | |  _/'  /'  | @@'\n @@ |    ~\ /--'~  |       , |  \__   |    | |@@\n @@, \     | ,,|   |       ,,|   | `\     /',@@\n `@@, ~\   \ '     |       / /    `' '   / ,@@\n  @@@,    \    ~~\ `\/~---'~/' _ /'~~~~~~~~--,_\n   `@@@_,---::::::=  `-,| ,~  _=:::::``````    `\n   ,/~~_---'_,-___     _-__  ' -~~~\_```---\n     ~`   ~~_/'// _,--~\_/ '~--, |\_\n          /' /'| `@@@@@,,,,,@@@@  | \      -Chev\n               `     `@@@@@@''',

    'bye17': '''\n               ....                          .... \n              ..x....                      ....x.. \n             ..xx......     ........     ......xx.. \n            ..xxxx...,,. .............. .,,...xxxx.. \n            ..xxxxx,,,,..................,,,,xxxxx.. \n             .,,,,..,,...................,,..,,,,,. \n           ........ ,,,.................,,, ......... \n         ....... .(((,,,...............,,,))). ........ \n        ..... ..,,a@@@@a,,...........,,a@@@@a,,.. ...... \n       .......,,a@@`  '@@,...........,@@`  '@@a,,........ \n       .......,,@@@    @@@,.a@@@@@a.,@@@    @@@,,........ \n       ....,,,,,,@@@aa@@@,,,,`@@@',,,,@@@aa@@@,,,,,,,.... \n        ...,,,,,,,,,,,,,,,,,,,,|,,,,,,,,,,,,,,,,,,,,,... \n          ...,,,,,,,,,,,,,,,,`   ',,,,,,,,,,,,,,,,,... \n              .. ,,,,,,,,,,,,,...,,,,,,,,,,,,,, .. \n      (     ......... ,,,,,,,,,,,,,,,,,,, ........... \n   (   )  .............._ _ _ _ _ _ _ _................   ( \n    )  ( ...............................................   ) \n   (   ) ...............................................  (  ) \n    ) ( ,,,,,,,,,,,,,,, ................. ,,,,,,,,,,,,,,,, ) ( \n ,%%%%,,,,,,,,,,,,,,,,,, ............... ,,,,,,,,,,,,,,,,,,%%%%, \n %%%%%`.,,(,,(,,(,,(,,'%%%%%%%%%%%%%%%%%%`,,,),,),,),,),,.'%%%%% \n `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%' \n    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n    ::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::::: \n   ::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::::: \n  ::::::;;%%;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::::: \n ::::::;;%%;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;%%:::::: \n::::::;;%%%;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;%%:::::: \n::::::;;%%%;;;;A;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;%%%::::: \n::::::;;;%%;;;;;AA;;;;;;;;;;;;;;;;;;;;A;;;;;;;;;;;;;;;;;;%%%::::: \n::::::;;;;%%;;;;;AAA;;;;;;;;;;;;;;;;AA;;;;;;;;;;;;A;;;;;;%%:::::: \n::::::;;A;;;;;;;;;AAA;;;;;;;;;A;;;;AAA;;;;;;;;;;;;;AA;;;%%;:::::: \n ::::::;AA;;;;;;;;;AAA;;;;;;;A;;;;;AAAA;;;;;A;;;;;;AAA;;;;:::::: \n  ::::::;AAA;;;;;;;AAA;;A;;;AA;;;;;;AAAA;;;;AA;;;;;AAA;;;:::::: \n    :::::;AAA;;;;;AAA;;AA;;;AAA;;;;;;AAAA;;AAA;;;;AAAA;;::::: \n       :::;AAAA;;AAAA;;AAA;;;AAA;;;;AAAAA;AAA;;;;AAAAAA::: \n          ::AAAAAAAA;;;;AAA;AAAAA;;AAAAA;;;AAA;;AAAAAAA \n            .::::::                           ::::::. \n           :::::::'                           `:::::::''',

    'bye17': '''\n              _,.\n           ,''   `.     __....__ \n         ,'        >.-''        ``-.__,)\n       ,'      _,''           _____ _,'\n      /      ,'           _.:':::_`:-._ \n     :     ,'       _..-''  \`'.;.`-:::`:. \n     ;    /       ,'  ,::'  .\,'`.`. `\::)`  \n    /    /      ,'        \   `. '  )  )/ \n   /    /      /:`.     `--`'   \     '`\n   `-._/      /::::)             )\n      /      /,-.:(   , _   `.-' \n     ;      :(,`.`-' ',`.     ;\n    :       |:\`' )      `-.._\ _\n    |         `:-(             `)``-._ \n    |           `.`.        /``'      ``:-.-__,\n    :           / `:\ .     :            ` \`-\n     \        ,'   '}  `.   |\n  _..-`.    ,'`-.   }   |`-'    \n,'__    `-'' -.`.'._|   | \n    ```--..,.__.(_|.|   |::._\n      __..','/ ,' :  `-.|::)_`.\n      `..__..-'   |`.      __,' \n                  :  `-._ `  ;\n                   \ \   )  /\n                   .\ `.   /\n                    ::    /\n                    :|  ,'\n                    :;,' SSt\n                    `''',
}

                                              

# Colortable for the rainbow function
colors = ['\033[31m', "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m", "\033[91m", "\033[92m",
          "\033[93m", "\033[94m", "\033[95m", "\033[96m", '\033[35m', "\033[95m", "\033[97m", "\033[90m", "\033[38;5;208m"]
red, green, yellow, blue, magenta, cyan, lred, lgreen, lyellow, lblue, lmagenta, lcyan, magenta, lmagenta, white, gray, orange = colors
# ColorVariations
blizzard = [lblue, lcyan, white]
acid = [lcyan, lgreen, lyellow]
hacker = [green, lgreen, gray]
love = [red, lred, magenta, lmagenta, white]
death = [red, lred, gray, lgreen]
circus = ['\033[31m', "\033[91m", "\033[93m", "\033[94m"]
gay = [lmagenta, white, lblue]
jamaika = [red, green, yellow]
ocean = [blue, cyan, white]
forest = [green, lgreen, red]
space = [gray, lyellow, white]
romance = [lred, magenta, lmagenta, green, gray, lyellow]
night = [gray, white]
desert = [yellow, lyellow, green]
rainbow = [red, lred, green, lgreen, blue, lblue, magenta]
sunset = [red, lred, orange, yellow, lyellow]
sunrise = [orange, yellow, lyellow, lgreen, blue]
neon = [lgreen, lblue, lmagenta, lyellow]
modes = [1, 2, 3, 4, 5, 'blizzard', 'acid', 'hacker', 'love', 'death', 'raw', 'gay', 'circus',
         'jamaika', 'ocean', 'forest', 'space', 'romance', 'night', 'desert', 'rainbow', 'sunset', 'neon']
bye_ascii = ['bye0', 'bye1', 'bye2', 'bye3',
             'bye4', 'bye5', 'bye6', 'bye7', 'bye8', 'bye9', 'bye10', 'bye11', 'bye12', 'bye13', 'bye14', 'bye15', 'bye16', 'bye17']


# ==================================================================================================
# ==================================================================================================
# =======================================FUNCTIONS==================================================
# ==================================================================================================
# ==================================================================================================


def format_size(size): # Filesize formater
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0: '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    if n == 0 and size > 0:
        return f"{round(size,2)}B"
    elif n == 0 and size == 0:
        return 'FOLDER'
    else:
        return f"{round(size,2)}{power_labels[n]}B"


def signal_handler(log): # For clean exit
    if log:
        rand = random.randint(0, len(bye_ascii) - 1)
        print_ascii(bye_ascii[rand], "r")
    sys.exit(0)


def rainbow_ascii(ascii_text, mode): # Make colorfull text
    if mode == "r":
        mode = modes[int(random.random() * len(modes))]
    ascii_lines = ascii_text.split('\n')
    formatted_lines = []
    for line in ascii_lines:
        formatted_chars = []
        for char in line:
            if mode == 1:
                formatted_chars.append(colors[int(
                    random.random() * len(colors) / 4)] + char + "\033[0m")
            elif mode == 2:
                formatted_chars.append(colors[int(
                    random.random() * len(colors) / 3)] + char + "\033[0m")
            elif mode == 3:
                formatted_chars.append(colors[int(
                    random.random() * len(colors) / 2.5)] + char + "\033[0m")
            elif mode == 4:
                formatted_chars.append(colors[int(
                    random.random() * len(colors) / 1.5)] + char + "\033[0m")
            elif mode == 5:
                formatted_chars.append(colors[int(
                    random.random() * len(colors))] + char + "\033[0m")
            elif mode == 'blizzard':
                formatted_chars.append(blizzard[int(
                    random.random() * len(blizzard))] + char + "\033[0m")
            elif mode == 'acid':
                formatted_chars.append(acid[int(
                    random.random() * len(acid))] + char + "\033[0m")
            elif mode == 'hacker':
                formatted_chars.append(hacker[int(
                    random.random() * len(hacker))] + char + "\033[0m")
            elif mode == 'love':
                formatted_chars.append(love[int(
                    random.random() * len(love))] + char + "\033[0m")
            elif mode == 'death':
                formatted_chars.append(death[int(
                    random.random() * len(death))] + char + "\033[0m")
            elif mode == 'jamaika':
                formatted_chars.append(jamaika[int(
                    random.random() * len(jamaika))] + char + "\033[0m")
            elif mode == 'gay':
                formatted_chars.append(gay[int(
                    random.random() * len(gay))] + char + "\033[0m")
            elif mode == 'circus':
                formatted_chars.append(circus[int(
                    random.random() * len(circus))] + char + "\033[0m")
            elif mode == 'ocean':
                formatted_chars.append(ocean[int(
                    random.random() * len(ocean))] + char + "\033[0m")
            elif mode == 'forest':
                formatted_chars.append(forest[int(
                    random.random() * len(forest))] + char + "\033[0m")
            elif mode == 'space':
                formatted_chars.append(space[int(
                    random.random() * len(space))] + char + "\033[0m")
            elif mode == 'romance':
                formatted_chars.append(romance[int(
                    random.random() * len(romance))] + char + "\033[0m")
            elif mode == 'night':
                formatted_chars.append(night[int(
                    random.random() * len(night))] + char + "\033[0m")
            elif mode == 'desert':
                formatted_chars.append(desert[int(
                    random.random() * len(desert))] + char + "\033[0m")
            elif mode == 'rainbow':
                formatted_chars.append(rainbow[int(
                    random.random() * len(rainbow))] + char + "\033[0m")
            elif mode == 'sunset':
                formatted_chars.append(sunset[int(
                    random.random() * len(sunset))] + char + "\033[0m")
            elif mode == 'sunrise':
                formatted_chars.append(sunrise[int(
                    random.random() * len(sunrise))] + char + "\033[0m")
            elif mode == 'neon':
                formatted_chars.append(neon[int(
                    random.random() * len(neon))] + char + "\033[0m")
            elif mode == 'raw':
                color1 = random.choice(colors)
                color2 = random.choice(colors)
                count = 0
                for char in line:
                    if char.isalpha():
                        if color1 == color2:
                            color2 = random.choice(colors)
                        formatted_chars.append(color1 + char)
                        color1, color2 = color2, color1
                    else:
                        if count == 0:
                            formatted_chars.append(color1 + char + "\033[0m")
                            count += 1
                        elif count == 1:
                            formatted_chars.append(color2 + char + "\033[0m")
                            count -= 1
                break
        formatted_lines.append(''.join(formatted_chars))
    if show_mode:
        formatted_lines.append("  Mode: " + str(mode))
    return '\n'.join(formatted_lines)


def print_ascii(ascii_name, mod): # print colorfull ascii
    print(rainbow_ascii(asciis[ascii_name], mod))


def ascii_color_show(): # Make a colorfull show of all modes
    the_show = '''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''

    print(rainbow_ascii("Welcome to the Color Show", "r"))
    print(rainbow_ascii('╔═══════════════════════════════════════════════╗', "hacker"))
    for modez in modes:
        print(rainbow_ascii(the_show, modez))
    print(rainbow_ascii('╚═══════════════════════════════════════════════╝', "hacker"))
    print(rainbow_ascii("The END", "r"))
    input("Press Enter to continue...")


def fast_travel(): # Fast Travel to custom Paths [Done code/ No color]
    os.system('clear')
    print_ascii('fasttravel', title_mode)
    list_current()
    list_custom()
    while True:
        choice = input('Destination (0 or q to quit): ')
        if choice == '0' or choice.lower() == 'q':
            break
        elif choice.isdigit() == False:
            print('Invalid Input!')
            continue
        elif choice == str(len(paths) + 1):
            path = input('Your wished Destination: (0 or q to quit)')
            if path.lower() == 'q' or path == '0':
                print('Aborted.')
                break
            os.chdir(path)
            break
        elif int(choice) >= 1 and int(choice) <= len(paths):
            os.chdir(paths[int(choice) - 1])
            break
        else:
            print('Invalid Destination')


def list_files(): # List all Files in current Directory [Done code/ No color]
    files = os.listdir()
    print('\nFiles in working directory:')
    print(os.getcwd())
    print('╔═══════════════════════════════════════════════╗')
    max_length = 0
    for i, file in enumerate(files):
        if os.path.isfile(file):
            if len(file) > max_length:
                max_length = len(file)
    for i, file in enumerate(files):
        if os.path.isfile(file):
            size = os.path.getsize(file)
            size = format_size(size)
            permissions = os.stat(file).st_mode
            if len(file) > 40:
                print("║ " + str(i+1).rjust(2) + ". " + file + "    [ " + size.rjust(
                    7) + " ] [ " + str(oct(permissions)[-3:]).rjust(3) + " ]")
            else:
                print("║ " + str(i+1).rjust(2) + ". " + file.ljust(41) +
                      " [ " + size.rjust(7) + " ] [ " + str(oct(permissions)[-3:]).rjust(3) + " ]")
        else:
            file_count = len(os.listdir(file))
            print("║ " + str(i+1).rjust(2) + ". " + file.ljust(41) +
                  " ( FOLDER  ) [ x" + str(file_count).rjust(3) + " Files ]")
    print('╚═══════════════════════════════════════════════╝')


def find_file(): # Find a filename in specified Path [Done code/ No color]
    os.system('clear')
    print_ascii('logo', logo_mode)
    print_ascii('find', title_mode)
    list_current()
    paths = ["/", "/home/pi", "/etc", "/boot", "/mnt/usb1/ELEMENTS"]
    while True:
        filename = input('\nEnter a filename (0 or q to quit): ')
        if filename.lower() == 'q' or filename == '0':
            print('Aborted.')
            break
        print(
            '\n╔═════════════════════════════════════════════════════════════════════════╗')
        for i in range(len(paths)):
            print("║ " + str(i+1).rjust(2) + ": " + paths[i])
        print("║ " + str(len(paths)+1) + ": Enter a custom path")
        print('╚═════════════════════════════════════════════════════════════════════════╝')
        path_choice = input("\nChoose a path to search (0 or q to quit): ")
        if path_choice == "0" or path_choice == "q":
            break
        elif int(path_choice) > len(paths):
            custom_path = input("Enter a custom path: ")
            print('\nSearching for Files...\n╔═════════════════════════════════════════════════════════════════════════╗')
            os.system('find ' + custom_path + ' -name ' + filename)
            print(
                '╚═════════════════════════════════════════════════════════════════════════╝')
            break
        else:
            print('\nSearching for Files...\n╔═════════════════════════════════════════════════════════════════════════╗')
            os.system(
                'find ' + paths[int(path_choice)-1] + ' -name ' + filename)
            print(
                '╚═════════════════════════════════════════════════════════════════════════╝')
            break
    input('Press enter to continue...')


def create(): # Create a new File or Folder [Done code/ No color]
    os.system('clear')
    print_ascii('logo', logo_mode)
    print_ascii('txt', title_mode)
    list_current()
    list_files()
    filename = ''
    while True:
        choice = input(
            'Do you want to create a folDer or a File? (f/d) (0 or q to quit): ')
        if choice == 'f':
            filename = input(
                'Enter an existing or new filename (0 or q to quit): ')
            if filename.lower() == 'q' or filename == '0':
                print('Aborted.')
                break
            if os.path.exists(filename):
                overwrite = input(
                    'File already exists. Do you want to overwrite? (y/n) ')
                if overwrite == 'y':
                    os.system('nano ' + filename)
                    break
                elif overwrite == 'n':
                    pass
            else:
                os.system('nano ' + filename)
                break
        elif choice == 'd':
            foldername = input(
                'Enter a foldername (0 or q to quit): ')
            if foldername.lower() == 'q' or foldername == '0':
                print('Aborted.')
                break
            if os.path.exists(foldername):
                overwrite = input(
                    'Folder already exists. Do you want to overwrite and rename it? (y/n) ')
                if overwrite == 'y':
                    os.system('rm -r ' + foldername)
                    os.system('mkdir ' + foldername)
                    break
                elif overwrite == 'n':
                    pass
            else:
                os.system('mkdir ' + foldername)
                break
        elif choice.lower() == 'q' or choice == '0':
            print('Aborted.')
            break
    input('Press enter to continue...')


def read_file_out(): # Read a File out [Done code/ No color]
    os.system('clear')
    print_ascii('logo', logo_mode)
    print_ascii('read', title_mode)
    list_current()
    list_files()
    while True:
        filename = input(
            'Enter an existing or new filename (0 or q to quit): ')
        if filename.lower() == 'q' or filename == '0':
            print('Aborted.')
            break
        elif filename.isdigit() == False:
            print('Invalid Input!')
            continue
        else:
            file_name = os.listdir(os.getcwd())[int(filename)]
            file_size = os.path.getsize(file_name)
            file_size_formatted = format_size(file_size)
            print(
                f'\n╔═════════════════════════════════════════════════════════════════════════╗\n    Name: {file_name}\n    Size: {file_size_formatted}\n╠════════════════════════════════════════╣')
            text = os.system('cat ' + file_name)
            print(str(text).replace('$', ''))
            input('\n╚═════════════════════════════════════════════════════════════════════════╝\nPress enter to continue...')
            break


def rename_file(): # Rename a File or Folder [Done code/ No color]
    os.system('clear')
    print_ascii('logo', logo_mode)
    print_ascii('rename', title_mode)
    list_current()
    files = os.listdir()
    print('Files in working directory: ')
    print('\n╔═════════════════════════════════════════════════════════════════════════╗')
    for i, file in enumerate(files):
        size = os.path.getsize(file)
        size_formatted = format_size(size)
        permissions = os.stat(file).st_mode
        if os.path.isdir(file):
            file_count = len(os.listdir(file))
            print("║ " + str(i+1).rjust(2) + ". " + file.ljust(41) +
                  " ( FOLDER  ) [ x" + str(file_count).rjust(3) + " Files ]")
        else:
            if len(file) > 40:
                print("║ " + str(i+1).rjust(2) + ". " + file + "    [ " + size_formatted.rjust(
                    7) + " ] [ " + str(oct(permissions)[-3:]).rjust(3) + " ]")
            else:
                print("║ " + str(i+1).rjust(2) + ". " + file.ljust(41) + " [ " + size_formatted.rjust(
                    7) + " ] [ " + str(oct(permissions)[-3:]).rjust(3) + " ]")
    print('╚═════════════════════════════════════════════════════════════════════════╝')
    while True:
        try:
            file_index = input('Enter a file number (0 or q to quit): ')
            if file_index == 0 or file_index.lower() == 'q':
                break
            elif file_index.isdigit() == False:
                print('Invalid Input!')
                continue
            else:
                print("═══════════════════════════════════════")
                filename = files[int(file_index) - 1]
                new_filename = input('Enter a NEW filename (0 or q to quit): ')
                if new_filename.lower() == 'q' or new_filename == '0':
                    print('Aborted.')
                    break
            os.rename(filename, new_filename)
        except FileNotFoundError:
            print('The specified file was not found.')
            input('Press enter to continue...')
            break
        except IndexError:
            print('The specified file number was not found.')
            input('Press enter to continue...')
            break
        else:
            print(
                f'File renamed successfully, from: \n   {filename}\nto:  {new_filename}.')
            input('Press enter to continue...')
            break


def move_file(): # Move a File or Folder [Done code/ No color]
    os.system('clear')
    print_ascii('logo', logo_mode)
    print_ascii('move', title_mode)
    list_current()
    folder_files = os.listdir()
    print('Files in working directory:')
    print('\n╔═════════════════════════════════════════════════════════════════════════╗')
    file_list = []
    for i, file in enumerate(folder_files):
        size = os.path.getsize(file)
        size_formatted = format_size(size)
        permissions = os.stat(file).st_mode
        file_list.append(file)
        if os.path.isdir(file):
            file_count = len(os.listdir(file))
            print("║ " + str(i+1).rjust(2) + ". " + file.ljust(41) +
                  " ( FOLDER  ) [ x" + str(file_count).rjust(3) + " Files ]")
        else:
            if len(file) > 41:
                print("║ " + str(i+1).rjust(2) + ". " + file + "    [ " + size_formatted.rjust(
                    7) + " ] [ " + str(oct(permissions)[-3:]).rjust(3) + " ]")
            else:
                print("║ " + str(i+1).rjust(2) + ". " + file.ljust(41) + " [ " + size_formatted.rjust(
                    7) + " ] [ " + str(oct(permissions)[-3:]).rjust(3) + " ]")
    print('╚═════════════════════════════════════════════════════════════════════════╝')
    while True:
        filename = input(
            'Enter the fileindex to move (separated by commas, 0 or q to quit): ')
        if filename.lower() == 'q' or filename == '0':
            print('Aborted.')
            break

        filenames = filename.split(',')
        for i in range(len(filenames)):
            if filenames[i].isdigit() == False:
                print('\nInvalid Input!')
                filenames.remove(filenames[i])
            else:
                filenames[i] = int(filenames[i]) - 1
        for filename in filenames:
            if int(filename) > len(folder_files):
                print('\nInvalid Input!  File not found.', int(filename)+1)
                filenames.remove(filenames[filenames.index(filename)])
                break
        list_custom()
        while True:
            choice = input('Option: ')
            if choice == '0' or choice.lower() == 'q':
                print('Aborted.')
                break
            elif choice.isdigit() == False:
                print('Invalid Input!')
                continue
            elif choice == str(len(paths) + 1):
                path = input('Own Path: ')
                if not os.path.exists(path):
                    mv_create = input(
                        'Path does not exist. Would you like to create it? (Y/N)')
                    if mv_create == 'Y' or mv_create == 'y':
                        os.makedirs(path)
                        for filename in filenames:
                            os.system('mv ' +
                                      folder_files[int(filename)] + ' ' + path)
                        print('Files moved successfully to ' + path)
                    else:
                        print("Aboarding, no folder created.")
                        continue
                else:
                    for filename in filenames:
                        print(folder_files[int(filename)])
                        os.system('mv ' +
                                  folder_files[int(filename)] + ' ' + path)
                    print('Files moved successfully to ' + path)
                break
            elif int(choice)-1 >= 0 and int(choice)-1 <= len(paths):
                for filename in filenames:
                    print(folder_files[int(filename)])
                    os.system(
                        'mv ' + folder_files[int(filename)] + ' ' + paths[int(choice) - 1])
                print('Files moved successfully to ' + paths[int(choice) - 1])
                break
            else:
                print('Invalid Option.')
                continue
        input('Press enter to continue...')
        break


def copy_file(): # Copy a File or Folder [Done code/ No color]
    os.system('clear')
    print_ascii('logo',    logo_mode)
    print_ascii('copy',   title_mode)
    list_current()
    folder_files = []
    for file in os.listdir():
        folder_files.append(file)
    print('Files in working directory:')
    print('\n╔═════════════════════════════════════════════════════════════════════════╗')
    for i, file in enumerate(folder_files):
        size = os.path.getsize(file)
        size_formatted = format_size(size)
        permissions = os.stat(file).st_mode
        if os.path.isdir(file):
            file_count = len(os.listdir(file))
            print("║ " + str(i+1).rjust(2) + ". " + file.ljust(41) +
                  " ( FOLDER  ) [ x" + str(file_count).rjust(3) + " Files ]")
        else:
            if len(file) > 40:
                print("║ " + str(i+1).rjust(2) + ". " + file + "    [ " + size_formatted.rjust(
                    7) + " ] [ " + str(oct(permissions)[-3:]).rjust(3) + " ]")
            else:
                print("║ " + str(i+1).rjust(2) + ". " + file.ljust(41) + " [ " + size_formatted.rjust(
                    7) + " ] [ " + str(oct(permissions)[-3:]).rjust(3) + " ]")
    print('╚═════════════════════════════════════════════════════════════════════════╝')
    while True:
        filename = input(
            'Enter a fileindex to copy (seperate with comma 1,2,3) (0 or q to quit): ')
        filenames = filename.split(',')
        if filename.lower() == 'q' or filename == '0':
            print('Aborted.')
            break
        for i in range(len(filenames)):
            if filenames[i].isdigit() == False:
                print('Invalid Input! ' + filenames[i])
                filenames.remove(filenames[i])
                continue
            else:
                filenames[i] = int(filenames[i]) - 1
        else:
            list_custom()
            while True:
                choice = input('Option: ')
                if choice == '0' or choice.lower() == 'q':
                    print('Aborted.')
                    break
                elif choice.isdigit() == False:
                    print('Invalid Input!')
                    continue
                elif choice == str(len(paths) + 1):
                    path = input('Own Path: ')
                    if not os.path.exists(path):
                        mv_create = input(
                            'Path does not exist. Would you like to create it? (Y/N)')
                        if mv_create == 'Y' or mv_create == 'y':
                            os.makedirs(path)
                            for filename in filenames:
                                print(folder_files[filename])
                                is_directory = os.path.isdir(
                                    folder_files[filename])
                                folderdd = "-r " if is_directory else ""
                                os.system('cp ' + folderdd +
                                          folder_files[filename] + ' ' + path)
                            print('File copied successfully to: ' +
                                  path)
                            break
                        else:
                            print("Aboarding, no folder created.")
                            continue
                    else:
                        for filename in filenames:
                            is_directory = os.path.isdir(
                                folder_files[filename])
                            folderdd = "-r " if is_directory else ""
                            print(folder_files[filename])
                            os.system('cp ' + folderdd +
                                      folder_files[filename] + ' ' + path)
                        print('File copied successfully to: ' +
                              path)
                        break
                elif int(choice) >= 1 and int(choice) <= len(paths):
                    for filename in filenames:
                        print(folder_files[filename])
                        is_directory = os.path.isdir(folder_files[filename])
                        folderdd = "-r " if is_directory else ""
                        os.system('cp ' + folderdd +
                                  folder_files[filename] + ' ' + paths[int(choice) - 1])
                    print('File copied successfully to: ' +
                          paths[int(choice) - 1])
                    break
            input('Press enter to continue...')
            break


def delete_file(): # Delete a File or Folder [Done code/ No color]
    os.system('clear')
    print_ascii('logo',   logo_mode)
    print_ascii('delete', title_mode)
    list_current()
    list_files = []
    files = os.listdir()
    for file in files:
        list_files.append(file)
    print('Files in working directory:')
    print('\n╔═════════════════════════════════════════════════════════════════════════╗')
    for i, file in enumerate(list_files):
        size = os.path.getsize(file)
        size_formatted = format_size(size)
        permissions = os.stat(file).st_mode
        if os.path.isdir(file):
            file_count = len(os.listdir(file))
            print("║ " + str(i+1).rjust(2) + ". " + file.ljust(41) +
                  " ( FOLDER  ) [ x" + str(file_count).rjust(3) + " Files ]")
        else:
            if len(file) > 40:
                print("║ " + str(i+1).rjust(2) + ". " + file + "    [ " + size_formatted.rjust(
                    7) + " ] [ " + str(oct(permissions)[-3:]).rjust(3) + " ]")
            else:
                print("║ " + str(i+1).rjust(2) + ". " + file.ljust(41) + " [ " + size_formatted.rjust(
                    7) + " ] [ " + str(oct(permissions)[-3:]).rjust(3) + " ]")
    print('╚═════════════════════════════════════════════════════════════════════════╝')
    file_numbers = []
    file_number = input(
        'Enter files number (separated by comma) (0 or q to quit): ')
    file_split = file_number.split(',')
    while True:
        if file_number.lower() == 'q' or file_number == '0':
            print('Aborted.')
            return

        for split_file in file_split:
            try:
                file_numbers.append(int(split_file) - 1)
            except ValueError:
                print('Invalid file number. Aboard,')
                input('Press enter to continue...')
                return
        break
    print(" ")
    for del_index in file_split:
        del_inx = int(del_index)-1
        if not os.path.isfile(list_files[del_inx]) and not os.path.isdir(list_files[del_inx]):
            print('Error: This file does not exist.')
            continue
        if os.path.isdir(list_files[del_inx]):
            folderdd = "-r "
        else:
            folderdd = ""
        os.system('rm ' + folderdd + list_files[del_inx])
        print('File deleted successfully file: ' +
              list_files[del_inx])
    input('\n       Done deleting\n\nPress enter to continue...')


def zip_file(): # Create a ZIP File [Done code/ No color]
    os.system('clear')
    print_ascii('logo', logo_mode)
    print_ascii('zip',  title_mode)
    list_current()
    files_in_directory = []
    for file in os.listdir():
        files_in_directory.append(file)
    if not files_in_directory:
        print('No files in working directory.')
        input('Press enter to continue...')
        return
    while True:
        zip_filename = input(
            '\n\nEnter a ZIP-fileNAME (without .zip) (0 or q to quit): ') + '.zip'
        if zip_filename.lower() == 'q' or zip_filename == '0':
            print('Aborted.')
            break
        list_files()
        file_indexes = input(
            'Enter the indexes of the files to add to ZIP-file (separated1,2,3) (0 or q to quit): ')
        if file_indexes.lower() == 'q' or file_indexes == '0':
            print('Aborted.')
            break
        print(" ")
        start_time = time.time()
        files_to_zip = []
        with zipfile.ZipFile(zip_filename, 'a') as zf:
            for index in file_indexes.split(','):
                index = int(index) - 1
                if index < len(files_in_directory):
                    filename = files_in_directory[index]
                    if os.path.exists(filename):
                        zf.write(filename)
                        print('File', filename, 'zipped to', zip_filename)
                        files_to_zip.append(filename)
                    else:
                        print('File', filename, 'does not exist. Skipping.')
                else:
                    print('Index', index, 'out of range. Skipping.')
        print(" ")
        end_time = time.time()
        total_time = end_time - start_time
        print(
            '\n╔═════════════════════════════════════════════════════════════════════════╗')
        print('║                   Zip Information')
        print(
            f"║     Start Time: {time.strftime('%H:%M:%S', time.localtime(start_time))}")
        print(
            f"║     End Time: {time.strftime('%H:%M:%S', time.localtime(end_time))}")
        print(f"║     Total Time: {total_time:.2f} seconds")
        print('║ Files:')
        for source in files_to_zip:
            file_name = source
            file_size = os.path.getsize(source)
            file_size_form = format_size(file_size)
            print(f"║   {file_name.ljust(64)}   [ {file_size_form.rjust(7)} ]")
        print('║\n║ Destination:')
        zip_size = os.path.getsize(zip_filename)
        zip_size_form = format_size(zip_size)
        print("║ " + (os.getcwd() + "/" + zip_filename).ljust(64) +
              f"   [ {zip_size_form.rjust(7)} ]")
        print('╚═════════════════════════════════════════════════════════════════════════╝')
        break
    input('Press enter to continue...')


def unzip_file(): # Unzip a ZIP File [Done code/ No color]
    os.system('clear')
    print_ascii('logo', logo_mode)
    print_ascii('unzip', title_mode)
    list_current()
    list_files()
    zip_files = os.listdir()
    if not zip_files:
        print('No files found in working directory.')
        input('Press enter to continue...')
    else:
        while True:
            zip_fileindex = input(
                'Enter a fileIndex ( seperate with comma 1,2,3) (0 or "q" to quit): ')
            zip_filename = zip_files[int(
                zip_fileindex)-1] if zip_fileindex != 'q' and zip_fileindex != '0' else None
            if zip_filename is None:
                print('Aborted.')
                input('Press enter to continue...')
                continue
            if '.zip' not in zip_filename:
                print('Error: Not a ZIP-file.')
                continue
            elif zip_filename in zip_files:
                start_time = time.time()
                with zipfile.ZipFile(zip_filename, 'r') as zf:
                    extracted_files = zf.namelist()
                    zf.extractall()
                    print(extracted_files)
                    end_time = time.time()
                    total_time = end_time - start_time
                print(
                    '\n╔═════════════════════════════════════════════════════════════════════════╗')
                print('║                   Unzip Information')
                print(
                    f"║     Start Time: {time.strftime('%H:%M:%S', time.localtime(start_time))}")
                print(
                    f"║     End Time: {time.strftime('%H:%M:%S', time.localtime(end_time))}")
                print(f"║     Total Time: {total_time:.2f} seconds")
                print('║ Files:')
                for source in extracted_files:
                    file_name = source
                    file_size = os.path.getsize(source)
                    file_size_form = format_size(file_size)
                    print(
                        f"║   {file_name.ljust(64)}   [ {file_size_form.rjust(7)} ]")
                print('║\n║ Destinations:')
                print(f"║   {os.getcwd()}")
                print(
                    '╚═════════════════════════════════════════════════════════════════════════╝')
            else:
                print(f'{zip_filename} not found in working directory.')
            input('Press enter to continue...')
            break


def change_dir(): # Change Directory to present Folder [Done code/ No color]
    os.system('clear')
    print_ascii('logo', logo_mode)
    print_ascii('dir', title_mode)
    list_current()
    cd_files = os.listdir()
    print('\nn╔═════════════════════════════════════════════════════════════════════════╗')
    for i, file in enumerate(cd_files):
        if os.path.isdir(file):
            print(f"║ {i+1}: {file}")
    print(f"║ {len(cd_files)+1}: Go back one folder")
    print('╚═════════════════════════════════════════════════════════════════════════╝')
    while True:
        foldername = input('Enter your Foldersnumber (0 or q to quit): ')
        if foldername.lower() == 'q' or foldername == '0':
            print('Aborted.')
            break
        if foldername.isdigit() == False:
            print("Invalid Inpu!")
            continue
        else:
            try:
                if foldername == str(len(cd_files)+1):
                    os.chdir('..')
                    break
                else:
                    foldername = cd_files[int(foldername)-1]
                    if os.path.isdir(foldername):
                        os.chdir(foldername)
                        break
                    else:
                        print("Folder not found")
            except ValueError:
                print("Folder not found")
            except IndexError:
                print("Folder not found")


def bash(): # Run s script from another file [Done code/ No color]
    os.system('clear')
    print_ascii('logo', logo_mode)
    print_ascii('bash', title_mode)
    list_current()
    print("\n Current Script Path: " + script_path)
    print('╔═════════════════════════════════════════════════════════════════════════╗\n║                 Select the script you want to run:' + ("║").rjust(23))
    for i, filename in enumerate(filenames):
        file_extension = filename.split('.')[-1]
        print(
            f'║ {("║").rjust(73)}\n║ {str(i+1).rjust(2)}: {filename.split("/")[-1].ljust(55)} ({filetypes[file_extension].rjust(7)})   ║')
    print(f'║ {("║").rjust(73)}\n║ 0 Back to main menu' +
          ("║").rjust(54))
    print(
        '╚═════════════════════════════════════════════════════════════════════════╝')
    choice = None
    while True:
        if choice is None:

            choice = input(
                'Enter the number of the script (0 or q to quit): ')
            if choice == '0' or choice.lower() == 'q':
                break

            try:
                choice = int(choice)
                if choice < 1 or choice-1 >= len(filenames):
                    print('Invalid input. Please try again.')
                    choice = None
                    continue
            except ValueError:
                print('Invalid input. Please try again.')
                choice = None
                continue
        else:
            if os.path.exists(script_path + filenames[choice-1]):
                os.system('clear')
                os.system(
                    f'{filetypes[filenames[choice-1].split(".")[-1]]} ' + script_path + filenames[choice-1])
                input('\n.Welcome Back Sir\n\nPress ENTER to continue..')
                break
            else:
                print('File not found. Please try again.')
                choice = None


def run_admin_command(): # Run a custom command [Done code/ No color]
    os.system('clear')
    print_ascii('logo', logo_mode)
    print_ascii('admin',    title_mode)
    list_current()

    global custom_cmd
    print(
        '\n╔═════════════════════════════════════════════════════════════════════════╗')
    print('║ Select a command (0 or q to quit): ')
    for i, cmd in enumerate(custom_cmd):
        print(f'║ {str(i+1).rjust(3)}. {cmd}')
    print(f'║ {str(len(custom_cmd)+1).rjust(3)}. Type your own:')
    print('╚═════════════════════════════════════════════════════════════════════════╝')
    while True:
        command = input('Enter a command: ')
        if command.lower() == 'q' or command == '0':
            print('Aborted.')
            break
        elif command.isdigit() == False:
            print('Invalid input. Please try again.')
            continue
        else:
            if int(command) in range(1, len(custom_cmd)+1):
                command = custom_cmd[int(command)-1]
            elif int(command) == len(custom_cmd)+1:
                command = input('Type your own command: ')
            else:
                print('Invalid input. Please try again.')
                continue
            print(
                '\n╔═════════════════════════════════════════════════════════════════════════╗')
            print('║ Command Executed:  ' + command)
            os.system(command)
            print(
                '╚═════════════════════════════════════════════════════════════════════════╝')
            input('\nPress enter to continue...')
            break


def rsync_backup(): # Backup files with rsync [Done code/ No color]
    os.system('clear')
    print_ascii('logo', logo_mode)
    print_ascii('rsync', title_mode)
    list_current()
    print('\n╔═════════════════════════════════════════════════════════════════════════╗\n║                   Choose Choose your File/s to Backup')
    for i, pfad in enumerate(backup_data):
        size = os.path.getsize(pfad)
        size = format_size(size)
        print(f"║ {i+1}: {pfad.ljust(64)} [ {size.rjust(7)} ]")
    print(f"║ {len(backup_data)+1}: Own Path")
    print('╚═════════════════════════════════════════════════════════════════════════╝')
    to_process = []

    while True:
        choiceg = input("Your Choice/s: (e.X: 0,1,2) (q or 0 to quit): ").split(",")
        choice = []
        
        for c in choiceg:
            if c.isdigit() == False:
                print("Invalid input: " + c)
                continue
            else:
                choice.append(c)
        if choice == 'q' or choice == '0':
            break
        elif len(choice) == 0:
            break
        
        elif choice == [str(len(backup_data)+1)]:
            list_custom()
            while True:
                custom_choice = input(
                    "XYour Custom Path (seperate with commas) (q or 0 to quit): ").split(",")
                if custom_choice == ['q'] or custom_choice == ['0']:
                    break
                
                elif int(custom_choice[0]) <= len(paths)+1:
                    if int(custom_choice[0]) == len(paths)+1:
                        print(
                            '\n╔═════════════════════════════════════════════════════════════════════════╗\n║                   Choose Choose your File/s to Backup')
                        for i, file in enumerate(os.listdir(os.getcwd())):
                            size = os.path.getsize(file)
                            size = format_size(size)

                            print(
                                f"║ {i+1}: {file.ljust(64)} [ {size.rjust(7)} ]")
                        print(f"║ {len(os.listdir(os.getcwd()))+1}: Own Path")
                        print(
                            '╚═════════════════════════════════════════════════════════════════════════╝')
                        while True:
                            current_choice = input(
                                "EYour Choice/s: (e.X: 0,1,2) (q or 0 to quit): ").split(",")
                            print(int(current_choice[0]), len(os.listdir(os.getcwd()))+1)
                            
                            if current_choice == ['q'] or current_choice == ['0']:
                                break
                            elif int(current_choice[0]) in range(1, len(os.listdir(os.getcwd()))+1):
                                if int(current_choice[0]) == len(os.listdir(os.getcwd()))+1:
                                    path = input(
                                        "Please enter the custom path to FOLDER: ")
                                    if os.path.exists(path):
                                        print(
                                            '\n╔═════════════════════════════════════════════════════════════════════════╗\n║                   Choose Choose your File/s to Backup')
                                        for i, fname in enumerate(os.listdir(path)):
                                            size = os.path.getsize(fname)
                                            size = format_size(size)
                                            print(
                                                f"║ {i+1}: {fname.ljust(64)} [ {size.rjust(7)} ]")
                                        print(
                                            '╚═════════════════════════════════════════════════════════════════════════╝')
                                        current_choice = input(
                                            "YYour Choice/s: (e.X: 0,1,2) (q or 0 to quit): ").split(",")
                                        if current_choice == ['q'] or current_choice == ['0']:
                                            break
                                        for i in current_choice:
                                            to_process.append(
                                                os.listdir(path)[int(i)-1])
                                        break
                                    else:
                                        print("Invalid Path!")
                                else:
                                    for i in current_choice:
                                        to_process.append(
                                            os.listdir(os.getcwd())[int(i)-1])
                                    print("done")
                                    break
                            else:
                                print("Invalid Choice!")
                            break
                    else:
                        for i in custom_choice:
                            to_process.append(paths[int(i)-1])
                        break
                else:
                    print("Invalid Choice!")
                break
        elif int(choice[0]) in range(len(backup_data)):
            for i in choice:
                to_process.append(backup_data[int(i)-1])
            break
        else:
            print("Invalid Choice!")
        break

    if choice == ['q'] or choice == ['0']:
        input("Aboarding rsync...")
    elif len(choice) == 0:
        input("Aboarding rsync...")
    else:
        print('\n╔═════════════════════════════════════════════════════════════════════════╗\n║                   Files to be saved:')
        for i in to_process:
            size = os.path.getsize(i)
            size = format_size(size)
            print(f"║ {i.split('/')[-1]}: {i.ljust(64)} [ {size.rjust(7)} ]")
        print('╚═════════════════════════════════════════════════════════════════════════╝')

        if len(to_process) > 0:
            print(
                '\n╔═════════════════════════════════════════════════════════════════════════╗\n║                   Choose Destination/s to Backup')
            for i, pfad in enumerate(destinations):
                print(f"║ {i+1}: {pfad}")
            print('╚═════════════════════════════════════════════════════════════════════════╝')
            selected_destinations = []
            while True:
                destination_choice = input(
                    "Your Choice/s: (e.X: 0,1,2) (q or 0 to quit): ")
                if destination_choice.lower() == 'q' or destination_choice == '0':
                    break
                else:
                    try:
                        for choice in destination_choice.split(','):
                            if int(choice)-1 in range(len(destinations)):
                                selected_destinations.append(
                                    destinations[int(choice)-1])
                            else:
                                print(f"Index {choice} skipped")
                        break
                    except ValueError:
                        print("Error Aborded!")
                        break
            if len(selected_destinations) > 0:
                start_time = time.time()
                for source in to_process:
                    print(source)
                    for destination in selected_destinations:
                        if os.path.isdir(source):
                            print("\nSource is a Folder == Creating ZIP File...")
                            zip_name = source + '.zip'
                            zip_file = zipfile.ZipFile(zip_name, 'w')
                            for root, dirs, files in os.walk(source):
                                for file in files:
                                    zip_file.write(os.path.join(root, file))
                            zip_file.close()
                            print("\nDone creating ZIP File!\n")
                            os.system('rsync -av ' + zip_name + ' ' + destination)
                            os.remove(zip_name)
                            print(
                                f"\n═══Backup up {source} to {destination} finished!═══\n")
                        else:
                            os.system('rsync -av ' + source + ' ' + destination)
                end_time = time.time()
                total_time = end_time - start_time
                print(
                    '\n╔═════════════════════════════════════════════════════════════════════════╗')
                print('║                   Backup Information')
                print(
                    f"║ Start Time: {time.strftime('%H:%M:%S', time.localtime(start_time))}")
                print(
                    f"║ End Time: {time.strftime('%H:%M:%S', time.localtime(end_time))}")
                print(f"║ Total Time: {total_time:.2f} seconds")
                print('║ Files:')
                for source in to_process:
                    file_name = source
                    file_size = os.path.getsize(source)
                    file_size_form = format_size(file_size)
                    print(
                        f"║ {file_name.ljust(64)}   [ {file_size_form.rjust(7)} ]")
                print('║\n║ Destinations:')
                for destination in selected_destinations:
                    print(f"║ {destination}")
                print(
                    '╚═════════════════════════════════════════════════════════════════════════╝')

                print("Backup Finished!")
                input("Press Enter to continue...")
            else:
                print("No Destination Chosen!")
                input("Press Enter to continue...")
        else:
            print("No File Chosen!")
            input("Press Enter to continue...")


def list_current(): # Menu Header [Done code/ Color Done]
    dirlen = os.listdir()
    files = [f for f in dirlen if os.path.isfile(f)]
    folders = [f for f in dirlen if not os.path.isfile(f)]
    if show_files:
        show = "ON "
        color = "\033[33m"
    elif not show_files:
        show = "OFF"
        color = "\033[31m"
    else:
        show = "ERR"

    if show_mode:
        show_m = "SHOW"
        show_mode_c = "\033[33m"
    elif not show_mode:
        show_m = "HIDE"
        show_mode_c = "\033[31m"
    else:
        show_m = "ERR"
    net_io_counters = psutil.net_io_counters()
    net_speed = (net_io_counters.bytes_sent +
                 net_io_counters.bytes_recv) / 1024 / 1024
    net_speed = round(net_speed, 1)
    net_send = round((net_io_counters.bytes_sent / 1024 / 1024), 1)
    net_recv = round((net_io_counters.bytes_recv / 1024 / 1024), 1)
    boot_time = psutil.boot_time()
    cpu_temp = os.popen("vcgencmd measure_temp").readline()[5:9]
    uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(boot_time)
    days, seconds = divmod(uptime.total_seconds(), 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    now = datetime.datetime.now()
    format_time = now.strftime("%Y/%m/%d - %H:%M:%S")

    print(
        '\033[36m╔══════════════════════════════════════════╦═══════════════════╗\033[0m')
    print('\033[36m║\033[0m \033[35mNetwork Speed Total:\033[0m \033[32m' + str(net_speed).ljust(7) +
          ' MB/s \033[0m' + red + cpu_temp + 'C°\033[0m \033[36m║\033[0m \033[35mSend:\033[0m \033[32m' + str(net_send).rjust(6) + ' MB/s\033[0m \033[36m║\033[0m')
    print('\033[36m╠════════════════════════════╗ \033[35mCPU:\033[0m \033[31m' + str(psutil.cpu_percent()).rjust(5) + "%" +
          '\033[0m \033[36m║\033[0m \033[35mRecv:\033[0m \033[32m' + str(net_recv).rjust(6) + ' MB/s\033[0m \033[36m║\033[0m')
    print('\033[36m║\033[0m \033[35mCurrent working directory:\033[0m \033[36m╚═════════════╩═══════════════════╝\033[0m')
    print('\033[36m║\033[0m          \033[35m==>\033[0m ' + os.getcwd())
    print('\033[36m║\033[0m \033[35m[X]:\033[0m ' + color + show.ljust(3) +
          '\033[0m \033[36m    ╚═══════════════╦══════════════════════════════════════════════════╗\033[0m')
    print('\033[36m║\033[0m      \033[35mFiles:\033[0m \033[32m' + str(len(files)).ljust(3) + ' \033[0m\033[35mFolders:\033[0m \033[32m' + str(len(folders)).ljust(3) +
          '\033[0m \033[36m║\033[0m \033[35m      Time:\033[0m    \033[33m' + str(format_time).ljust(26) + str("\033[0m\033[36m     ║").rjust(18) + '\033[0m')
    print('\033[36m╚════════════════╗ \033[35mTotal:\033[0m \033[32m' + str(len(files) + len(folders)).ljust(4) + '\033[0m \033[36m║\033[0m \033[35mUptime:\033[0m \033[33m' +
          str("%d days, %d hours, %d minutes, %d seconds" % (days, hours, minutes, seconds)))
    print('\033[35m[D]esign:\033[0m ' + show_mode_c + show_m.ljust(7) +
          '\033[0m\033[36m╚═════════════╝\033[0m \033[36m' + str("══╝").rjust(50) + '\033[0m')

    if (show_files):
        list_files()


def list_custom(): # List Custompaths [Done code/ No color]
    print(rainbow_ascii("\n  Your Customized Paths:", 'hacker'))
    print('╔═════════════════════════════════════════════════════════════════════════╗')
    for i in range(len(paths)):
        if i < 9:
            print('║ {}.  ║ {}'.format(i + 1, shorten_path(paths[i])))
        else:
            print('║ {}. ║ {}'.format(i + 1, shorten_path(paths[i])))
    print('║ {}. ║ Type your own'.format(len(paths) + 1))
    print('╚═════════════════════════════════════════════════════════════════════════╝')

def shorten_path(path): # Shorten Path [Done code/ No color needed]
    path_parts = path.split('/')
    if len(path_parts) >= 6:
        return '/'.join(path_parts[:3]) + '/.../' + '/'.join(path_parts[-3:])
    else:
        return path


def monitor_stats(): #Start Loop for updating Stats every X seconds [No code/ No color]
    random_asc = random.randint(1, len(bye_ascii))
    new_asci_in = 10
    stat_ascii_mode = 'death'
    c = 0
    refresh_time = 1
    while True:
        try:
            if c == new_asci_in:
                c = 0
                random_asc = random.randint(1, len(bye_ascii))
            os.system("clear")
            print_ascii('logo', stat_ascii_mode)
            print(" ")
            print(" ")
            list_current()
            print(" ")
            print(" ")
            print("Displaying Stats every " + str(refresh_time) + " seconds  [ CRTL + C to quit ]")
            print_ascii(bye_ascii[random_asc], stat_ascii_mode)
            time.sleep(refresh_time)
            c += 1
        except KeyboardInterrupt:
            break
        

def switch_show(sbof): # Switch for always show current files of folder [Done code/ No color]
    global show_files
    if (sbof):
        print("  Show Files is now: OFF")
        show_files = False
    elif (not sbof):
        print("  Show Files is now: ON")
        show_files = True
    input("  Press Enter to continue...")


def switch_design(): # Switch for ASCII Design Mode [Done code/ No color]
    print("  Select a Design Mode:")
    print('\n╔═════════════════════════════════════════════════════════════════════════╗')
    for mode in modes:
        print(f'║ {str(modes.index(mode) + 1).rjust(2)}.  ║  {mode}')
    print(f'║ {str(len(modes)+ 1).rjust(2)}.  ║  Switch off Show Mode')
    print('║ 0 or q to quit')
    mode_choice = input('║ Your Choice: ')
    if mode_choice == '0' or mode_choice.lower() == 'q':
        print("  Exiting...")
        input("  Press Enter to continue...")
    elif int(mode_choice) == len(modes)+1:
        global show_mode
        if show_mode:
            show_mode = False
        elif not show_mode:
            show_mode = True
        print(" Show Designname is now  " + str(show_mode))
    elif int(mode_choice) > len(modes)+1:
        print("  Invalid Choice! Aborting...")
        input("  Press Enter to continue...")
    else:
        global logo_mode
        logo_mode = modes[int(mode_choice) - 1]
        global title_mode
        title_mode = modes[int(mode_choice) - 1]
        print("  Design Mode set to: " + title_mode)
        input("  Press Enter to continue...")


def show_main_menu(): # Display the Main menu [Done code/ No color]
    os.system('clear')
    print_ascii('logo', logo_mode)
    print_ascii('main', title_mode)

    list_current()
    print("\n    HELP? == type help")
    print('╔═════════════════════════════════════════════════════════════════════════╗')
    print(
        f'║ 1.     ║ Manager                                              {("║").rjust(11)}')
    print(
        f'║ 2.     ║ Scripts                                              {("║").rjust(11)}')
    print(
        F'║ 3.     ║ Admin/Commands                                       {("║").rjust(11)}')
    print(
        F'║ 4.     ║ Monitor Stats                                        {("║").rjust(11)}')
    print(
        F'║ 5.     ║ Fast Travel                                          {("║").rjust(11)}')
    print(
        F'║ 6.     ║ RSYNC BackUp                                         {("║").rjust(11)}')
    print(
        F'║ 7.     ║ Show all ASCII Colormodes                            {("║").rjust(11)}')
    print(
        F'║ 0.     ║ QUIT                                                 {("║").rjust(11)}')
    print(F'╚═════════════════════════════════════════════════════════════════════════╝')
    return input('Enter a number: ')


def show_manager_menu(): # Display the Manager menu [Done code/ No color]
    os.system('clear')
    print_ascii('logo', logo_mode)
    print_ascii('manager', title_mode)

    list_current()
    print("\n        HELP? == type help")
    print('╔═════════════════════════════════════════════════════════════════════════╗')
    print(
        f'║ 1. ║ <fast> Travel                                                {("║").rjust(7)}')
    print(
        f'║ 2. ║ <list> Files                                                 {("║").rjust(7)}')
    print(
        f'║ 3. ║ <find> File                                                  {("║").rjust(7)}')
    print(
        f'║ 4. ║ <create> Folder or Create/Edit File                          {("║").rjust(7)}')
    print(
        f'║ 5. ║ <read> File                                                  {("║").rjust(7)}')
    print(
        f'║ 6. ║ <rename> File                                                {("║").rjust(7)}')
    print(
        f'║ 7. ║ <move> File                                                  {("║").rjust(7)}')
    print(
        f'║ 8. ║ <copy> File                                                  {("║").rjust(7)}')
    print(
        f'║ 9. ║ <delete> File                                                {("║").rjust(7)}')
    print(
        f'║ 10.║ <zip> File/s                                                 {("║").rjust(7)}')
    print(
        f'║ 11.║ <unzip> File                                                 {("║").rjust(7)}')
    print(
        f'║ 12.║ <ch>ange Directory                                           {("║").rjust(7)}')
    print(
        f'║ 13.║ <rsync> Backup                                               {("║").rjust(7)}')
    print(
        f'║ 0. ║ Back to main menu                                            {("║").rjust(7)}')
    print('╚═════════════════════════════════════════════════════════════════════════╝')
    return input('Enter a number: ')



# ==================================================================================================
# ==================================================================================================
# =======================================  MAIN   ==================================================
# ==================================================================================================
# ==================================================================================================


def main():
    try:
        while True:
            main_menu_selection = show_main_menu()
            if main_menu_selection == '1':
                while True:
                    manager_menu_selection = show_manager_menu()
                    if manager_menu_selection == '1' or manager_menu_selection == "fast":
                        fast_travel()
                    elif manager_menu_selection == '2' or manager_menu_selection == "list":
                        list_files()
                        input('Press enter to continue...')
                    elif manager_menu_selection == '3' or manager_menu_selection == "find":
                        find_file()
                    elif manager_menu_selection == '4' or manager_menu_selection == "create":
                        create()
                    elif manager_menu_selection == '5' or manager_menu_selection == "read":
                        read_file_out()
                    elif manager_menu_selection == '6' or manager_menu_selection == "rename":
                        rename_file()
                    elif manager_menu_selection == '7' or manager_menu_selection == "move":
                        move_file()
                    elif manager_menu_selection == '8' or manager_menu_selection == "copy":
                        copy_file()
                    elif manager_menu_selection == '9' or manager_menu_selection == "delete":
                        delete_file()
                    elif manager_menu_selection == '10' or manager_menu_selection == "zip":
                        zip_file()
                    elif manager_menu_selection == '11' or manager_menu_selection == "unzip":
                        unzip_file()
                    elif manager_menu_selection == '12' or manager_menu_selection == "ch":
                        change_dir()
                    elif manager_menu_selection == '13' or manager_menu_selection == "rsync":
                        rsync_backup()
                    elif manager_menu_selection.lower() == 'x':
                        switch_show()
                    elif manager_menu_selection.lower() == 'd' :
                        switch_design()
                    elif manager_menu_selection.lower() == 'help':
                        print(info)
                        input("Press enter to continue...")
                    elif manager_menu_selection == '0' or manager_menu_selection.lower() == 'q':
                        break
                    else:
                        print("Invalid input. Please try again.")
            elif main_menu_selection == '2':
                bash()
            elif main_menu_selection == '3':
                run_admin_command()
            elif main_menu_selection == '4':
                monitor_stats()
            elif main_menu_selection == '5':
                fast_travel()
            elif main_menu_selection == '6':
                rsync_backup()
            elif main_menu_selection == '7':
                ascii_color_show()
            elif main_menu_selection.lower() == 'x':
                switch_show(show_files)
            elif main_menu_selection.lower() == 'd':
                switch_design()
            elif main_menu_selection.lower() == 'help':
                print(info)
                input("Press enter to continue...")
            elif main_menu_selection == '0' or main_menu_selection.lower() == 'q':
                rand = random.randint(1, len(bye_ascii))
                print_ascii(bye_ascii[rand], 'r')
                break
    except KeyboardInterrupt:
        signal_handler(True)


if __name__ == '__main__':
    main()
