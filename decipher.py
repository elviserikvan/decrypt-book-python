# This script is intent to get the url hidden
# in the book "The Book of Law.txt"

BOOK_NAME = 'The Book of Law.txt'
BOOK_KEYS_FILENAME = 'book_line_keys.txt'

#
# This class helps to identify the line in the book
#
class ConvertInt:
    def __init__(self, chars):
        self.chars = chars

    
    def convert(self):
        if self.check_convert_two():
            return self.convert_two_chars()
        elif self.check_convert_one():
            return self.convert_one_char()
        else:
            return False

    def check_convert_two(self):
        try:
            num = int(self.chars[:2])
        except ValueError:
            return False

        return True


    def convert_two_chars(self):
        return int(self.chars[:2])


    def check_convert_one(self):
        try:
            num = int(self.chars[:1])
        except ValueError:
            return False

        return True


    def convert_one_char(self):
        return int(self.chars[:1])



# This function tries to read the line keys
keys = list()
def read_line_keys():
    with open(BOOK_KEYS_FILENAME, 'r') as file:
        for line in file:

            # Remove break line from line
            line = line.replace("\n", '')


            if line[:1] == '/':
                keys.append('/')
            else:
                line_keys = line.split(':')
                
                # Convert from string to int
                line_number = ConvertInt(line_keys[1]).convert()
                letter_number = ConvertInt(line_keys[2]).convert() 

                keys.append(( line_number, letter_number ))
            
# Now 'keys' is a list of tuples with keys
read_line_keys()

def decipher_line(keys):

    with open(BOOK_NAME, 'r') as file:
        for line in file:
            num = ConvertInt(line).convert()

            if num is not False and num == keys[0]:
                words = line.split(' ')
                words.pop(0) # Remove the first word witch is usually the line number

                letter_position = keys[1]

                if letter_position < 0:

                    line_number = str(num)
                    if letter_position < -1:
                        return line_number[:1]
                    else:
                        return line_number[1:2]

                else:
                    for word in words:
                        if len(word) < letter_position:
                             letter_position -= len(word)
                        else:
                            minP = letter_position - 1
                            maxP = letter_position 
                            return word[minP:maxP]
                            break



result = ''
for item in keys:
    if item == '/':
        result += item
    else:
        result += decipher_line(item)



print(result)
