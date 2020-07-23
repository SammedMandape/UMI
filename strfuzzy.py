#import pdb
# Author: Benjamin Crysup
"""Contains utilities for finding things in a fuzzy manner."""

def fuzzyFind(inString, subString, fuzz=0, start=0, end=None):
    """
        This will search for a string inside another, allowing for up to fuzz mismatches.
        @param inString: The string to search through.
        @param subString: The string to search for.
        @param fuzz: The maximum number of mismatches to allow.
        @param start: The index to start searching from. Defaults to the real start.
        @param end: The index to stop searching at. Defaults to the real end.
        @return: The index at which subString can be found in inString (with up to fuzz mismatches), or -1 if it is not found.
    """
    # handle the empty string special
    if len(subString) == 0:
        return 0
    # get the slice of the string
    end = len(inString) if (end is None) else end
    sliceInStr = inString[start:end]
    # note the actual start index
    rstart = start if (start >= 0) else (len(inString) + start)
    # run down that slice
    for i in range(0, 1+len(sliceInStr)-len(subString)):
        totFuzz = 0
        for j in range(0, len(subString)):
            if sliceInStr[i+j] != subString[j]:
                #pdb.set_trace()
                totFuzz = totFuzz + 1
                if totFuzz > fuzz:
                    break
        if totFuzz <= fuzz:
            return rstart + i
    return -1

#print(fuzzyFind("ABCDEFGHIJK", "DZF", fuzz=0))
#print(fuzzyFind("....ABC....", "ABC"))
def fuzzyFindAll(inString, subString, fuzz=0, start=0, end=None):
    """
        This will search for all occurrences of a string (with up to fuzz number of mismatches) in another.
        @param inString: The string to search through.
        @param subString: The string to search for.
        @param fuzz: The maximum number of mismatches to allow.
        @param start: The index to start searching from. Defaults to the real start.
        @param end: The index to stop searching at. Defaults to the real end.
        @return: All the indices it was found at.
    """
    # get the slice of the string
    end = len(inString) if (end is None) else end
    sliceInStr = inString[start:end]
    # note the actual start index
    rstart = start if (start >= 0) else (len(inString) + start)
    # handle the empty string special
    if len(subString) == 0:
        return [rstart + i for i in range(0, len(sliceInStr)+1)]
    # run down the rest
    toRet = []
    subStart = 0
    while subStart < len(inString):
        subInd = fuzzyFind(sliceInStr, subString, fuzz, subStart)
        if subInd < 0:
            subStart = len(inString)
        else:
            toRet.append(subInd)
            subStart = subInd + 1
    return toRet


import unittest

class _FuzzyTest(unittest.TestCase):
    def test_exact(self):
        self.assertTrue(fuzzyFind("....ABC....", "ABC", 0) == 4)
    def test_off(self):
        self.assertTrue(fuzzyFind("....ADC....", "ABC", 0) == -1)
    def test_one(self):
        self.assertTrue(fuzzyFind("....ADC....", "ABC", 1) == 4)
    def test_multi_exact(self):
        self.assertTrue(set(fuzzyFindAll("....AGADAGA....", "AGA", 0)) == set([4,8]))
    def test_multi_one(self):
        self.assertTrue(set(fuzzyFindAll("....AGADAGA....", "AGA", 1)) == set([4,6,8]))

if __name__ == "__main__":
   unittest.main()
