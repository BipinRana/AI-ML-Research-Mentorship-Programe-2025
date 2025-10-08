def is_even_odd(n):
    if n%2==0:
        print(f'{n} is even')
    else:
        print(f'{n} is odd')

is_even_odd(7)

#write a function that takes a string and returns the first string

def first_vowel(name):
    for letter in name:
        if letter.lower() in 'aeiou':
            return letter
    return "There was no vowel"

print(first_vowel("Hello World"))

def first_constant(name):
    for letter in name:
        if letter.lower() not in 'aeiou':
            return letter
    return "There was no consonant"

print(first_constant("Hello World"))

# total number of vowel
# total number of consonant
# total number of vowel, consonant in a string
# returns sum of numbers< by first taking a list of numbers
# return first alphabet
# return last alphabet
# case swap of the the string
# reverse the string
# true of false // palindrome
#true of false // palindrome (case sensetive)

def total_number_of_vowel(name):
    count = 0 
    for letter in name:
        if letter.lower() in 'aeiou':
            count += 1
    return count

def total_number_of_consonant(name):
    count = 0 
    for letter in name:
        if letter.lower() not in 'aeiou':
            count+=1
    return count

def total_number_of_consonant_vowel(name):
    count = 0 
    for letter in name:
        if letter.lower() in 'aeiou':
            count+=1
    return len(name.replace(" ",""))-count,count


def sum_of_numbers(*args):
    sum=0
    for num in args:
        sum+=num
    return sum
    #return sum(args)


print(sum_of_numbers(1,2,3,4,5,6,7,8,9,10))

def first_alphabet(name):
    for letter in name:
        if letter.isalpha():
            return letter
        
def last_alphabet(name):
    for letter in name[::-1]:
        if letter.isalpha():
            return letter
        
print(last_alphabet('1234abcd1234'))

def case_swap(name):
    return name.swapcase()

print(case_swap('hElLo'))

def reverse_string(name):
    return name[::-1]

def check_palindrome_case_sensitive(name):
    return name== name[::-1]
    
def check_palindrome_case_insensitive(name):
    return name.lower()== name[::-1].lower()
    
print(check_palindrome_case_sensitive('Mom'))
print(check_palindrome_case_sensitive('Mom'))
print(total_number_of_consonant_vowel('aeiouBCD'))

print (case_swap('Hello World'))
