# Unigram Tagger and Evaluation

This repository contains the implementation of a Unigram Tagger and its evaluation as part of the "Programmieren II: Fortgeschrittene (Python)" course in the University of Heidelberg. The tasks involve reading text files, training a Unigram Tagger, evaluating it, and addressing method resolution order (MRO) concepts.

## Features

- **Custom Corpus Handling**: Efficiently read and process text data using custom classes.
- **Unigram Tagger Implementation**: Train a Unigram Tagger from scratch, handling unseen words with a basic strategy.
- **Evaluation Framework**: Evaluate the tagger's performance with a custom evaluation method, providing detailed accuracy metrics.
- **Object-Oriented Design**: Utilize classes and methods to structure the code, ensuring maintainability and scalability.

## Project Structure

- `corpus_utils.py`: Defines classes to read and handle the corpus data.
- `tagger_models.py`: Contains the Unigram Tagger implementation.
- `eval_utils.py`: Includes the evaluation logic for the tagger.
- `main.py`: The main script to execute training and evaluation.
- `train.tsv`: Training dataset.
- `test.tsv`: Test dataset.

## Corpus Handling

Implemented in `corpus_utils.py`, the `Corpus`, `Sentence`, and `Token` classes provide:

- **Reading the Corpus**: Load and process the TSV file format.
- **Corpus Statistics**: Methods to get the number of sentences and access specific sentences.
- **Iteration Support**: Iterate through sentences in the corpus seamlessly.

## Unigram Tagger

Implemented in `tagger_models.py`, the `UnigramTagger` class provides:

- **Training**: Train the tagger using the most frequent PoS tags for each word form.
- **Tagging**: Predict PoS tags for new sentences, handling unseen words efficiently.
- **Callable Instances**: Use the tagger instance as a function to tag sentences.

## Evaluation

Implemented in `eval_utils.py`, the `TaggerTester` class provides:

- **Performance Evaluation**: Compare predicted tags with actual tags and calculate accuracy.
- **Detailed Metrics**: Output accuracy and other relevant metrics to assess performance.

## Code Highlights

- **No External Libraries**: The implementation avoids libraries like `collections`, `nltk`, and `pandas`, showcasing pure Python solutions.
- **Modular Design**: Each class and method is designed for reusability and clarity.
- **Error Handling**: Robust error handling for unseen words and other edge cases.