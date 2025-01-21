---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:3012496
- loss:MatryoshkaLoss
- loss:MultipleNegativesRankingLoss
base_model: sentence-transformers/static-retrieval-mrl-en-v1
widget:
- source_sentence: what is the difference between body spray and eau de toilette?
  sentences:
  - Eau de Toilette (EDT) is ideal for those that may find the EDP or Perfume oil
    too strong, with 7%-12% fragrance concentration in alcohol. Gives four to five
    hours wear. Body Mist is a light refreshing fragrance perfect for layering with
    other products from the same family. 3-5% fragrance concentration in alcohol.
  - Apples, watermelon, and grapes are all high in a type of sugar called fructose.
    Many people have a fructose intolerance or sensitivity, meaning their body has
    a hard time digesting this sugar. The result? “One of the biggest symptoms is
    diarrhea, but you can also have gas and abdominal pain,” Gans says.
  - Fermentation recycles NAD+, and produces 2 ATPs. In lactic acid fermentation,
    pyruvate from glycolysis changes to lactic acid. ... In alcoholic fermentation,
    pyruvate changes to alcohol and carbon dioxide. This type of fermentation is carried
    out by yeasts and some bacteria.
- source_sentence: how many points do you need to get a free movie at redbox?
  sentences:
  - 'Points needed to redeem rewards with Redbox Perks: 1,500 points = FREE 1-night
    DVD rental. 1,750 points = FREE Blu-ray rental. 2,500 points = FREE 1-night Game
    rental.'
  - Typical High School Grades You will need exceptionally good grades to get into
    Stanford University. The average high school GPA of the admitted freshman class
    at Stanford University was 4.18 on the 4.0 scale indicating that primarily A students
    are accepted and ultimately attend.
  - About This Article. To calculate percentages, start by writing the number you
    want to turn into a percentage over the total value so you end up with a fraction.
    Then, turn the fraction into a decimal by dividing the top number by the bottom
    number. Finally, multiply the decimal by 100 to find the percentage.
- source_sentence: what asvab score for army?
  sentences:
  - To join the Army as an enlisted member you must usually take the Armed Services
    Vocational Aptitude Battery (ASVAB) test and get a good score. The maximum ASVAB
    score is 99. For enlistment into the Army you must get a minimum ASVAB score of
    31.
  - Exons are termed as nucleic acid sequences represented in the RNA molecule. Introns
    are the nucleotide sequences found within the genes that are removed through RNA
    splicing. In other words, exons are coding areas, whereas, introns are non-coding
    areas.
  - American Airlines' ConciergeKey (often misspelled as “Concierge Key”) status is
    the coveted holy grail for any AA flyer. It is the top tier in their AAdvantage
    program, given only to those who truly spend more money than almost any consumer.
- source_sentence: what are the health risks associated with black mold?
  sentences:
  - Apple's prices for out-of-warranty iPhone screen repairs vary, but it costs $129
    to get an iPhone 5S screen replaced — Amazon will only charge you $79.99. An iPhone
    7 Plus screen repair will set you back $169 at Apple, but $119.99 at Amazon.
  - The most common black mold symptoms and health effects are associated with a respiratory
    response. Chronic coughing and sneezing, irritation to the eyes, mucus membranes
    of the nose and throat, rashes, chronic fatigue and persistent headaches can all
    be symptomatic of black mold exposure or black mold poisoning.
  - It is used to treat or prevent a lack of these nutrients during pregnancy or due
    to poor diet or certain illnesses. Vitamins, minerals, and fatty acids are important
    building blocks of the body and help keep you in good health. This combination
    product may contain folic acid.
