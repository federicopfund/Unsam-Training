
#%%
class TextManipulator:
    def __init__(self, text):
        self.text = text
        self.words = text.split()

    def neutralize_word(self, word):
        if len(word) >= 2 and word[-2] == '0':
            return word[:-2] + 'e' + word[-1]
        elif word[-1] == 'o':
            return word[:-1] + 'e'
        else:
            return word

    def neutralize_all_words_generator(self):
        for word in self.words:
            yield self.neutralize_word(word)

    def manipulate_text(self):
        neutralized_words = self.neutralize_all_words_generator()
        return ' '.join(neutralized_words)

#%%
# Ejemplo de uso de la clase TextManipulator
frase = '¿como trasmitir a los otros el infinito Aleph?'
text_manipulator = TextManipulator(frase)
frase_t = text_manipulator.manipulate_text()

print(frase_t)

