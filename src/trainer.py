# -*- coding: utf-8 -*-
from reader import get_documents_with_tags_from
from vector_creator import create_list_of_tagged_vectors
import datetime


# ********************************************************************
#       Main function
# ********************************************************************

def train(model_trainer, feature, morph_analyzer, ngram_affixes,
          path="C:\\Users\\admin\\PycharmProjects\\ner_svm\\data\\devset"):
    """
    :param model_trainer:
    :param feature:
    :param morph_analyzer:
    :param path:
    :return:
    """
    documents = get_documents_with_tags_from(path, morph_analyzer, ngram_affixes)
    prefixes = set([item for document in documents.values() for item in document.get_prefixes()])
    suffixes = set([item for document in documents.values() for item in document.get_suffixes()])
    print('Docs are here for training', datetime.datetime.now())
    list_of_tagged_vectors = create_list_of_tagged_vectors(documents, feature, prefixes, suffixes)
    print('Vectors are created', datetime.datetime.now())
    return model_trainer.train(list_of_tagged_vectors, prefixes, suffixes)
