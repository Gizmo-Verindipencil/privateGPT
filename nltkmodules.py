# ref : https://github.com/delip/PyTorchNLPBook/issues/14#issuecomment-1057151683

import nltk
import ssl

def load():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    nltk.download("punkt")