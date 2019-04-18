# TextGraphs-13 Shared Task on Explanation Regeneration

```shell
$ ./evaluate.py --gold=questions/ARC-Elementary-QC+EXPL-Dev.tsv predict.txt
```

The format of the `predict.txt` file is `questionID<TAB>explanationID` without header;
the order is important.

```shell
$ ./baseline_tfidf.py annotation/expl-tablestore-export-2017-08-25-230344/tables questions/ARC-Elementary-QC+EXPL-Dev.tsv
```