- source_sentence: what is the difference between antibiotics and probiotics?
  sentences:
  - Equilateral triangle. ... In the familiar Euclidean geometry, an equilateral triangle
    is also equiangular; that is, all three internal angles are also congruent to
    each other and are each 60°. It is also a regular polygon, so it is also referred
    to as a regular triangle.
  - In most fast food restaurants, the minimum age requirement for team members stands
    between 14 and 16 years old. Entry-level team member jobs do not typically require
    prior work experience, although employers may prefer candidates with some employment
    experience.
  - Probiotics can help with digestion Without probiotics, antibiotics can sometimes
    wipe out the protective gut bacteria, which is no good for your digestive system.
    Probiotics are thought to directly kill or inhibit the growth of harmful bacteria,
    stopping them from producing toxic substances that can make you ill.
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- cosine_accuracy@1
- cosine_accuracy@3
- cosine_accuracy@5
- cosine_accuracy@10
- cosine_precision@1
- cosine_precision@3
- cosine_precision@5
- cosine_precision@10
- cosine_recall@1
- cosine_recall@3
- cosine_recall@5
- cosine_recall@10
- cosine_ndcg@10
- cosine_mrr@10
- cosine_map@100
model-index:
- name: SentenceTransformer based on sentence-transformers/static-retrieval-mrl-en-v1
  results:
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: NanoClimateFEVER
      type: NanoClimateFEVER
    metrics:
    - type: cosine_accuracy@1
      value: 0.34
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.52
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.6
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.78
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.34
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.19333333333333333
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.14
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.10399999999999998
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.16666666666666663
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.239
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.27899999999999997
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.4196666666666667
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.33823171504825245
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.45530158730158726
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.2698727995787136
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: NanoDBPedia
      type: NanoDBPedia
    metrics:
    - type: cosine_accuracy@1
      value: 0.7
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.84
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.9
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.94
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.7
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.5866666666666666
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.544
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.45199999999999996
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.0804732343549837
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.16047472236902457
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.21798474210348842
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.31433571884014205
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.5681388031303078
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.7853888888888889
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.43341408330155323
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: NanoFEVER
      type: NanoFEVER
    metrics:
    - type: cosine_accuracy@1
      value: 0.46
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.8
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.84
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.94
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.46
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.26666666666666666
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.18
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.09999999999999998
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.4366666666666667
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.7466666666666667
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.8033333333333332
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.9033333333333333
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.6921500788245725
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.639690476190476
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.62054338159709
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: NanoFiQA2018
      type: NanoFiQA2018
    metrics:
    - type: cosine_accuracy@1
      value: 0.28
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.46
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.54
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.64
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.28
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.2
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.16
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.10399999999999998
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.15188888888888888
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.2996031746031746
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.3792936507936508
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.4837936507936508
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.3654196533999851
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.3931269841269841
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.30249270045918686
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: NanoHotpotQA
      type: NanoHotpotQA
    metrics:
    - type: cosine_accuracy@1
      value: 0.64
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.82
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.86
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.96
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.64
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.3733333333333333
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.26
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.14799999999999996
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.32
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.56
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.65
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.74
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.6547177705459605
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.7485238095238096
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.5798287201418006
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: NanoMSMARCO
      type: NanoMSMARCO
    metrics:
    - type: cosine_accuracy@1
      value: 0.18
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.42
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.5
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.66
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.18
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.13999999999999999
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.10000000000000002
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.066
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.18
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.42
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.5
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.66
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.4040678769319761
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.3244682539682539
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.33886403445504565
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: NanoNFCorpus
      type: NanoNFCorpus
    metrics:
    - type: cosine_accuracy@1
      value: 0.42
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.56
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.62
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.72
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.42
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.3733333333333333
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.32
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.244
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.04278202363094378
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.09842444348194118
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.11962677523904507
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.1389182072247147
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.3241949561078219
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.5040793650793652
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.14484993142973004
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: NanoNQ
      type: NanoNQ
    metrics:
    - type: cosine_accuracy@1
      value: 0.24
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.44
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.58
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.7
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.24
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.14666666666666667
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.124
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.07600000000000001
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.24
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.43
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.58
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.69
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.4533881733265689
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.3764047619047619
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.3890004761200936
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: NanoQuoraRetrieval
      type: NanoQuoraRetrieval
    metrics:
    - type: cosine_accuracy@1
      value: 0.8
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.96
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 1.0
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 1.0
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.8
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.38666666666666655
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.24799999999999997
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.12999999999999998
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.7106666666666667
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.9253333333333333
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.9626666666666668
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.9793333333333334
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.895097527564125
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.88
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.8594406482406483
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: NanoSCIDOCS
      type: NanoSCIDOCS
    metrics:
    - type: cosine_accuracy@1
      value: 0.28
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.48
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.54
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.7
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.28
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.22666666666666666
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.188
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.14
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.059666666666666666
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.14166666666666666
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.19466666666666668
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.2886666666666667
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.26425784158945775
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.39979365079365076
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.2048905794855987
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: NanoArguAna
      type: NanoArguAna
    metrics:
    - type: cosine_accuracy@1
      value: 0.1
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.46
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.56
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.74
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.1
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.15333333333333332
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.11200000000000003
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.07400000000000001
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.1
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.46
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.56
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.74
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.4077879341218404
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.3033888888888889
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.31510434322531095
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: NanoSciFact
      type: NanoSciFact
    metrics:
    - type: cosine_accuracy@1
      value: 0.52
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.6
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.62
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.76
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.52
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.20666666666666667
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.132
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.08399999999999999
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.485
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.57
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.595
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.75
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.6112943449013399
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.5836904761904762
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.5685531248445042
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: NanoTouche2020
      type: NanoTouche2020
    metrics:
    - type: cosine_accuracy@1
      value: 0.5714285714285714
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.8979591836734694
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.9795918367346939
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 1.0
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.5714285714285714
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.6054421768707482
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.6244897959183674
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.5326530612244899
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.03980518443040866
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.12364050983083796
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.21026175680869896
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.337763524116533
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.5718722166431826
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.744047619047619
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.4473069639930506
      name: Cosine Map@100
  - task:
      type: nano-beir
      name: Nano BEIR
    dataset:
      name: NanoBEIR mean
      type: NanoBEIR_mean
    metrics:
    - type: cosine_accuracy@1
      value: 0.4254945054945054
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.6352276295133438
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.7030455259026686
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.8107692307692307
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.4254945054945054
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.29682888540031394
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.24096075353218213
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.1734348508634223
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.23181661522860703
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.3980622705347419
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.46552566089319625
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.5727547000750032
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.5038937609334915
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.549069597069597
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.4210893682209482
      name: Cosine Map@100
