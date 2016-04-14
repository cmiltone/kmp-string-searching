"""
The Knuth-Morris-Pratt string matching algorithm
"""

class kmp:
    pattern = "ACACAGT" #input("Enter pattern:")
    string = "ACAT ACGACACAGT"#input("Enter String")
    ptbl = [] #prefix table:- contains longest Same Prefix and Suffix Lengths
        
    def initPTbl():
        pattern = kmp.pattern
        m = len(pattern)
        i = 0
        for i in range(m):
            k = 1
            prefixes = []
            suffixes = []
            #slice to get all possible prefixes & suffixes in the pattern
            while k <= i:
                prefixes.append(''.join(pattern[0:k]))
                suffixes.append(''.join(pattern[k:i+1]))
                k+=1
            #get the lengths of characters that are both in the prefixes and suffixes
            same = [len(v) for v in prefixes if v in suffixes]
            #get the longest length
            if len(same) >0:
                lsp = max(same)
            else:
                lsp = 0
            kmp.ptbl.append(lsp)
            
        return kmp.ptbl

    def doSearch():
        pos = []
        ptn = kmp.pattern
        strng = kmp.string
        kmp.initPTbl()
        print("Looking for pattern %s in string %s: "%(ptn, strng))
        m = len(strng)
        l = len(ptn)
        i = 0
        j = 0
        while i < m:
            print("Checking... string[%i](%s) and pattern[%i](%s)"%(i, strng[i:i+l+1], j, ptn[j]))
            if strng[i:i+l] == ptn[0:l+1]:
                pos.append(i)
                print("Found match at position %i in string"%i)
            if ptn[j] == strng[i]:
                i+= 1
                j+= 1
                print("Same... next pair")
            elif ptn[j] != strng[i]:
                shift = kmp.ptbl[j]
                if kmp.ptbl[j] == 0:
                    shift = 1
                print("Not same... shifting from string[%i] to string[%i]"%(i, i+shift))
                i+= shift
                j = 0
            if j == l:
                j = 0
        if len(pos):
            print("Am done! the pattern is at position(s): %s of the string."%pos)
        else:
            print("Am done but sorry the pattern was not found in the string!")
