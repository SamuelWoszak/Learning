#Transform the number (needs to be an int number) to extense form
import num2words

numberInputed = int(input('Insert the number that you want to write by extense: '))
print(f'English Version: {num2words.num2words(numberInputed, lang="en")}')
print(f'English Version: {num2words.num2words(numberInputed, lang="pt")}')
