class Token:
    def __init__(self, form, pos_tag=None):
        self.form = form
        self.pos_tag = pos_tag

    def __repr__(self):
        return f"Token(form='{self.form}', pos_tag='{self.pos_tag}')"


class Sentence:
    def __init__(self, tokens):
        self.tokens = tokens

    def __repr__(self):
        return f"Sentence({self.tokens})"

    def __len__(self):
        return len(self.tokens)
    
    def __iter__(self):
        return iter(self.tokens)

    def __getitem__(self, index):
        return self.tokens[index]

class Corpus:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.sentence_array = self.getData()

    def __iter__(self):
        return iter(self.sentence_array)
    
    def __len__(self):
        return len(self.sentence_array)
    
    def __getitem__(self, index):
        return self.sentence_array[index]
    
    def getData(self):
        token_array = []
        sentence_array = []

        with open(self.filepath, "r+") as datafile:
            dataArr = datafile.readlines()

        for data in dataArr:
            split_data = data.split('\t')
            
            if data != "\n" and data != "" and data != " ":
                if len(split_data) == 2:
                    token = Token(split_data[0], split_data[1].replace("\n", ""))
                elif len(split_data) == 1:
                    token = Token(split_data[0])
                token_array.append(token)
        
        buffer = []
        for token in token_array:
            if token.form in [".", "!", "!!", "!!!", "?", "??", "???", "!?", "?!", "?!!"]:
                sentence_array.append(buffer)
                buffer = []
                
            buffer.append(token)

        return sentence_array