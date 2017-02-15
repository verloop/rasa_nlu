from mitie import tokenize
import re


class MITIETokenizer(object):
    def __init__(self):
        pass

    def tokenize(self, text, nlp=None):
        return [w.decode('utf-8') for w in tokenize(text.encode('utf-8'))]

    def tokenize_with_offsets(self, text):
        _text = text.encode('utf-8')
        offsets = []
        offset = 0
        tokens = [w.decode('utf-8') for w in tokenize(_text)]
        for tok in tokens:
            m = re.search(re.escape(tok), _text[offset:])
            offsets.append(offset + m.start())
            offset += m.end()
        return tokens, offsets
