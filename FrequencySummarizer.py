#-*-coding utf-8-*-
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest

class SimpleFrequencySummarizer:
  def __init__(self, min_cut=0.1, max_cut=0.9):
    self._min_cut = min_cut
    self._max_cut = max_cut
    self._stopwords = set(stopwords.words('english') + list(punctuation))

  def _compute_frequencies(self, word_sent):
    """
        Подсчитываем частоту каждого слова
    """
    freq = defaultdict(int)
    for s in word_sent:
      for word in s:
        if word not in self._stopwords:
          freq[word] += 1
    # Частотная нормализация
    """
        Данную формулу можно модифицировать:
            Tf-idf
    """
    m = float(max(freq.values()))

    for w in list(freq):
      freq[w] = freq[w]/m
      if freq[w] >= self._max_cut or freq[w] <= self._min_cut:
        del freq[w]
    return freq

  def summarize(self, text, n):
    """
      Формируем текст из списка предложений
    """
    sents = sent_tokenize(text)
    assert n <= len(sents)
    word_sent = [word_tokenize(s.lower()) for s in sents]
    self._freq = self._compute_frequencies(word_sent)
    ranking = defaultdict(int)
    for i,sent in enumerate(word_sent):
      for w in sent:
        if w in self._freq:
          ranking[i] += self._freq[w]
    sents_idx = self._rank(ranking, n)
    return [sents[j] for j in sents_idx]

  def _rank(self, ranking, n):
    """
        Возвращаем n предложений с наивысшим ранжированием
    """
    return nlargest(n, ranking, key=ranking.get)


