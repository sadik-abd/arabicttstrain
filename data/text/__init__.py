from typing import Union

from data.text.symbols import all_phonemes
from data.text.tokenizer import Phonemizer, Tokenizer


class TextToTokens:
    def __init__(self, phonemizer: Phonemizer, tokenizer: Tokenizer):
        self.phonemizer = phonemizer
        self.tokenizer = tokenizer
    
    def __call__(self, input_text: Union[str, list]) -> list:
        phn = ""
        for txt in input_text.split("."):
            phons = self.phonemizer(txt)
            phn += " ".join(phons) + ". "
        tokens = self.tokenizer(phn)
        return tokens
    
    @classmethod
    def default(cls, language: str, add_start_end: bool, with_stress: bool, model_breathing: bool, njobs=1):
        phonemizer = Phonemizer(language=language, njobs=njobs, with_stress=with_stress)
        tokenizer = Tokenizer(add_start_end=add_start_end, model_breathing=model_breathing)
        return cls(phonemizer=phonemizer, tokenizer=tokenizer)
