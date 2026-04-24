'''
    @author: George Gugulea
    @author_email: gugulea@gmail.com
    @date: 2026.04.20
    @description: Parse knowb4 egress links found in emails and extract the original URL
'''

import sys
import pathlib
import os

from options import Options
from logger import Logger
from knowb4_decode import KnowB4Decode

knowb4_decode_version = "0.0.1"

# ############################################### ###############################################

def check_preconditions(options):
    if options.url is None or options.url == "":
        Logger.LogError("URL is not specified")
        return False
        os.makedirs(options.workingDir)
    return True

def printVersion():
    msg = "knowb4_decode v{0}".format(knowb4_decode_version)
    print(msg)


# ############################################### ###############################################

def print_decoded(knowb4):
    Logger.TerminalPrintBlue("================================================================================")
    if knowb4.domain != "links.eu1.defend.egress.com":
        Logger.LogWarning("Encoded URL is not a links.eu1.defend.egress.com URL")
    Logger.TerminalPrintGreen(f"| Decoded URL: {knowb4.urlDecoded}")
    Logger.TerminalPrintBlue("================================================================================")

def open_in_browser(url):
    print("Do you want to open the decoded URL in the default browser? (y/n)")
    answer = input().lower()
    if answer == "y":
        import webbrowser
        webbrowser.open(url)

def main(argv):

    options = Options()
    options.parseCommandLine(argv)

    if options.printVersionAndExit:
        printVersion()
        sys.exit()

    if not check_preconditions(options):
        return False

    try:
        kb4decoder = KnowB4Decode(options)
        if not kb4decoder.decode():
            Logger.LogError("Failed to decode the URL")
            return False
        print_decoded(kb4decoder)
        KnowB4Decode.AnalyzeURL(kb4decoder.urlDecoded)

        # open_in_browser(kb4decoder.urlDecoded)

        return True

    except Exception as ex:
        Logger.LogExceptionTrace("main: Got an error", ex)

# ############################################### ###############################################

if __name__ == '__main__':
    main(sys.argv[1:])
