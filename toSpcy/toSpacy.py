import re

class Convertor():
    def __init__(self, tagslabels={}):
        self._tagslabels = tagslabels

    def _handleLabel(self, tag):
        if tag in self._tagslabels.keys():
            return self._tagslabels[tag]
        return tag

    def _handleSingle(self, t):

        entities = []
        index = 0
        t = re.sub(r'\s+', ' ', t)
        tList = re.split('(<[a-zA-Z]+>[^<]+</[a-zA-Z]+>)', t)
        if len(tList) % 2 == 0:
            print("Error! Some labels might be missed! ")
            return

        pattern = re.compile("<[a-zA-Z]+>[^<]+</[a-zA-Z]+>")
        for ele in tList:
            if pattern.match(ele):
                len_notag = len(''.join(re.split('</?[a-zA-Z]+>', ele)))
                entities.append((index, index + len_notag,
                                 self._handleLabel(re.split('.+</|>', ele)[1])))
                index += len_notag
            else:
                index += len(ele)

        return (''.join(re.split('</?[a-zA-Z]+>', t)), {'entities': entities})

    def toSpacyFormat(self, tagged_data):
        return [self._handleSingle(data) for data in tagged_data]
