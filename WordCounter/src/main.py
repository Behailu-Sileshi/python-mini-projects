def word_counter(file_path: str) -> None:
    '''

    :param file_path: string 
    :return: void

    This method accept the path of text file as its parameter and print no of lines, words, and characters in the console.
    '''
    with open(file_path) as file:
        lines = file.readlines()
        no_of_line = len(lines)
    no_of_words = 0
    no_of_chars = 0
    for line in lines:
        no_of_words += line.count(' ') + 1 # counting whitespace between words and add 1 for each line.
        no_of_chars += len(line)
    print(f' number of lines: {no_of_line} \n no_of words: {no_of_words}\n no_of_chars: {no_of_chars}')

if __name__ == '__main__':
    word_counter('file.txt')
