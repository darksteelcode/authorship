# Authorship
### Computational Analysis of Different Authors Writings

When authors write, they use unconscious and consistent stylistic choices and habits in writing, and these vary between authors. It therefore follows that these differences are enough to differentiate between text by different authors. There is a computationally identifiable difference between calculable features of texts written by different authors, such that these differences can be used to identify the author of a text with unknown authorship given texts written by all possible authors of the text with unknown authorship.

This is a project that attempts to guess at the author of a text by calculating numerical features (in the `features` directory) and using classifiers (in the `classifiers` directory). To run, run `main.py`

### Process

1. Features are calculated for writings with know Authorship
2. Classifiers are trained with the calculated features to be able to guess which author wrote something
3. The features of a text with unknown authorship are calculatedData
4. These features are fed into the trained classifier, and the resulting author is the guessed author

### Features
(In `features` Directory)

#### CommonWords
  This feature calculates the frequency of the thirty most common english words throughout the text

#### Punctuation
  This feature calculates the frequency of a few basic punctuation marks in the text

#### SentenceLength
  This feature calculates the average length, in characters, of sentences in the text

### Texts
(In `texts` Directory)

Texts with known authors are located in sub-directories named for their authors
Texts with unknown authors are located in the `Unknown` sub-directory

#### `AUTHORS.txt`
(`texts/Unknown/AUTHORS.txt`)

This file contains a list of the unknown texts and their "known" authors. This file is not required, nor is a author needed for any unknown text. The only use of this file is to measure accuracy of guesses after they have been made. When the program is applied to actually unknown texts, no author is needed in `AUTHORS.txt`.

Format for `AUTHORS.txt`
File name and author are separated by a `:`, with no whitespace except in the author's name
Example:

```
pickwick_papers.txt:Charles Dickens
return_of_sherlock_holmes.txt:Arthur Conan Doyle
```
