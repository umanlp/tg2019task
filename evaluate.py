#!/usr/bin/env python3

import math
import sys
import warnings
from collections import namedtuple, OrderedDict

import pandas as pd

class ListShouldBeEmptyWarning(UserWarning):
    pass

Question = namedtuple('Question', 'id explanations')
Explanation = namedtuple('Explanation', 'id role')


def load_gold(filepath_or_buffer, sep='\t'):
    df = pd.read_csv(filepath_or_buffer, sep=sep)

    gold = OrderedDict()

    for _, row in df[['questionID', 'explanation']].dropna().iterrows():
        explanations = OrderedDict((uid, Explanation(uid, role))
                                   for e in row['explanation'].split()
                                   for uid, role in (e.split('|', 1),))

        question = Question(row['questionID'], explanations)

        gold[question.id] = question

    return gold


def load_pred(filepath_or_buffer, sep='\t'):
    df = pd.read_csv(filepath_or_buffer, sep=sep, names=('question', 'explanation'))

    pred = OrderedDict()

    for question_id, df_explanations in df.groupby('question'):
        pred[question_id] = list(df_explanations['explanation'])

    return pred


def compute_ranks(true, pred):
    ranks = []

    if not true or not pred:
        return ranks

    targets = list(true)

    # I do not understand the corresponding block of the original Scala code.
    for i, pred_id in enumerate(pred):
        for true_id in targets:
            if pred_id == true_id:
                ranks.append(i + 1)
                targets.remove(pred_id)
                break

    # Example: Mercury_SC_416133
    if targets:
        warnings.warn('targets list should be empty, but it contains: ' + ', '.join(targets), ListShouldBeEmptyWarning)

        for _ in targets:
            ranks.append(0)

    return ranks


def average_precision(ranks):
    total = 0.

    if not ranks:
        return total

    for i, rank in enumerate(ranks):
        precision = float(i + 1) / float(rank) if rank > 0 else math.inf
        total += precision

    return total / len(ranks)


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--gold', type=argparse.FileType('r', encoding='UTF-8'), required=True)
    parser.add_argument('pred', type=argparse.FileType('r', encoding='UTF-8'))
    args = parser.parse_args()

    gold, pred = load_gold(args.gold), load_pred(args.pred)

    total, count = 0., 0

    for question in gold.values():
        if question.id in pred:
            ranks = compute_ranks(list(question.explanations), pred[question.id])

            score = average_precision(ranks)

            if math.isfinite(score):
                total += score
                count += 1

            print(question.id, score, file=sys.stderr)

    mean_ap = total / count if count > 0 else 0.

    print('Total: ', mean_ap)


if '__main__' == __name__:
    main()
