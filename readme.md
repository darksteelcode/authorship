# Authorship
### Computational Analysis of Different Authors Writings

When authors write, they use unconscious and consistent stylistic choices and habits in writing, and these vary between authors. It therefore follows that these differences are enough to differentiate between text by different authors. There is a computationally identifiable difference between calculable features of texts written by different authors, such that these differences can be used to identify the author of a text with unknown authorship given texts written by all possible authors of the text with unknown authorship.

This is a project that attempts to guess at the author of a text by calculating numerical features (in the `features` directory) and using classifiers (in the `classifiers` directory).

### Process

1. Features are calculated for writings with know Authorship
2. Classifiers are trained with the calculated features to be able to guess which author wrote something
3. The features of a text with unknown authorship are calculatedData
4. These features are fed into the trained classifier, and the resulting author is the guessed author

### Features
  #### (In `Features` Directory)
