# Wordle_Cheat_Machine

Basic "memory aid" for [Wordle](https://www.powerlanguage.co.uk/wordle/ "Wordle page") daily challenges :)

Word list was extracted from [Mieliestronk's](http://www.mieliestronk.com/wordlist.html) list of english words.

# Usage

Use the function *get_suggestions* with the 3 following arguments:
+ a key of 5 characters using underscores for the unknown letters
+ a string with letters present in the word
+ a string with letters that are not in the word

```python
suggestions = get_suggestions('__ung', 'un', 'adieboschkfl')
```