---

# SentenceTransformer based on sentence-transformers/static-retrieval-mrl-en-v1

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/static-retrieval-mrl-en-v1](https://huggingface.co/sentence-transformers/static-retrieval-mrl-en-v1). It maps sentences & paragraphs to a 1024-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/static-retrieval-mrl-en-v1](https://huggingface.co/sentence-transformers/static-retrieval-mrl-en-v1) <!-- at revision f60985c706f192d45d218078e49e5a8b6f15283a -->
- **Maximum Sequence Length:** inf tokens
- **Output Dimensionality:** 1024 dimensions
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): StaticEmbedding(
    (embedding): EmbeddingBag(30522, 1024, mode='mean')
  )
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'what is the difference between antibiotics and probiotics?',
    'Probiotics can help with digestion Without probiotics, antibiotics can sometimes wipe out the protective gut bacteria, which is no good for your digestive system. Probiotics are thought to directly kill or inhibit the growth of harmful bacteria, stopping them from producing toxic substances that can make you ill.',
    'In most fast food restaurants, the minimum age requirement for team members stands between 14 and 16 years old. Entry-level team member jobs do not typically require prior work experience, although employers may prefer candidates with some employment experience.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 1024]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities.shape)
# [3, 3]
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Information Retrieval

* Datasets: `NanoClimateFEVER`, `NanoDBPedia`, `NanoFEVER`, `NanoFiQA2018`, `NanoHotpotQA`, `NanoMSMARCO`, `NanoNFCorpus`, `NanoNQ`, `NanoQuoraRetrieval`, `NanoSCIDOCS`, `NanoArguAna`, `NanoSciFact` and `NanoTouche2020`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator)

