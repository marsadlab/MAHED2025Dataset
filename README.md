# [MAHED2025](https://marsadlab.github.io/mahed2025/) at [ArabicNLP-2025](https://arabicnlp2025.sigarab.org/)

In this edition we offered three tasks (i) hate and hope speech classification, (ii) emotion, offensive, and hate detection (multitask), (iii) multimodal hateful meme detection. Each task offers two subtasks with different variations. This repository contains the _dataset_, _format checker, scorer and baselines_ for each task of the [MAHED2025](https://marsadlab.github.io/mahed2025/).



- [Task 1: Text-based Hate and Hope Speech Classification](task1)

  Classify Arabic text as hate, hope, or not_applicable.


- [Task 2: Emotion, Offensive Language, and Hate Detection](task2)

  Multimodal Hate Speech Detection in Memes

- [Task 3: Emotion, Offensive Language, and Hate Detection](task2)

  Detect whether a meme (text + image) is hateful or not.

# Licensing

Please check the task-specific directory for the licensing of the respective dataset.

# Credits

**Lab Organizers:** Please find on the task website: https://marsadlab.github.io/mahed2025

# Contact
<!-- Slack Channel: [join](https://join.slack.com/t/araieval/shared_invite/zt-20rzypxs7-LuHUsw8ltj7ylae9c4I7XQ) <br>
Email: [araieval@googlegroups.com](araieval@googlegroups.com) -->

# Citation
TBA
<!-- **The task overview paper must be cited:**

```

``` -->

**Please find relevant papers below that might be useful to read. Associated bib file available [here:bibtex/bibliography.bib](bibtex/bibliography.bib)**

<a id="1">[1]</a> Wajdi Zaghouani, Hamdy Mubarak, and Md. Rafiul Biswas. 2024. So Hateful! Building a Multi-Label Hate Speech Annotated Arabic Dataset. In Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024), pages 15044–15055, Torino, Italia. ELRA and ICCL.
<br>
<a id="1">[2]</a> Alam, F., Biswas, M.R., Shah, U., Zaghouani, W., Mikros, G. (2025). Propaganda to Hate: A Multimodal Analysis of Arabic Memes with Multi-agent LLMs. In: Barhamgi, M., Wang, H., Wang, X. (eds) Web Information Systems Engineering – WISE 2024. WISE 2024. Lecture Notes in Computer Science, vol 15440. Springer, Singapore. https://doi.org/10.1007/978-981-96-0576-7_28
<br>
<a id="1">[3]</a> Firoj Alam, Abul Hasnat, Fatema Ahmad, Md. Arid Hasan, and Maram Hasanain. 2024. ArMeme: Propagandistic Content in Arabic Memes. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 21071–21090, Miami, Florida, USA. Association for Computational Linguistics.
<br>
<a id="2">[4]</a> Maram Hasanain, Fatema Ahmad, and Firoj Alam. 2024. Can GPT-4 Identify Propaganda? Annotation and Detection of Propaganda Spans in News Articles. In Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024), pages 2724–2744, Torino, Italia. ELRA and ICCL.
<br>
<a id="3">[5]</a> Maram Hasanain, Fatema Ahmad, and Firoj Alam. 2024. Large Language Models for Propaganda Span Annotation. In Findings of the Association for Computational Linguistics: EMNLP 2024, pages 14522–14532, Miami, Florida, USA. Association for Computational Linguistics..
<br>

