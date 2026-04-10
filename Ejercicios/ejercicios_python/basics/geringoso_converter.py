
"""
Geringoso converter module.

Converts words to 'Geringoso' language where vowels are repeated with 'p' in between.
"""

class GeringosoConverter:
    """Converter for Geringoso language."""
    def __init__(self):
        self.dictionary = {}

    def convert_to_geringoso(self, word):
        """
        Convert a single word to Geringoso.

        Args:
            word (str): The word to convert.

        Returns:
            str: The converted word.
        """
        if not isinstance(word, str):
            raise ValueError("Input must be a string")
        converted_word = ""
        for char in word.lower():
            if char in "aeiou":
                converted_word += char + "p" + char
            else:
                converted_word += char
        return converted_word

    def process_list(self, word_list):
        """
        Process a list of words and store conversions in dictionary.

        Args:
            word_list (list): List of words to convert.

        Returns:
            dict: Dictionary with original words as keys and converted as values.
        """
        self.dictionary = {}
        for word in word_list:
            try:
                converted = self.convert_to_geringoso(word)
                self.dictionary[word] = converted
            except ValueError as e:
                print(f"Error converting '{word}': {e}")
        return self.dictionary


if __name__ == "__main__":
    # Create an instance of the GeringosoConverter
    geringoso_instance = GeringosoConverter()

    # Use the instance to process a list of words
    result = geringoso_instance.process_list(['pera', 'mandarina', 'naranja'])

    # Display the result
    print(result)
