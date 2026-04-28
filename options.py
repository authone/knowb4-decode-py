'''
Options class to parse command line parameters:
            -h                      print this help and exit.   
            -v, --version           print application version and exit.
            -t, --text              simple text output
            --url url               knowb4 egress URL to parse
'''

import getopt
import sys

class Options:
    def __init__(self):
        self.printVersionAndExit = False
        self.url = None
        self.textOutput = False

    def parseCommandLine(self, argv):
        try:
            opts, args = getopt.getopt(
                argv, "hvtu:", ["version", "url="])
        except getopt.GetoptError:
            self.printHelp()
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                self.printHelp()
                sys.exit()
            elif opt in ("-v", "--version"):
                self.printVersionAndExit = True
            elif opt in ("-t", "--text"):
                self.textOutput = True
            elif opt in ("--url"):
                self.url = arg
    def printHelp(self):
        print('''
            -h                      print this help and exit.   
            -v, --version           print application version and exit.
            -t, --text              simple text output
            -u,--url url               knowb4 egress URL to parse
            ''')