<a id="4">[6]</a> Dimitrov, Dimitar, Firoj Alam, Maram Hasanain, Abul Hasnat, Fabrizio Silvestri, Preslav Nakov, and Giovanni Da San Martino. "SemEval-2024 Task 4: Multilingual Detection of Persuasion Techniques in Memes." In *Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)*, Mexico City, Mexico, June 2024. Association for Computational Linguistics.
<br>
<a id="5">[7]</a> Maram Hasanain, Firoj Alam, Hamdy Mubarak, Samir Abdaljalil, Wajdi Zaghouani, Preslav Nakov, Giovanni Da San Martino, and Abed Alhakim Freihat. 2023. "ArAIEval Shared Task: Persuasion Techniques and Disinformation Detection in Arabic Text." In Proceedings of the First Arabic Natural Language Processing Conference (ArabicNLP 2023), December. Singapore: Association for Computational Linguistics.
<br>
<a id="6">[8]</a> Firoj Alam, Hamdy Mubarak, Wajdi Zaghouani, Giovanni Da San Martino, and Preslav Nakov. 2022. "Overview of the WANLP 2022 Shared Task on Propaganda Detection in Arabic.", In Proceedings of the Seventh Arabic Natural Language Processing Workshop (WANLP), 108–118, December. Abu Dhabi, United Arab Emirates (Hybrid): Association for Computational Linguistics. [https://aclanthology.org/2022.wanlp-1.11](https://aclanthology.org/2022.wanlp-1.11).
<br>

```
@inproceedings{zaghouani-etal-2024-hateful,
    title = "So Hateful! Building a Multi-Label Hate Speech Annotated {A}rabic Dataset",
    author = "Zaghouani, Wajdi  and
      Mubarak, Hamdy  and
      Biswas, Md. Rafiul",
    editor = "Calzolari, Nicoletta  and
      Kan, Min-Yen  and
      Hoste, Veronique  and
      Lenci, Alessandro  and
      Sakti, Sakriani  and
      Xue, Nianwen",
    booktitle = "Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)",
    month = may,
    year = "2024",
    address = "Torino, Italia",
    publisher = "ELRA and ICCL",
    url = "https://aclanthology.org/2024.lrec-main.1308/",
    pages = "15044--15055",  
}
@inproceedings{alam2024propaganda,
  title = {Propaganda to Hate: A Multimodal Analysis of Arabic Memes with Multi-agent LLMs},
  author = {Alam, Firoj and Biswas, Md Rafiul and Shah, Uzair and Zaghouani, Wajdi and Mikros, Georgios},
  booktitle = {International Conference on Web Information Systems Engineering},
  pages = {380--390},
  year = {2024},
  organization = {Springer},
}
@inproceedings{alam-etal-2024-armeme,
    title = "{A}r{M}eme: Propagandistic Content in {A}rabic Memes",
    author = "Alam, Firoj  and
      Hasnat, Abul  and
      Ahmad, Fatema  and
      Hasan, Md. Arid  and
      Hasanain, Maram",
    editor = "Al-Onaizan, Yaser  and
      Bansal, Mohit  and
      Chen, Yun-Nung",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2024",
    address = "Miami, Florida, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.emnlp-main.1173/",
    doi = "10.18653/v1/2024.emnlp-main.1173",
    pages = "21071--21090",    
}

@inproceedings{hasanain-etal-2024-large,
    title = "Large Language Models for Propaganda Span Annotation",
    author = "Hasanain, Maram  and
      Ahmad, Fatema  and
      Alam, Firoj",
    editor = "Al-Onaizan, Yaser  and
      Bansal, Mohit  and
      Chen, Yun-Nung",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2024",
    month = nov,
    year = "2024",
    address = "Miami, Florida, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.findings-emnlp.850/",
    doi = "10.18653/v1/2024.findings-emnlp.850",
    pages = "14522--14532",
}

@inproceedings{hasanain2024can,
  title={Can GPT-4 Identify Propaganda? Annotation and Detection of Propaganda Spans in News Articles},
  author={Hasanain, Maram and Ahmed, Fatema and Alam, Firoj},
  booktitle = "Proceedings of the 2024 Joint International Conference On Computational Linguistics, Language Resources And Evaluation",
  series = "LREC-COLING 2024",
  year={2024},
  address={Torino, Italy}
}

@InProceedings{dimitrov-EtAl:2024:SemEval2024,
  author    = {Dimitrov, Dimitar and Alam, Firoj and Hasanain, Maram and Hasnat, Abul and Silvestri, Fabrizio and Nakov, Preslav and Martino, Giovanni Da San},
  title     = {SemEval-2024 Task 4: Multilingual Detection of Persuasion Techniques in Memes},
  booktitle      = {Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)},
  month          = {June},
  year           = {2024},
  address        = {Mexico City, Mexico},
  publisher      = {Association for Computational Linguistics}
}

@inproceedings{araieval:arabicnlp2023-overview,
    title = "{ArAIEval Shared Task}: Persuasion Techniques and Disinformation Detection in Arabic Text",
    author = "Hasanain, Maram and Alam, Firoj and Mubarak, Hamdy, and Abdaljalil, Samir  and Zaghouani, Wajdi and Nakov, Preslav  and Da San Martino, Giovanni and Freihat, Abed Alhakim",
    booktitle = "Proceedings of the First Arabic Natural Language Processing Conference (ArabicNLP 2023)",
    month = Dec,
    year = "2023",
    address = "Singapore",
    publisher = "Association for Computational Linguistics",
}

@inproceedings{alam-etal-2022-overview,
    title = "Overview of the {WANLP} 2022 Shared Task on Propaganda Detection in {A}rabic",
    author = "Alam, Firoj  and
      Mubarak, Hamdy  and
      Zaghouani, Wajdi  and
      Da San Martino, Giovanni  and
      Nakov, Preslav",
    booktitle = "Proceedings of the The Seventh Arabic Natural Language Processing Workshop (WANLP)",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates (Hybrid)",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.wanlp-1.11",
    pages = "108--118",
}

```

## Additional Resources (Tools/Source code)
We listed the following tools/source code, which might be helpful to run the experiments.
* https://huggingface.co/docs/transformers/en/tasks/image_classification
* https://llava-vl.github.io/
* https://github.com/dsaidgovsg/multimodal-learning-hands-on-tutorial
* https://fasttext.cc/docs/en/supervised-tutorial.html
* https://github.com/facebookresearch/mmf

## Recommended reading
The following papers might be useful. We have not provided exhaustive list. But these could be a good start.<br>
[Download bibliography](bibtex/bibliography.bib)

**Persuasion Techniques Detection**
* Maram Hasanain, Ahmed El-Shangiti, Rabindra Nath Nandi, Preslav Nakov, and Firoj Alam. 2023. **QCRI at SemEval-2023 Task 3: News Genre, Framing and Persuasion Techniques Detection Using Multilingual Models.** In Proceedings of the 17th International Workshop on Semantic Evaluation (SemEval-2023), pages 1237–1244, Toronto, Canada. Association for Computational Linguistics.
* Jakub Piskorski, Nicolas Stefanovitch, Giovanni Da San Martino, and Preslav Nakov. 2023. **SemEval-2023 Task 3: Detecting the Category, the Framing, and the Persuasion Techniques in Online News in a Multi-lingual Setup**. In Proceedings of the The 17th International Workshop on Semantic Evaluation (SemEval-2023), pages 2343–2361, Toronto, Canada. Association for Computational Linguistics.
* Alam, Firoj, Hamdy Mubarak, Wajdi Zaghouani, Giovanni Da San Martino, and Preslav Nakov. **"Overview of the WANLP 2022 Shared Task on Propaganda Detection in Arabic."** In Proceedings of the The Seventh Arabic Natural Language Processing Workshop (WANLP), pp. 108-118. Association for Computational Linguistics, 2022.
* Dimitrov, Dimitar, Bishr Bin Ali, Shaden Shaar, Firoj Alam, Fabrizio Silvestri, Hamed Firooz, Preslav Nakov, and Giovanni Da San Martino **"SemEval-2021 Task 6: Detection of Persuasion Techniques in Texts and Images."** Proceedings of the 15th International Workshop on Semantic Evaluation (SemEval-2021). 2021.
* Da San Martino, Giovanni, Shaden Shaar, Yifan Zhang, Seunghak Yu, Alberto Barrón-Cedeno, and Preslav Nakov. **"Prta: A system to support the analysis of propaganda techniques in the news."** In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics: System Demonstrations, pp. 287-293. 2020.
* Dimitrov, Dimitar, Bishr Bin Ali, Shaden Shaar, Firoj Alam, Fabrizio Silvestri, Hamed Firooz, Preslav Nakov, and Giovanni Da San Martino. **"Detecting Propaganda Techniques in Memes."** In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), pp. 6603-6617. 2021
* Sharma, Shivam, Firoj Alam, Md Shad Akhtar, Dimitar Dimitrov, Giovanni Da San Martino, Hamed Firooz, Alon Halevy, Fabrizio Silvestri, Preslav Nakov, and Tanmoy Chakraborty. **"Detecting and Understanding Harmful Memes: A Survey."** In Proceedings of the Thirty-First International Joint Conference on Artificial Intelligence,{IJCAI} 2022, Vienna, Austria, 23-29 July 2022, pp. 5597-5606. 2022.
* Alam, Firoj, Stefano Cresci, Tanmoy Chakraborty, Fabrizio Silvestri, Dimiter Dimitrov, Giovanni Da San Martino, Shaden Shaar, Hamed Firooz, and Preslav Nakov. **"A Survey on Multimodal Disinformation Detection."** In Proceedings of the 29th International Conference on Computational Linguistics, pp. 6625-6643. 2022.
