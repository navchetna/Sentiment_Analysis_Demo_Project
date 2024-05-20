from better_profanity import profanity


class profanity_masker():
    def __init__(self) -> None:
        profanity.load_censor_words()

    def mask_words(self, text):
        censored_text = profanity.censor(text)
        return censored_text