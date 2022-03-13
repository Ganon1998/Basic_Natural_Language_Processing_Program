import re


class SentenceReadingAgent:
    def __init__(self):
        # Initialized at the start of the program
        self.Sentence = ""
        self.tokens = []

        # everything below are arrays serve as boostrapped knowledge for the agent
        self.Pronouns = ["i", "she", "her", "he", "him", "they", "them"]

        self.AUXS = ['can', 'be', 'will', 'would', 'have', 'could', 'do', 'may', 'be', 'must', 'should', 'might']


        self.ADPS = ['above', 'across', 'against', 'along', 'among', 'around', 'at', 'before', 'behind', 'below',
                     'beneath', 'beside', 'between', 'by', 'down', 'from', 'in', 'into', 'near', 'of', 'off',
                     'on', 'to', 'toward', 'under', 'upon', 'with' 'within']

        self.ADVS = ['out', 'up', 'about', 'then', 'there', 'so', 'down', 'now', 'back', 'very', 'just', 'much', 'too',
                     'well', 'also', 'even',
                     'here', 'kind', 'off', 'again', 'still', 'never', 'far', 'together', 'often', 'always', 'once',
                     'sure', 'ever', 'soon', 'well', 'early', 'fast', 'ago', 'perhaps', 'yet']

        self.NOUNS = ['word', 'time', 'thing', 'day', 'sound', 'number', 'water', 'call', 'all', 'people', 'side',
                      'work', 'part', 'place', 'man', 'year', 'under', 'name', 'think', 'line', 'turn', 'mean', 'move',
                      'boy',
                      'sentence', 'want', 'air', 'end', 'hand', 'port', 'spell', 'land', 'follow', 'act', 'man',
                      'change', 'house', 'picture', 'animal', 'point', 'mother', 'world', 'self', 'mile', 'father', 'head',
                      'page',
                      'country', 'answer', 'school', 'grow', 'study', 'plant', 'cover', 'food', 'thought', 'eye',
                      'door', 'city', 'tree', 'cross', 'start', 'story', 'sea', 'draw', 'run', 'press', 'night', 'life',
                      'child', 'children', 'example', 'ease', 'paper', 'letter', 'river', 'car', 'foot', 'group', 'carry', 'rain',
                      'eat', 'room', 'friend', 'idea', 'fish', 'mountain', 'north', 'base', 'horse',
                      'cut', 'color', 'wood', 'girl', 'list', 'talk', 'bird', 'body', 'dog', 'family', 'pose',
                      'measure', 'state', 'product', 'class', 'wind', 'question', 'ship', 'area', 'rock',
                      'order', 'fire', 'problem', 'piece', 'farm', 'top', 'king', 'size', 'hour', 'am', 'step',
                      'ground', 'interest', 'sing', 'table', 'travel', 'morning', 'vowel', 'war', 'pattern',
                      'center', 'love', 'person', 'money', 'road', 'map', 'science', 'rule', 'govern', 'notice',
                      'voice', 'fall', 'power', 'town', 'fly', 'unit', 'machine', 'note', 'plan', 'figure', 'field',
                      'rest', 'pound', 'beauty', 'drive', 'teach', 'week', 'sleep', 'minute', 'mind', 'tail', 'fact',
                      'street', 'inch', 'lot', 'course', 'wheel', 'force', 'object', 'decide', 'surface',
                      'moon', 'island', 'foot', 'test', 'record', 'boat', 'plane', 'age', 'wonder', 'laugh', 'check', 'east',
                      'game', 'shape', 'heat', 'snow', 'bed', 'weight', 'language', 'today', 'adult', 'adults', 'him', 'her', 'home', 'us',
                      'men', 'book']

        self.VERBS = ['is', 'be', 'have', 'walk', 'have', 'use', 'say', 'do', 'way', 'write', 'written', 'make', 'see', 'look',
                      'go', 'come', 'know', 'find', 'take', 'get', 'make', 'come',
                      'show', 'give', 'form', 'say', 'help', 'cause', 'differ', 'tell', 'set', 'play', 'put', 'read',
                      'add', 'ask', 'go', 'need', 'try', 'stand',
                      'find', 'learn', 'let', 'keep', 'see', 'leave', 'stop', 'seem', 'begin', 'get', 'music', 'care',
                      'take', 'begin', 'hear', 'watch', 'face',
                      'feel', 'leave', 'happen', 'tell', 'know', 'hear', 'remember', 'hold', 'reach', 'listen', 'lie',
                      'serve', 'appear', 'pull', 'lead', 'came', 'come'
                      'cry', 'wait', 'bring', 'brought', 'did', 'does', 'stand', 'contain', 'give', 'develop',
                      'produce', 'stay', 'run', 'sit', 'fill', 'made', 'saw', 'told', 'was']

        self.ADJS = ['hot', 'other', 'many', 'long', 'more', 'most', 'first', 'new', 'live', 'little', 'only', 'round',
                     'good', 'great', 'low', 'same', 'right', 'old', 'small', 'large', 'big', 'high',
                     'such', 'light', 'own', 'last', 'hard', 'late', 'close', 'real', 'few', 'open', 'next', 'white',
                     'second', 'main', 'enough', 'plain', 'usual', 'young', 'ready', 'red', 'direct', 'black', 'short',
                     'numeral', 'complete', 'half', 'whole', 'good', 'true', 'west', 'less', 'simple', 'several',
                     'slow', 'cold', 'fine', 'certain', 'dark', 'correct', 'able', 'front', 'final', 'green', 'quick',
                     'warm',
                     'free', 'strong', 'special', 'clear', 'full', 'blue', 'deep', 'busy', 'common', 'gold', 'possible',
                     'dry', 'cool', 'yellow', 'best']

        self.NAMES = ["Serena", "Andrew", "Bobbie", "Cason", "David", "Farzana", "Frank",
                      "Hannah", "Ida", "Irene", "Jim", "Jose", "Keith", "Laura", "Lucy",
                      "Meredith", "Nick", "Ada", "Yeeling", "Yan", "Red", "She", "He"]

        self.NUMBER = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'hundred', 'thousand']

        self.TIMES = ['today', 'soon', 'day', 'yesterday', 'tomorrow']




    # answers questions pertaining to how
    def HowQuestion(self, QToken, semantic_structure):
        question_structure = {'AGENTS': [], 'ADV': [], 'VERB': [], 'AUX': [], 'ADJ': [], 'ADP': [], 'NOUN': [],
                            'TIME': []}

        # parses question
        for i in range(1, len(QToken)):
            if QToken[i] in semantic_structure['AGENTS']:
                question_structure['AGENTS'].append(QToken[i])
            elif QToken[i] in self.VERBS:
                question_structure['VERB'].append(QToken[i])
            elif QToken[i] in self.NOUNS:
                question_structure['NOUN'].append(QToken[i])
            elif QToken[i] in self.ADJS:
                question_structure['ADJ'].append(QToken[i])
            elif QToken[i] in self.AUXS:
                question_structure['AUX'].append(QToken[i])
            elif QToken[i] in self.ADPS:
                question_structure['ADP'].append(QToken[i])
            elif QToken[i] in self.ADVS:
                question_structure['ADV'].append(QToken[i])

        # if the how is asking about an adjective of a noun
        if len(question_structure['ADJ']) > 0 and len(question_structure['AGENTS']) == 0 and len(
                    question_structure['NOUN']) > 0:
            for i in range(len(semantic_structure['NOUN'])):
                if semantic_structure['NOUN'][i] in question_structure['NOUN']:
                    if i >= len(semantic_structure['ADJ']):
                        return semantic_structure['ADJ'][-1]
                    else:
                        return semantic_structure['ADJ'][i]

        # if the how is asking about an adjective of an agent
        if len(question_structure['ADJ']) > 0 and len(question_structure['AGENTS']) > 0:
            for i in range(len(semantic_structure['AGENTS'])):
                if semantic_structure['AGENTS'][i] in question_structure['AGENTS']:
                    if i >= len(semantic_structure['ADJ']):
                        return semantic_structure['ADJ'][-1]
                    else:
                        return semantic_structure['ADJ'][i]

        # this one asks for an adjective verb of an agent
        if len(semantic_structure['ADJ']) > 0 and len(question_structure['AGENTS']) > 0 and len(
                semantic_structure['VERB']) > 0 and len(semantic_structure['NOUN']) > 0:
            for i in range(len(semantic_structure['AGENTS'])):
                if question_structure['AGENTS'][i] in semantic_structure['AGENTS']:
                    if i >= len(semantic_structure['VERB']):
                        return semantic_structure['VERB'][-1]
                    else:
                        return semantic_structure['VERB'][i]

        # if how is asking about how much/many someone did an action
        if len(question_structure['ADJ']) > 0 and len(question_structure['AGENTS']) > 0 and len(
                semantic_structure['VERB']) > 0 and len(semantic_structure['NOUN']) > 0:
            for i in range(len(semantic_structure['AGENTS'])):
                if question_structure['AGENTS'][i] in semantic_structure['AGENTS']:
                    if i >= len(semantic_structure['VERB']):
                        return semantic_structure['VERB'][-1]
                    else:
                        return semantic_structure['VERB'][i]


        # if how is asking about how much/many someone did WITHOUT ADJ
        if len(question_structure['ADJ']) == 0 and len(question_structure['AGENTS']) == 0 and len(
                semantic_structure['VERB']) > 0 and len(semantic_structure['NOUN']) > 0:
            for token in semantic_structure['NOUN']:
                if token not in question_structure['NOUN']:
                    return token


        # this does the same but is more niche. Attaches verb to noun
        if len(question_structure['ADV']) > 0 and len(question_structure['AGENTS']) > 0 and len(
                semantic_structure['VERB']) > 0 and len(semantic_structure['NOUN']) > 0:
            for i in range(len(semantic_structure['VERB'])):
                if semantic_structure['VERB'][i] in question_structure['VERB']:
                    if i >= len(semantic_structure['NOUN']):
                        return semantic_structure['NOUN'][-1]
                    else:
                        return semantic_structure['NOUN'][i]

        # how someone performs something, find the verb
        if len(question_structure['VERB']) > 0 and len(question_structure['NOUN']) > 0:
            for token in semantic_structure['VERB']:
                if token not in question_structure['VERB']:
                    return token

        # if how is asking about how much/many someone did for numbers
        if len(semantic_structure['NUMBER']) > 0 and len(question_structure['AGENTS']) == 0 and len(
                semantic_structure['VERB']) == 0 and len(semantic_structure['NOUN']) > 0:
            return semantic_structure['NUMBER'][-1]



    # What questions are solved here
    def WhenQuestion(self, QToken, semantic_structure):
        question_structure = {'AGENTS': [], 'ADV': [], 'VERB': [], 'AUX': [], 'ADJ': [], 'ADP': [], 'NOUN': [],
                              'TIME': []}

        # parse question
        for i in range(1, len(QToken)):
            if QToken[i] in semantic_structure['AGENTS']:
                question_structure['AGENTS'].append(QToken[i])
            elif QToken[i] in self.VERBS:
                question_structure['VERB'].append(QToken[i])
            elif QToken[i] in self.NOUNS:
                question_structure['NOUN'].append(QToken[i])
            elif QToken[i] in self.ADJS:
                question_structure['ADJ'].append(QToken[i])
            elif QToken[i] in self.AUXS:
                question_structure['AUX'].append(QToken[i])
            elif QToken[i] in self.ADPS:
                question_structure['ADP'].append(QToken[i])

        # if it asks for a time for when someone went to a noun
        if len(semantic_structure['NOUN']) > 0 and len(semantic_structure['TIME'] > 0):
            for i in range(len(semantic_structure['NOUN'])):
                if semantic_structure['NOUN'][i] in question_structure['NOUN']:
                    if i >= len(semantic_structure['TIME']):
                        return semantic_structure['TIME'][-1]
                    else:
                        return semantic_structure['TIME'][i]

        # a particular day or time
        if len(semantic_structure['TIME']) > 0 and len(semantic_structure['TIME']) == len(question_structure['NOUN']):
            return semantic_structure['TIME'][-1]




    # Where questions
    def WhereQuestion(self, QToken, semantic_structure):
        question_structure = {'AGENTS': [], 'ADV': [], 'VERB': [], 'AUX': [], 'ADJ': [], 'ADP': [], 'NOUN': [],
                              'TIME': []}

        # parse question
        for i in range(1, len(QToken)):
            if QToken[i] in semantic_structure['AGENTS']:
                question_structure['AGENTS'].append(QToken[i])
            elif QToken[i] in self.VERBS:
                question_structure['VERB'].append(QToken[i])
            elif QToken[i] in self.NOUNS:
                question_structure['NOUN'].append(QToken[i])
            elif QToken[i] in self.ADJS:
                question_structure['ADJ'].append(QToken[i])
            elif QToken[i] in self.AUXS:
                question_structure['AUX'].append(QToken[i])
            elif QToken[i] in self.ADPS:
                question_structure['ADP'].append(QToken[i])


        # pull up most recent location: matches verb location with the noun
        if len(question_structure['VERB']) > 0 and len(semantic_structure['NOUN']) > 0 and len(
                question_structure['AGENTS']) > 0:
            if len(question_structure['VERB']) - 1 >= 0:
                return semantic_structure['NOUN'][len(question_structure['VERB']) - 1]
            else:
                return semantic_structure['NOUN'][-1]

        # if the where location doesn't have a verb associated with it and there's no agents
        ################### before len(VERB) == 0
        if len(question_structure['VERB']) > 0 and len(question_structure['NOUN']) > 0 and len(semantic_structure['AGENTS']) == 0:
            for token in semantic_structure['NOUN']:
                if token not in question_structure['NOUN']:
                    return token

        # if its asking about a noun's location
        if len(question_structure['VERB']) > 0 and len(semantic_structure['NOUN']) > 0 and len(
                question_structure['AGENTS']) == 0:
            if len(question_structure['VERB']) - 1 >= 0:
                return semantic_structure['NOUN'][len(question_structure['VERB']) - 1]
            else:
                return semantic_structure['NOUN'][-1]


        # where a noun's location is
        if len(semantic_structure['ADP']) > 0 and len(question_structure['NOUN']) > 0 and len(semantic_structure['AGENTS']) == 0:
            for token in semantic_structure['NOUN']:
                if token not in question_structure['NOUN']:
                    return token




    # answers what questions
    def WhatQuestion(self, QToken, semantic_structure):
        question_structure = {'AGENTS': [], 'ADV': [], 'VERB': [], 'AUX': [], 'ADJ': [], 'ADP': [], 'NOUN': [],
                              'TIME': []}
        # parse questions
        for i in range(1, len(QToken)):
            if QToken[i] in semantic_structure['AGENTS']:
                question_structure['AGENTS'].append(QToken[i])
            elif QToken[i] in self.VERBS:
                question_structure['VERB'].append(QToken[i])
            elif QToken[i] in self.NOUNS:
                question_structure['NOUN'].append(QToken[i])
            elif QToken[i] in self.ADJS:
                question_structure['ADJ'].append(QToken[i])
            elif QToken[i] in self.AUXS:
                question_structure['AUX'].append(QToken[i])
            elif QToken[i] in self.ADPS:
                question_structure['ADP'].append(QToken[i])
            elif QToken[i] == 'she' or QToken[i] == 'he':
                question_structure['AGENTS'].append(QToken[i])


        # what will the agent do
        if 'do' in question_structure['VERB'] and len(semantic_structure['AGENTS']) > 0 and 'time' not in question_structure['NOUN']:
            return semantic_structure['VERB'][-1]

        # what color
        if 'color' in question_structure['NOUN']:
            if len(semantic_structure['ADJ']) >= 1:
                # gets matching noun index with matching adjective index
                for i in range(len(semantic_structure['NOUN'])):
                    if semantic_structure['NOUN'][i] in question_structure['NOUN'] and semantic_structure['NOUN'][i] != 'color':
                        if i >= len(semantic_structure['ADJ']):
                            return semantic_structure['ADJ'][-1]
                        else:
                            return semantic_structure['ADJ'][i]
            else:
                return semantic_structure['ADJ'][-1]


        # asks name of noun
        if 'name' in question_structure['NOUN'] and len(semantic_structure['AGENTS']) > 0:
            return semantic_structure['AGENTS'][-1]


        # if a specific date or time is mentioned
        if len(semantic_structure['TIME']) > 0 and len(semantic_structure['TIME']) == len(question_structure['NOUN']):
            return semantic_structure['TIME'][-1]

        # WHAT asks about an item an agent did with. It finds a matching index of the verb and ties it to the object (noun)
        if len(question_structure['VERB']) > 0 and len(question_structure['AGENTS']) > 0 and len(
                semantic_structure['NOUN']) > 0:
            for token in semantic_structure['NOUN']:
                if token not in question_structure['NOUN']:
                    return token

        # If what asks about an adjective of a noun and not an agent
        if len(question_structure['ADJ']) > 0 and len(semantic_structure['ADJ']) > 0 and len(semantic_structure['AGENTS']) == 0 and len(semantic_structure['NOUN']) > 0:
            for i in range(len(semantic_structure['ADJ'])):
                if semantic_structure['ADJ'][i] in question_structure['ADJ']:
                    if i >= len(semantic_structure['NOUN']):
                        return semantic_structure['NOUN'][-1]
                    else:
                        return semantic_structure['NOUN'][i]

        # if the question has > 1 noun involved implying it's looking for an ADJ but it asks with a noun
        # no verbs are here either
        if len(question_structure['ADJ']) == 0 and len(semantic_structure['ADJ']) > 0 and len(question_structure['NOUN']) > 0 and len(semantic_structure['VERB']) == 0:
            for i in range(len(semantic_structure['NOUN'])):
                if semantic_structure['NOUN'][i] in question_structure['NOUN']:
                    if i >= len(semantic_structure['ADJ']):
                        return semantic_structure['ADJ'][-1]
                    else:
                        return semantic_structure['ADJ'][i]


        ##### these next ones are the same but pertain to an agent #####
        ################################################################

        # If what asks about an adjective of a noun and not an agent
        if len(question_structure['ADJ']) > 0 and len(semantic_structure['ADJ']) > 0 and len(semantic_structure['AGENTS']) > 0:
            for i in range(len(semantic_structure['ADJ'])):
                if semantic_structure['ADJ'][i] in question_structure['ADJ']:
                    if i >= len(semantic_structure['AGENTS']):
                        return semantic_structure['AGENTS'][-1]
                    else:
                        return semantic_structure['AGENTS'][i]

        # if the question has > 1 noun involved implying it's looking for an ADJ but it asks with a noun
        if len(question_structure['ADJ']) == 0 and len(semantic_structure['ADJ']) > 0 and len(question_structure['AGENTS']) > 0:
            for i in range(len(semantic_structure['AGENTS'])):
                if semantic_structure['AGENTS'][i] in question_structure['AGENTS']:
                    if i >= len(semantic_structure['ADJ']):
                        return semantic_structure['ADJ'][-1]
                    else:
                        return semantic_structure['ADJ'][i]


        # asks what noun is in what
        if len(semantic_structure['ADP']) > 0 and len(semantic_structure['NOUN']) > 0 and len(question_structure['NOUN']) > 0:
            for token in semantic_structure['NOUN']:
                if token not in question_structure['NOUN']:
                    return token

        # niche case: "Watch your step" type questions
        if len(semantic_structure['VERB']) == 1 and len(semantic_structure['NOUN']) == 1 and len(question_structure['NOUN']) == 0:
            return semantic_structure['NOUN'][0]

        # asks about what action was done
        if len(semantic_structure['VERB']) == 1 and len(semantic_structure['NOUN']) >= 1 and len(semantic_structure['AGENTS']) == 0:
            return semantic_structure['VERB'][0]


        # what noun is it?
        if len(semantic_structure['NOUN']) >= len(semantic_structure['VERB']) and len(semantic_structure['VERB']) > 0 and len(semantic_structure['AGENTS']) == 0:
            for token in semantic_structure['NOUN']:
                if token not in question_structure['NOUN']:
                    return token




    # Who question
    def WhoQuestion(self, QToken, semantic_structure):
        question_structure = {'AGENTS': [], 'ADV': [], 'VERB': [], 'AUX': [], 'ADJ': [], 'ADP': [], 'NOUN': [],
                              'TIME': []}

        # parse question
        for i in range(1, len(QToken)):
            if QToken[i] in semantic_structure['AGENTS']:
                question_structure['AGENTS'].append(QToken[i])
            elif QToken[i] in self.VERBS:
                question_structure['VERB'].append(QToken[i])
            elif QToken[i] in self.NOUNS:
                question_structure['NOUN'].append(QToken[i])
            elif QToken[i] in self.ADJS:
                question_structure['ADJ'].append(QToken[i])
            elif QToken[i] in self.AUXS:
                question_structure['AUX'].append(QToken[i])
            elif QToken[i] in self.ADPS or QToken[i] == 'with':
                question_structure['ADP'].append(QToken[i])

        # if there's only 1 agent and it asks about what happened to the noun
        if 'was' in question_structure['VERB'] and len(question_structure['ADP']) == 0:
            if len(semantic_structure['VERB']) == 1 and len(semantic_structure['NOUN']) > 0 and len(semantic_structure['AGENTS']) == 1:
                for token in semantic_structure['NOUN']:
                    if token not in question_structure['NOUN'] and token not in self.Pronouns:
                        return token

        # if the WHO question has a basic structure
        if len(question_structure['VERB']) > 0 and len(semantic_structure['AGENTS']) > 0:
            # get the index of where the verb is found which will correspond with which person did what.
            # for ex: Mike kicked hte ball Jake Punched the ball. Punched will have a verb index of 1 in the semantic break down and so will Jake so Jake is returned
            # this makes sure the verb is assigned appropriately with the agent

            # this checks if the WHO asks who received an action from an agent
            if len(question_structure['AGENTS']) > 0 and len(question_structure['ADP']) > 0:
                for i in range(len(semantic_structure['AGENTS'])):
                    if semantic_structure['AGENTS'][i] not in question_structure['AGENTS']:
                        if i >= len(semantic_structure['AGENTS']):
                            return semantic_structure['AGENTS'][-1]
                        else:
                            return semantic_structure['AGENTS'][i]

            # checks if a noun is acting as an agent "Three men in a car"
            if len(question_structure['NOUN']) > 0 and len(question_structure['ADP']) > 0:
                for i in range(len(semantic_structure['NOUN'])):
                    if semantic_structure['NOUN'][i] not in question_structure['NOUN'] and question_structure['ADP'][i - 1] in semantic_structure['ADP']:
                        if i >= len(semantic_structure['NOUN']):
                            return semantic_structure['NOUN'][-1]
                        else:
                            return semantic_structure['NOUN'][i]

            # checks if an agent is interacting with a noun #################### maybe janky
            if len(semantic_structure['NOUN']) > 0 and len(question_structure['ADP']) > 0:
                for i in range(len(semantic_structure['NOUN'])):
                    if semantic_structure['NOUN'][i] not in question_structure['NOUN']:
                        return semantic_structure['NOUN'][-1]

            else:
                # if the who is on the first agent
                for i in range(len(semantic_structure['VERB'])):
                    if semantic_structure['VERB'][i] in question_structure['VERB'] and question_structure['NOUN'][i] in semantic_structure['NOUN']:
                        if i >= len(semantic_structure['AGENTS']):
                            return semantic_structure['AGENTS'][-1]
                        else:
                            return semantic_structure['AGENTS'][i]

        # who asks about agent activity with another using "with", "behind", etc.
        elif len(question_structure['ADP']) > 0 and len(question_structure['AGENTS']) > 0 and len(question_structure['NOUN']) == 0:
            for token in semantic_structure['AGENTS']:
                if token not in question_structure['AGENTS']:
                    return token

        # if the who is a noun receiving an action
        elif len(semantic_structure['NOUN']) > 0 and len(semantic_structure['VERB']) == len(question_structure['VERB']) and len(question_structure['VERB']) > 0:
            for token in semantic_structure['NOUN']:
                if token not in question_structure['NOUN']:
                    return token


        # who asks about noun activity with another using "with", "behind", etc.
        elif len(question_structure['ADP']) > 0 and len(question_structure['NOUN']) > 0 and len(question_structure['AGENTS']) == 0:
            for token in semantic_structure['NOUN']:
                if token not in question_structure['NOUN']:
                    return token





    def solve(self, sentence, question):

        # the parsed sentence goes into this dicitonary
        semantic_structure = {'AGENTS': [], 'ADV': [], 'VERB': [], 'AUX': [], 'ADJ': [], 'ADP': [], 'NOUN': [],
                              'TIME': [], 'NUMBERS': []}

        # update sentence and tokens if necessary
        if self.Sentence != sentence:
            self.tokens.clear()
            self.Sentence = ""

            new_sentence = sentence[:-1]
            self.Sentence = new_sentence
            self.tokens = new_sentence.split()

        # put tokens of sentence into the semantic_structure table
        for i in range(len(self.tokens)):
            
            # if the token is a time
            if re.compile('^(1[0-2]|0?[1-9]):[0-5][0-9](AM|PM)$').match(self.tokens[i]):
                semantic_structure['TIME'].append(self.tokens[i])

            elif self.tokens[i] in self.TIMES:
                semantic_structure['TIME'].append(self.tokens[i])

            elif self.tokens[i] in self.NAMES or self.tokens[i].lower() in self.NAMES:
                semantic_structure['AGENTS'].append(self.tokens[i])

            elif self.tokens[i] in self.ADVS:
                semantic_structure['ADV'].append(self.tokens[i].lower())

            elif self.tokens[i] in self.AUXS:
                semantic_structure['AUX'].append(self.tokens[i].lower())

            elif self.tokens[i] in self.VERBS or self.tokens[i].lower() in self.VERBS:
                semantic_structure['VERB'].append(self.tokens[i].lower())

            elif self.tokens[i] in self.ADJS:
                semantic_structure['ADJ'].append(self.tokens[i].lower())

            elif self.tokens[i] in self.NUMBER:
                if self.tokens[i].lower() == "one":
                    if self.tokens[i + 1] is not None and self.tokens[i+1] not in self.NUMBER and self.tokens[i+1] not in self.ADVS:
                        semantic_structure['NOUN'].append(self.tokens[i + 1].lower())
                        continue
                    else:
                        semantic_structure['NUMBERS'].append(self.tokens[i].lower())
                else:
                    semantic_structure['NUMBERS'].append(self.tokens[i].lower())


            elif self.tokens[i] in self.ADPS:
                semantic_structure['ADP'].append(self.tokens[i].lower())

            elif self.tokens[i] in self.NOUNS and self.tokens[i] not in semantic_structure['NOUN']:
                semantic_structure['NOUN'].append(self.tokens[i].lower())


        new_question = question[:-1]
        QToken = new_question.split()

        # collect tokens from question and compare them to the semantic_structure to find the answer
        # Who is looking for a noun and or agent
        if QToken[0] == "Who":
            return self.WhoQuestion(QToken=QToken, semantic_structure=semantic_structure)

        # What types of questions
        # What is looking for a noun
        if QToken[0] == "What" or QToken[1] == "what":
            return self.WhatQuestion(QToken=QToken, semantic_structure=semantic_structure)

        # How is looking for a verb or noun
        if QToken[0] == "How":
            return self.HowQuestion(QToken=QToken, semantic_structure=semantic_structure)

        # How is looking for a verb or noun
        if QToken[0] == "When":
            return self.WhenQuestion(QToken=QToken, semantic_structure=semantic_structure)

        if QToken[0] == "Where":
            return self.WhereQuestion(QToken=QToken, semantic_structure=semantic_structure)