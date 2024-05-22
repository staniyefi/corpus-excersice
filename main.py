from corpus_utils import Corpus
from tagger_models import UnigramTagger, NounTagger
from eval_utils import TaggerTester

if __name__ == "__main__":
    train_corpus = Corpus("train.tsv")
    test_corpus = Corpus("test.tsv")

    my_tagger = UnigramTagger()
    my_tagger.train(train_corpus)
    noun_tagger = NounTagger()

    tester = TaggerTester()
    tester.compare_taggers(
        test_corpus, [my_tagger, noun_tagger],
    )


#Tagger: NounTagger
#Accuracy: 0.19476841052982338

#Tagger: SimilarityTagger (different case)
#Accuracy: 0.7140953015661446

#Tagger: SimilarityTagger (all to lower case)
#Accuracy: 0.7155948017327558

#Tagger: Assume NOUN if not known
#Accuracy: 0.7949016994335222

#Tagger: Assume NOM if not known
#Accuracy: 0.6754415194935022