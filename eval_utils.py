from typing import Iterable

from tagger_models import Tagger
from corpus_utils import Corpus


class TaggerTester:
    def evaluate_tagger(self, corpus: Corpus, tagger: Tagger) -> None:
        # take every sentence in test file
        # collect predictions from tagger
        # compute and print accuracy
        allPred = 0
        rightPred = 0
        wrongPred = 0

        
        for corpusSentence in corpus:
            taggedSentence = tagger(corpusSentence)
            for index, corpusToken in enumerate(corpusSentence):
                if taggedSentence[index].pos_tag == corpusToken.pos_tag:
                    rightPred += 1
                else:
                    wrongPred += 1
                allPred += 1
            
        accuracy = rightPred / allPred
        print(f"Tagger: {str(tagger)}")
        print(f"Accuracy: {accuracy}")

    def compare_taggers(self, corpus: Corpus, taggers: Iterable[Tagger]) -> None:
        for tagger in taggers:
            self.evaluate_tagger(corpus, tagger)
            print("------")
