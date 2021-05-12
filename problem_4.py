# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
import time


def main():
    palindrom = 0
    for i in range(1000, 100, -1):
        for j in range(1000, 100, -1):
            if str(i * j) == str(i * j)[::-1] and i * j > palindrom:
                palindrom = i * j
    print(
        "The largest palindrom of the product of two 3-digit number is %d" % palindrom
    )


start_time = time.time()
main()
print("The runtime was %.2f seconds" % (time.time() - start_time))
