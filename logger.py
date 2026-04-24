'''
    @author: George Gugulea
    @author_email: george.gugulea@certsign.ro
    @date: 2026.04.20
    @description: Parse knowb4 egress links found in emails and extract the original URL
'''

import traceback
import sys

class Logger:
    @staticmethod
    def LogError(msg):
        Logger.TerminalPrintOnRed("ERROR: " + msg)


    @staticmethod
    def LogWarning(msg):
        Logger.TerminalPrintOnYellow("WARNING: " + msg)

    @staticmethod
    def LogInfo(msg):
        print("INFO: ", msg)

    @staticmethod
    def LogException(msg, ex):
        Logger.LogError(msg + ":" + ex)

    @staticmethod
    def LogExceptionTrace(msg, ex):
        print("ERROR: ", msg)
        print('-'*60)
        traceback.print_exc(file=sys.stdout)
        print('-'*60)
        # extype, value, tb = sys.exc_info()
        # pdb.post_mortem(tb)
        # print('-'*60)

    @staticmethod
    def TerminalPrintColor(msg, fgcolor, bgColor, bold=False):
        style = '1' if bold else '0'
        code = f"{style};{fgcolor};{bgColor}"
        print(f"\033[{code}m {msg} \033[00m")

    @staticmethod
    def TerminalPrintRed(msg):
        Logger.TerminalPrintColor(msg, fgcolor='31', bgColor='40')
    
    @staticmethod
    def TerminalPrintGreen(msg):
        Logger.TerminalPrintColor(msg, fgcolor='32', bgColor='40')
    
    @staticmethod
    def TerminalPrintYellow(msg):
        Logger.TerminalPrintColor(msg, fgcolor='33', bgColor='40')

    @staticmethod
    def TerminalPrintBlue(msg):
        Logger.TerminalPrintColor(msg, fgcolor='34', bgColor='40')

    @staticmethod
    def TerminalPrintOnRed(msg):
        Logger.TerminalPrintColor(msg, fgcolor='37', bgColor='41')

    @staticmethod
    def TerminalPrintOnGreen(msg):
        Logger.TerminalPrintColor(msg, fgcolor='37', bgColor='42')

    @staticmethod
    def TerminalPrintOnYellow(msg):
        Logger.TerminalPrintColor(msg, fgcolor='30', bgColor='43')

    @staticmethod
    def TerminalPrintOnBlue(msg):
        Logger.TerminalPrintColor(msg, fgcolor='37', bgColor='44')