Languages
---------

English
=======

| Test                 | System   | Type  | Model    | Dataset test    | Model size | Test time | Tokens/min| Mem. usage | FB1       |
|----------------------|----------|-------|----------|-----------------|-----------:|----------:|----------:|-----------:|----------:|
| en-elmo              | AllanNLP | NNs   | --       | ConLL 2003 test |     MB     | 34 mins   |    1374   | ? 6.0 GB   | ? 91.54%  |
| en-flair             | Flair    | NNs   | ner      | ConLL 2003 test | 413 MB     | 43 mins   |    1086   | ? 1.5 GB   | ^ 92.69%  |
| en-flair-fast        | Flair    | NNs   | ner-fast | ConLL 2003 test | 259 MB     | 14 mins   |    3337   |   0.8 GB   | ^ 92.31%  |
| en-stanford          | Flair    | CRF   | 4class   | ConLL 2003 test |  17 MB     |  4 secs   |  700830   |   0.5 GB   |   88.83%  |

^nondeterministic


Polish
======

| Test                 | System | Type  | Model    | Dataset test    | Model size | Test time | Tokens/min | Mem. usage | FB1       |
|----------------------|--------|-------|----------|-----------------|------------|-----------|-----------:|------------|-----------|
| pl-applica-poleval18 | Flair  | NNs   | --       | PolEval 2018    |  3276 MB   |  123 mins |      4394  | 6.8 GB     |  84.3%    |
| pl-liner2-poleval18  | Liner2 | CRF   | --       | PolEval 2018    |   440 MB   |    3 mins |    180181  | 1.0 GB     |  77.8%    |
| pl-liner2-top9       | Liner2 | CRF   | top9     | KPWr test       |       MB   |      mins |            | 1.0 GB     |           |


Datasets
-------- 
 
| Dataset          | Classes             | Nested |  Tokens |
|:-----------------|:--------------------|--------|---------|
| ConLL 2003       | LOC, MISC, ORG, PER | No     |  46 722 |
| PolEval 2018 NER |                     | Yes    | 540 545 |
| KPWr test top9   |                     | No     |         |
