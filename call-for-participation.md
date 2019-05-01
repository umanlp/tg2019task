TextGraphs-13 Shared Task on Explanation Regeneration
=====================================================

Overview
--------
Multi-hop inference is the task of combining more than one piece of information to solve an inference task, such as question answering.  This can take many forms, from combining free-text sentences read from books or the web, to combining linked facts from a structured knowledge base.   

#### The need for multi-hop inference in question answering

Question answering can often be modeled as a retrieval task, answer sentence selection, where a method must find some sentence or short passage of text in a corpus that answers the question.  Unfortunately for complex questions it's unlikely that one can find such answer passages, even in extremely large corpora.  For example, consider the following multiple choice elementary science question:

Q: Which of the following is an example of an organism taking in nutrients?
( A ) a dog burying a bone
( B ) a girl eating an apple (Correct answer)
( C ) an insect crawling on a leaf
( D ) a boy planting tomatoes

For this question, it's highly unlikely that one could find a passage in a corpus that says "a girl eating an apple is an example of an organism taking in nutrients", even if that corpus was extremely large.  Instead, one likely has to combine a number of separate facts to successfully make this inference:
( 1 ) A girl means a human girl.
( 2 ) Humans are living organisms.
( 3 ) Eating is when an organism takes in nutrients in the form of food.
( 4 ) Fruits are kinds of foods.
( 5 ) An apple is a kind of fruit.

Combining each of these facts is often modeled as a graph traversal problem, where one must "hop" from some starting fact (say, fact 1) to other, related facts, until one has enough facts to infer the answer.  This is illustrated below: 

![Example explanation graph](images/example-girl-eating-apple.jpg)

#### The need for explanations

Developing methods of automated inference that are able to provide users with compelling human-readable justifications for why the answer to a question is correct are critical for domains such as science and medicine, where user trust and detecting costly errors are limiting factors to adoption.  Multi-hop inference is attractive for explanation-centered inference, as the path one assembles while traversing a knowledge graph can serve as an explanation for a user.  For example:

Why is 'a girl eating an apple' an example of an organism taking in nutrients?  
Explanation: Because: A girl means a human girl. humans are living organisms.  Eating is when an organism takes in nutrients in the form of food.  Fruits are kinds of foods.  An apple is a kind of fruit.

#### Contemporary Challenges in Multi-hop Inference

**Semantic Drift:** One of the central challenges to performing multi-hop inference is that combining facts -- i.e. traversing from one fact to another in a knowledge graph -- is a noisy process, because the current signals we have for knowing whether two facts are relevant to the inference required to answer a question (and can thus be combined) are imperfect.  Often times those signals are as simple as lexical overlap -- two sentences (or nodes) in a knowledge graph sharing one or more of the same words.  Sometimes this lexical overlap helps -- for example, knowing that "an apple is a kind of [fruit]" and that "[fruits] are foods" helps answer the above question.  But often times it leads to information that isn't on context -- for example, "a [tree] is a kind of living thing" and "[trees] require sunlight to survive" likely wouldn't help answer a question about *"Q: Which adaptations help a tree survive the heat of a forest fire."*

This observation that chaining facts together on imperfect signals often leads inference to go off-context and become errorful is the phenomenon of *"semantic drift"* *(Fried et al., "Higher-order Lexical Semantic Models for Non-factoid Answer Reranking", TACL 2015)*, and has been demonstrated across a wide variety of representations and traversal algorithms.  Typically multi-hop models see small performance benefits (of between 1-5%) when aggregating 2 pieces of information, and may see small performance benefits when aggregating 3 pieces of information, then performance decreases as progressively more information is aggregated due to this "semantic drift".  

**Long Inference Chains:** Jansen et al. *("WorldTree: A Corpus of Explanation Graphs for Elementary Science Questions supporting Multi-hop Inference", LREC 2018)* showed that even inferences for elementary science require aggregating an average of 6 facts (and as many as 16 facts) to answer and explain the reasoning behind those answers when common sense knowledge is included.   With current inference models infrequently able to combine more than 2 facts, the state-of-the-art is far from this requirement.

**Multi-hop methods are not required to answer questions on many "multi-hop" datasets:** Chen and Durrett *("Understanding Dataset Design Choices for Multi-hop Reasoning", NAACL 2019)* show that it's possible to achieve near state-of-the-art performance on two popular multi-hop question answering datasets (WikiHop and HotPotQA) using baseline models that do not perform multi-hop inference.  Because new multi-hop inference algorithms are often characterized using their accuracy on the question answering task as a proxy for their capacity to perform multi-hop inference, rather than explicitly evaluating an algorithm's capacity to aggregate information by controlling the amount of information it can combine (as in Fried et al.),  we currently do not have well-controlled characterizations of the information aggregation abilities of many proposed multi-hop algorithms.

