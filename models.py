import os
import pickle
import itertools
from log_helper import LogHelper


class LanguageModelException(Exception):
    pass



class ModelBase(object):
    def __init__(self, logger, message="ModelBase"):
        self.message = message
        self.logger = logger
        self.logger.info("Init Model Base: {0} ".format(message))

    def predict(self, words, top=1):
        self.logger.info("ModelBase predict always the same")
        word = "foo"
        if(len(words) > 0):
            word = words[-1]
        return tuple([word]*top)



# You can add more Models here.

# class MyModel(ModelBase):
#    def __init__(self, logger, message="ProbabilityModel"):
#         super().__init__(logger, message)
#
#    def predict(self, words, top=1):
#        word = "foo"
#        if(len(words) > 0):
#            word = words[0]
#        return tuple([word]*top)

