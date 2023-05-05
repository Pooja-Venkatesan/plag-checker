from termcolor import colored

text = "This is some text to highlight"
highlighted_text = colored(text, 'red', attrs=['underline', 'bold'])
print(highlighted_text)