**Chance Performance on Knowledge Graphs:** Jansen *("Multi-hop Inference for Sentence-level TextGraphs: How Challenging is Meaningfully Combining Information for Science Question Answering?", TextGraphs 2018)* empirically demonstrated that semantic drift can be *overpoweringly large* or *deceptively low*, depending on the text resources used to build the knowledge graph, and the criteria used for selecting nodes.  While the chance of hopping to a relevant node on a graph constructed from sentences in an open-domain corpus like Wikipedia can be very small, using a term frequency model can increase this chance performance by orders of magnitude, increasing chance traversal performance beyond the performance of some algorithms reported in the literature.  Unfortunately evaluating the chance performance on a knowledge graph is currently a very expensive manual task, and we currently suffer from a methods problem of being able to disentangle the performance of novel multi-hop algorithms from the chance performance of a given knowledge graph.

**Explicit Training Data for Multi-hop Inference and Explanation Construction:** Because of the difficulty and expense associated with manually annotating inference paths in a knowledge base, most multi-hop inference algorithms have lacked supervision for this task, and had to resort to using other methods (such as latent machine learning algorithms) that use other signals, like answering a question correctly, as a proxy for doing well at the multi-hop inference task. 

#### The Task: Explanation Reconstruction 
Many of these contemporary methodological challenges are potentially now addressable using WorldTree, a new corpus of explicit training data designed to help instrument the multi-hop inference and explanation-construction tasks.  WorldTree contains manually assembled detailed explanations, including common-sense reasoning facts, for nearly every publicly available elementary science exam question.  Explanations are represented as a series of facts that, when combined, answer a question, and provide a detailed explanation for the answer.  Facts in an explanation explicitly connect with each other on lexical overlap -- i.e., having one or more of the same words.  Each fact is drawn from a grade-appropriate knowledge base of approximately 5,000 facts that are simultaneously represented as both free-text sentences and structured knowledge (*n-ary relations*), allowing both structured and unstructured methods to be evaluated on the same data.  Additional annotation identifies which facts are "central" to the explanation, allowing automated evaluation of an inference method's ability to combine "core scientific facts" with common-sense knowledge that grounds core science knowledge with world knowledge. 


Important Dates
---------------

1. __xx-xx-xxxx__: Example (trial) data release
2. __xx-xx-xxxx__: Training data release
3. __xx-xx-xxxx__: Test data release. Evaluation start
4. __xx-xx-xxxx__: Evaluation end
5. __xx-xx-xxxx__: System description paper deadline
6. __xx-xx-xxxx__: Deadline for reviews of system description papers
7. __xx-xx-xxxx__: Author notifications
8. __xx-xx-xxxx__: Camera-ready description paper deadline
9. __11-03-2019/11-04-2019__: TextGraphs-13 workshop


Data
----

The data used in this shared task comes from the WorldTree corpus (Jansen et al., 2018). The data includes TODO: discuss data organization. Include 1 example question, correct/incorrect answers, and explanation for the correct answer. 

Participating systems will be evaluated using TODO: discuss evaluation measure. 

The shared task data distribution includes a baseline that TODO: discuss how the baseline works. The performance of this baseline on the development partition is TODO: summarize the baseline performance. 

## Examples

Simpler
![Example explanation graph](images/example-simpler-insect6legs.png)

List
![Example explanation graph](images/example-list-cloudsfogmadeof.png)

Hard, many-facts
![Example explanation graph](images/example-hard-treesurviveforestfire.png)





Terms and Conditions
--------------------

By submitting results to this competition, you consent to the public release of your scores at the TextGraph-13 workshop and in the associated proceedings, at the task organizers' discretion. Scores may include, but are not limited to, automatic and manual quantitative judgements, qualitative judgements, and such other metrics as the task organizers see fit. You accept that the ultimate decision of metric choice and score value is that of the task organizers.

You further agree that the task organizers are under no obligation to release scores and that scores may be withheld if it is the task organizers' judgement that the submission was incomplete, erroneous, deceptive, or violated the letter or spirit of the competition's rules. Inclusion of a submission's scores is not an endorsement of a team or individual's submission, system, or science.

You further agree that your system may be named according to the team name provided at the time of submission, or to a suitable shorthand as determined by the task organizers.

You agree not to use or redistribute the shared task data except in the manner prescribed by its licence.

References
----------

```
@InProceedings{jansen2018worldtree,
    author = {Peter Jansen and Elizabeth Wainwright and Steven Marmorstein and Clayton T. Morrison},
    title = {WorldTree: A Corpus of Explanation Graphs for Elementary Science Questions supporting Multi-hop Inference},
    booktitle = {Proceedings of the 11th International Conference on Language Resources and Evaluation (LREC)},
    year = {2018},
    url = {http://cognitiveai.org/wp-content/uploads/2018/02/jansen_et_al_lrec2018_worldtree_computable_explanation_corpus_8pg_cameraready.pdf},
    url_code = {http://cognitiveai.org/explanationbank/}
}
```
