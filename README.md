# 🔐 Password Generator (Python)
___
A simple yet powerful Python-based password generator that creates secure and customizable passwords based on user preferences.
The program ensures strong password practices by enforcing minimum length and character diversity, then evaluates the password strength.

___

## 🚀 Features

* ✅ Choose which character types to include:
  
    * Uppercase letters (A–Z)

    * Lowercase letters (a–z)

    * Numbers (0–9)

    * Special characters (!@#$%^&*…)

* ✅ Ensures at least one character from each selected type
  
* ✅ Enforces a minimum password length of 7
  
* ✅ Randomly shuffles characters for unpredictability

* ✅ Evaluates password strength:

    * Weak
    * Moderate
    * Strong
      
✅ Beginner-friendly, clean Python logic

___

## 🧠 How It Works (Logic Overview)

1. The user selects which character types to include.
2. The program ensures at least one type is selected.
3. One guaranteed character is added for each chosen type.
4. The user enters a password length:
5. Must be ≥ 7
6. Must be ≥ number of selected character types
7. Remaining characters are filled randomly from the allowed pool.
8. The password is shuffled to avoid predictable patterns.
9. The password is displayed along with a strength rating.

This project demonstrates secure password generation using python

___

## 🧪 Example Output

```
Welcome to the Password Generator!
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include special characters? (y/n): y
Enter the desired password length: 10

Your password is: A7k!p2Z@Qe
This is a strong password.

```
___ 

## 🔒 Password Strength Criteria

* Strength	Conditions:

    * Strong:	Length > 12 AND ≥ 3 character types

    * Moderate:	Length ≥ 7 AND ≥ 2 character types

    * Weak:	Meets minimum rules but low diversity

___

## 🛠️ Future Improvements

* Regenerate password option
* Make it a streamlit App

___

## 👤 Author

Abdelkerim | AI and Data Science Student


