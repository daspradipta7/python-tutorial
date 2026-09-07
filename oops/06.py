class Utils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]


raw = " water, sugar, salt, vinegar, lemon juice "

cleaned_ingredients = Utils.clean_ingredients(raw)
print(cleaned_ingredients)
