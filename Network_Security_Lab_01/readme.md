#Network Security - Lab 01
##Cryptographic Hashes
**Objective:** Understand the purpose of hashing algorithms and create a tool that solves a problem using one of them.
**Task:** Create a duplicate finder, which analyzes a given directory and prints a list of identical files that have different names or paths.

**What is a hash function?**
A hash function is any function that can be used to map data of arbitrary size to data of fixed size.
The values returned by a hash function are called hash values, hash codes, hash sums, or simply hashes.

**Hash function properties:**
- Impossible to invert (they imply a 1-way transformation)
- 2 different inputs can't give the same output. You can't modify the input data in such a way that it will have the same message digest.

**Why do we need hashing ?**
- We can use it to compare large amounts of data efficiently
- Use them to store index data
- Use them in cryptographic applications like digital signatures.
- Generate random strings.

In this laboratory work i will use hash functions for finding duplicate records. I will use the **MD5** algorithm which may be less unique but faster than other ones which are more secure and have a less probabilty for collisions.

According to a benchmark called Crypto++ MD5 is 1.6 times faster than SHA-1, 2.3 times faster than SHA-256 and more than 2.5 times faster than SHA-512.

**How my application works:**
1. It finds the list of all the files in a given folder.
2. Finds the duplicates by comparing the hash values
3. Prints the files that have the same hash.


