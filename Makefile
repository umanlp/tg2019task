WORLDTREE := worldtree_corpus_textgraphs2019sharedtask_withgraphvis

predict-tfidf.zip: predict-tfidf.txt
	rm -f $@
	$(eval TMP := $(shell mktemp -d))
	ln -sf $(CURDIR)/$< $(TMP)/predict.txt
	zip -j $@ $(TMP)/predict.txt
	rm -rf $(TMP)

predict-tfidf.txt:
	./baseline_tfidf.py $(WORLDTREE)/annotation/expl-tablestore-export-2017-08-25-230344/tables $(WORLDTREE)/questions/ARC-Elementary+EXPL-Dev.tsv > $@

dataset: worldtree_corpus_textgraphs2019sharedtask_withgraphvis.zip
	unzip -o $<

worldtree_corpus_textgraphs2019sharedtask_withgraphvis.zip: worldtree_corpus.sha256
	@echo 'Please note that this distribution is still subject to the terms set forth in the included license.'
	@echo 'See the full license for specific details: EULA AI2 Mercury Dataset 01012018.docx'
	curl -sL -o "$@" 'http://cognitiveai.org/dist/worldtree_corpus_textgraphs2019sharedtask_withgraphvis.zip'
	sha256sum -c "$<"
