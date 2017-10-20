# Authorship
### Computational Analysis of Different Authors Writings

When authors write, they use unconscious and consistent stylistic choices and habits in writing, and these vary between authors. It therefore follows that these differences are enough to differentiate between text by different authors. There is a computationally identifiable difference between calculable features of texts written by different authors, such that these differences can be used to identify the author of a text with unknown authorship given texts written by all possible authors of the text with unknown authorship.

This is a project that attempts to guess at the author of a text by calculating numerical features (in the `features` directory) and using classifiers (in the `classifiers` directory).

#### Process

1. Numerical Features for a number of texts with known authors are calculated
2. Classifiers are trained on the features calculated
3. Features are calculated for the text with the unknown author
4. Text with unknown author is classified by trained classifiers
