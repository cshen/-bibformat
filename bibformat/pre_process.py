import re

"""
    echo "$@" | tr '[:upper:]' '[:lower:]' | gsed "s/ on / /g" | \
        gsed "s/proceedings/ /g" |   \
        gsed "s/proc./ /g" |         \
        gsed "s/ and / /g" |         \
        gsed "s/CVF//g" |   \
        gsed "s/ of / /g" | \
        gsed "s/ the / /g" | \
        gsed "s/international/int./g" | \
        gsed "s/european/eur./g" | \
        gsed "s/\///g"  | \
        gsed "s/conference/conf./g" |\
        gsed "s/transactions/trans./g" |\
        gsed "s/computer/comp./g" |\
        gsed "s/vision/vis./g" |
        gsed "s/machine/mach./g" |
        gsed "s/learning/learn./g" |
        gsed "s/recognition/recogn./g" |
        gsed "s/pattern/patt./g" |
        gsed "s/journal/j./g" |
        gsed "s/  / /g" |\
        gsed "s/  / /g"
"""


def mysed(  patt, replace, input):

    input = input.lower()
    out = re.sub(patt, replace, input)
    return out


def pre_process(input_str):
    input_str = mysed('proceedings', '', input_str)
    input_str = mysed('proc.', '', input_str)
    input_str = mysed(' and ', ' ', input_str)
    input_str = mysed(' of ', ' ', input_str)
    input_str = mysed(' on ', ' ', input_str)
    input_str = mysed('the', '', input_str)
    input_str = mysed('cvf','', input_str)
    input_str = mysed('international', 'int.', input_str)
    input_str = mysed('european', 'eur.', input_str)
    input_str = mysed('conference', 'conf.', input_str)
    input_str = mysed('transactions', 'trans.', input_str)
    input_str = mysed('journal', 'j.', input_str)
    input_str = mysed('computer', 'comp.', input_str)
    input_str = mysed('vision', 'vis.', input_str)
    input_str = mysed('machine', 'mach.', input_str)
    input_str = mysed('learning', 'learn.', input_str)
    input_str = mysed('pattern', 'patt.', input_str)
    input_str = mysed('recognition', 'recogn.', input_str)

    input_str = mysed('  ', ' ', input_str)
    input_str = mysed('   ', ' ', input_str)
    input_str = mysed('    ', ' ', input_str)
    return input_str
