import string
import numpy as np


def cipher_word(input_word):
    primes = cipher_prime(103)
    alphabet = list(string.ascii_lowercase)
    cipher = dict(zip(alphabet, primes))

    encoded = []
    for letter in input_word:
        encoded.append(cipher.get(letter))
    code = np.prod(encoded)
    return code


def cipher_prime(num):
    """ Returns array prime numbers between 2 to num. """
    primes = []
    for possiblePrime in range(2, num):
        is_prime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                is_prime = False
        if is_prime:
            primes.append(possiblePrime)
    return primes


word = "key"
ciphered = cipher_word(word)
