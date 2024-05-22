from typing import Any
from corpus_utils import Token, Sentence, Corpus


class Tagger:
    # So etwas würde man natürlich nicht machen. Wir lernen abstrakte Klassen, die an dieser Stelle geeigneter wären, später kennen.
    pass


class NounTagger(Tagger):
    def __str__(self) -> str:
        return "NounTagger"

    def tag(self, untagged_sentence: Sentence) -> Sentence:
        return Sentence([Token(token.form, "NOUN") for token in untagged_sentence])

    def __call__(self, untagged_sentence: Sentence):
        return self.tag(untagged_sentence)


class UnigramTagger(Tagger):
    def __str__(self) -> str:
        return "UnigramTagger"
    
    def __call__(self, untagged_sentence: Sentence):
        return self.tag(untagged_sentence)

    def __init__(self) -> None:
        self.trainedData = {}

    def train(self, corpus: Corpus) -> None:
        #{WORT: {TAG1: int, TAG2: int}}
        formTags = {}
        for sentence in corpus:
            for token in sentence:
                if token.form not in formTags.keys():
                    formTags[token.form] = {token.pos_tag: 1}
                    continue
                if token.pos_tag not in formTags[token.form].keys():
                    formTags[token.form][token.pos_tag] = 1
                    continue
                formTags[token.form][token.pos_tag] += 1

        #{WORT: meist genutzesTAG}
        for form in formTags.keys():
            formKeys = list(formTags[form].keys())
            if len(formKeys) == 1:
                self.trainedData[form] = formKeys[0]
            elif len(formKeys) > 1:
                formValues = list(formTags[form].values())
                highestTagOccurance = max(formValues)
                self.trainedData[form] = max(formTags[form], key=formTags[form].get) #assign tag with highest value



    def tag(self, untagged_sentence: Sentence) -> Sentence:
        untagged_sentence = NounTagger().tag(untagged_sentence)
        for token in untagged_sentence:
            trainedDataKeys = list(self.trainedData.keys())
            if token.form in trainedDataKeys:
                token.pos_tag = self.trainedData[token.form]
            else:
                #Idea: Similarity = amount of same occuring characters - length difference
                #Example: s(die, der) = 2 - 0 = 2
                #Example2: s(Alexander, Vater) = 3 - 9 = -6
                similarityValues = {}
                for trainedToken in trainedDataKeys:
                    trainedWordList = list(trainedToken.lower())
                    tagWordList = list(token.form.lower())

                    lengthDiff = abs(len(trainedWordList) - len(tagWordList))
                    sameOccuringChars = 0
                    for char in tagWordList:
                        if char in trainedWordList:
                            sameOccuringChars += 1

                    similarityValue = sameOccuringChars - lengthDiff

                    if self.trainedData[trainedToken] not in list(similarityValues.values()):
                        similarityValues[self.trainedData[trainedToken]] = similarityValue
                    else:
                        similarityValues[self.trainedData[trainedToken]] += similarityValue
                
                highestProbableTag = max(similarityValues, key=similarityValues.get)
                token.pos_tag = highestProbableTag
        return untagged_sentence