| Metric              | NanoClimateFEVER | NanoDBPedia | NanoFEVER  | NanoFiQA2018 | NanoHotpotQA | NanoMSMARCO | NanoNFCorpus | NanoNQ     | NanoQuoraRetrieval | NanoSCIDOCS | NanoArguAna | NanoSciFact | NanoTouche2020 |
|:--------------------|:-----------------|:------------|:-----------|:-------------|:-------------|:------------|:-------------|:-----------|:-------------------|:------------|:------------|:------------|:---------------|
| cosine_accuracy@1   | 0.34             | 0.7         | 0.46       | 0.28         | 0.64         | 0.18        | 0.42         | 0.24       | 0.8                | 0.28        | 0.1         | 0.52        | 0.5714         |
| cosine_accuracy@3   | 0.52             | 0.84        | 0.8        | 0.46         | 0.82         | 0.42        | 0.56         | 0.44       | 0.96               | 0.48        | 0.46        | 0.6         | 0.898          |
| cosine_accuracy@5   | 0.6              | 0.9         | 0.84       | 0.54         | 0.86         | 0.5         | 0.62         | 0.58       | 1.0                | 0.54        | 0.56        | 0.62        | 0.9796         |
| cosine_accuracy@10  | 0.78             | 0.94        | 0.94       | 0.64         | 0.96         | 0.66        | 0.72         | 0.7        | 1.0                | 0.7         | 0.74        | 0.76        | 1.0            |
| cosine_precision@1  | 0.34             | 0.7         | 0.46       | 0.28         | 0.64         | 0.18        | 0.42         | 0.24       | 0.8                | 0.28        | 0.1         | 0.52        | 0.5714         |
| cosine_precision@3  | 0.1933           | 0.5867      | 0.2667     | 0.2          | 0.3733       | 0.14        | 0.3733       | 0.1467     | 0.3867             | 0.2267      | 0.1533      | 0.2067      | 0.6054         |
| cosine_precision@5  | 0.14             | 0.544       | 0.18       | 0.16         | 0.26         | 0.1         | 0.32         | 0.124      | 0.248              | 0.188       | 0.112       | 0.132       | 0.6245         |
| cosine_precision@10 | 0.104            | 0.452       | 0.1        | 0.104        | 0.148        | 0.066       | 0.244        | 0.076      | 0.13               | 0.14        | 0.074       | 0.084       | 0.5327         |
| cosine_recall@1     | 0.1667           | 0.0805      | 0.4367     | 0.1519       | 0.32         | 0.18        | 0.0428       | 0.24       | 0.7107             | 0.0597      | 0.1         | 0.485       | 0.0398         |
| cosine_recall@3     | 0.239            | 0.1605      | 0.7467     | 0.2996       | 0.56         | 0.42        | 0.0984       | 0.43       | 0.9253             | 0.1417      | 0.46        | 0.57        | 0.1236         |
| cosine_recall@5     | 0.279            | 0.218       | 0.8033     | 0.3793       | 0.65         | 0.5         | 0.1196       | 0.58       | 0.9627             | 0.1947      | 0.56        | 0.595       | 0.2103         |
| cosine_recall@10    | 0.4197           | 0.3143      | 0.9033     | 0.4838       | 0.74         | 0.66        | 0.1389       | 0.69       | 0.9793             | 0.2887      | 0.74        | 0.75        | 0.3378         |
| **cosine_ndcg@10**  | **0.3382**       | **0.5681**  | **0.6922** | **0.3654**   | **0.6547**   | **0.4041**  | **0.3242**   | **0.4534** | **0.8951**         | **0.2643**  | **0.4078**  | **0.6113**  | **0.5719**     |
| cosine_mrr@10       | 0.4553           | 0.7854      | 0.6397     | 0.3931       | 0.7485       | 0.3245      | 0.5041       | 0.3764     | 0.88               | 0.3998      | 0.3034      | 0.5837      | 0.744          |
| cosine_map@100      | 0.2699           | 0.4334      | 0.6205     | 0.3025       | 0.5798       | 0.3389      | 0.1448       | 0.389      | 0.8594             | 0.2049      | 0.3151      | 0.5686      | 0.4473         |

#### Nano BEIR

* Dataset: `NanoBEIR_mean`
* Evaluated with [<code>NanoBEIREvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.NanoBEIREvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@1   | 0.4255     |
| cosine_accuracy@3   | 0.6352     |
| cosine_accuracy@5   | 0.703      |
| cosine_accuracy@10  | 0.8108     |
| cosine_precision@1  | 0.4255     |
| cosine_precision@3  | 0.2968     |
| cosine_precision@5  | 0.241      |
| cosine_precision@10 | 0.1734     |
| cosine_recall@1     | 0.2318     |
| cosine_recall@3     | 0.3981     |
| cosine_recall@5     | 0.4655     |
| cosine_recall@10    | 0.5728     |
| **cosine_ndcg@10**  | **0.5039** |
| cosine_mrr@10       | 0.5491     |
| cosine_map@100      | 0.4211     |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset


* Size: 3,012,496 training samples
* Columns: <code>sentence_0</code> and <code>sentence_1</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                                    | sentence_1                                                                                       |
  |:--------|:----------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
  | type    | string                                                                                        | string                                                                                           |
  | details | <ul><li>min: 18 characters</li><li>mean: 44.4 characters</li><li>max: 91 characters</li></ul> | <ul><li>min: 55 characters</li><li>mean: 253.35 characters</li><li>max: 378 characters</li></ul> |
* Samples:
  | sentence_0                                         | sentence_1                                                                                                                                                                                                                                                                                                                                      |
  |:---------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>is toprol xl the same as metoprolol?</code>  | <code>Metoprolol succinate is also known by the brand name Toprol XL. It is the extended-release form of metoprolol. Metoprolol succinate is approved to treat high blood pressure, chronic chest pain, and congestive heart failure.</code>                                                                                                    |
  | <code>are you experienced cd steve hoffman?</code> | <code>The Are You Experienced album was apparently mastered from the original stereo UK master tapes (according to Steve Hoffman - one of the very few who has heard both the master tapes and the CDs produced over the years). ... The CD booklets were a little sparse, but at least they stayed true to the album's original design.</code> |
  | <code>how are babushka dolls made?</code>          | <code>Matryoshka dolls are made of wood from lime, balsa, alder, aspen, and birch trees; lime is probably the most common wood type. ... After cutting, the trees are stripped of most of their bark, although a few inner rings of bark are left to bind the wood and keep it from splitting.</code>                                           |
* Loss: [<code>MatryoshkaLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#matryoshkaloss) with these parameters:
  ```json
  {
      "loss": "MultipleNegativesRankingLoss",
      "matryoshka_dims": [
          512,
          256
      ],
      "matryoshka_weights": [
          1,
          1
      ],
      "n_dims_per_step": -1
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 256
- `per_device_eval_batch_size`: 256
- `num_train_epochs`: 15
- `fp16`: True
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: no
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 256
- `per_device_eval_batch_size`: 256
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 15
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `use_ipex`: False
- `bf16`: False
- `fp16`: True
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `dispatch_batches`: None
- `split_batches`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: False
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: False
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin

</details>

### Training Logs
| Epoch  | Step  | Training Loss | NanoClimateFEVER_cosine_ndcg@10 | NanoDBPedia_cosine_ndcg@10 | NanoFEVER_cosine_ndcg@10 | NanoFiQA2018_cosine_ndcg@10 | NanoHotpotQA_cosine_ndcg@10 | NanoMSMARCO_cosine_ndcg@10 | NanoNFCorpus_cosine_ndcg@10 | NanoNQ_cosine_ndcg@10 | NanoQuoraRetrieval_cosine_ndcg@10 | NanoSCIDOCS_cosine_ndcg@10 | NanoArguAna_cosine_ndcg@10 | NanoSciFact_cosine_ndcg@10 | NanoTouche2020_cosine_ndcg@10 | NanoBEIR_mean_cosine_ndcg@10 |
|:------:|:-----:|:-------------:|:-------------------------------:|:--------------------------:|:------------------------:|:---------------------------:|:---------------------------:|:--------------------------:|:---------------------------:|:---------------------:|:---------------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-----------------------------:|:----------------------------:|
| 0.0425 | 500   | 0.3904        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.0850 | 1000  | 0.387         | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.1275 | 1500  | 0.3877        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.1700 | 2000  | 0.3866        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.2124 | 2500  | 0.3802        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.2549 | 3000  | 0.3882        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.2974 | 3500  | 0.3857        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.3399 | 4000  | 0.3826        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.3824 | 4500  | 0.3849        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.4249 | 5000  | 0.3832        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.4674 | 5500  | 0.3841        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.5099 | 6000  | 0.3879        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.5523 | 6500  | 0.3849        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.5948 | 7000  | 0.3848        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.6373 | 7500  | 0.3783        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.6798 | 8000  | 0.3861        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.7223 | 8500  | 0.3877        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.7648 | 9000  | 0.3881        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.8073 | 9500  | 0.3871        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.8498 | 10000 | 0.3837        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.8923 | 10500 | 0.3819        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.9347 | 11000 | 0.3819        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 0.9772 | 11500 | 0.3861        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.0    | 11768 | -             | 0.3382                          | 0.5681                     | 0.6922                   | 0.3654                      | 0.6547                      | 0.4041                     | 0.3242                      | 0.4534                | 0.8951                            | 0.2643                     | 0.4078                     | 0.6111                     | 0.5704                        | 0.5038                       |
| 1.0197 | 12000 | 0.3856        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.0622 | 12500 | 0.3856        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.1047 | 13000 | 0.3834        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.1472 | 13500 | 0.3845        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.1897 | 14000 | 0.3817        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.2322 | 14500 | 0.3874        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.2746 | 15000 | 0.3812        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.3171 | 15500 | 0.3812        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.3596 | 16000 | 0.3814        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.4021 | 16500 | 0.3811        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.4446 | 17000 | 0.3812        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.4871 | 17500 | 0.3823        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.5296 | 18000 | 0.3855        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.5721 | 18500 | 0.3823        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.6145 | 19000 | 0.3842        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.6570 | 19500 | 0.3843        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.6995 | 20000 | 0.38          | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.7420 | 20500 | 0.3737        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.7845 | 21000 | 0.3775        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.8270 | 21500 | 0.3832        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.8695 | 22000 | 0.3857        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.9120 | 22500 | 0.3858        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.9545 | 23000 | 0.3908        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 1.9969 | 23500 | 0.3852        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.0    | 23536 | -             | 0.3382                          | 0.5681                     | 0.6922                   | 0.3654                      | 0.6547                      | 0.4041                     | 0.3242                      | 0.4534                | 0.8951                            | 0.2643                     | 0.4078                     | 0.6111                     | 0.5704                        | 0.5038                       |
| 2.0394 | 24000 | 0.3815        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.0819 | 24500 | 0.3846        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.1244 | 25000 | 0.3835        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.1669 | 25500 | 0.3802        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.2094 | 26000 | 0.3809        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.2519 | 26500 | 0.3843        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.2944 | 27000 | 0.3835        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.3368 | 27500 | 0.3798        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.3793 | 28000 | 0.3793        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.4218 | 28500 | 0.3736        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.4643 | 29000 | 0.3834        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.5068 | 29500 | 0.3805        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.5493 | 30000 | 0.382         | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.5918 | 30500 | 0.3837        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.6343 | 31000 | 0.3892        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.6768 | 31500 | 0.3837        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.7192 | 32000 | 0.3856        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.7617 | 32500 | 0.3759        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.8042 | 33000 | 0.3826        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.8467 | 33500 | 0.3835        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.8892 | 34000 | 0.3866        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.9317 | 34500 | 0.3796        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 2.9742 | 35000 | 0.3879        | -                               | -                          | -                        | -                           | -                           | -                          | -                           | -                     | -                                 | -                          | -                          | -                          | -                             | -                            |
| 3.0    | 35304 | -             | 0.3382                          | 0.5681                     | 0.6922                   | 0.3654                      | 0.6547                      | 0.4041                     | 0.3242                      | 0.4534                | 0.8951                            | 0.2643                     | 0.4078                     | 0.6113                     | 0.5719                        | 0.5039                       |


### Framework Versions
- Python: 3.12.7
- Sentence Transformers: 3.3.1
- Transformers: 4.48.0
- PyTorch: 2.5.1+cu124
- Accelerate: 1.3.0
- Datasets: 3.2.0
- Tokenizers: 0.21.0

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### MatryoshkaLoss
```bibtex
@misc{kusupati2024matryoshka,
    title={Matryoshka Representation Learning},
    author={Aditya Kusupati and Gantavya Bhatt and Aniket Rege and Matthew Wallingford and Aditya Sinha and Vivek Ramanujan and William Howard-Snyder and Kaifeng Chen and Sham Kakade and Prateek Jain and Ali Farhadi},
    year={2024},
    eprint={2205.13147},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```

#### MultipleNegativesRankingLoss
```bibtex
@misc{henderson2017efficient,
    title={Efficient Natural Language Response Suggestion for Smart Reply},
    author={Matthew Henderson and Rami Al-Rfou and Brian Strope and Yun-hsuan Sung and Laszlo Lukacs and Ruiqi Guo and Sanjiv Kumar and Balint Miklos and Ray Kurzweil},
    year={2017},
    eprint={1705.00652},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->