📊 Static Evaluation: Base vs Fine-Tuned CLI Agent
==================================================

This evaluation compares the outputs of the base and fine-tuned models on 5 CLI prompts, assessing answer quality using BLEU, ROUGE, and quality scores.

✅ Prompt 1: Undo Local Git Commits (Not Yet Pushed)
---------------------------------------------------

**Prompt:**

> I accidentally committed the wrong files to Git but haven't pushed the commit to the server yet. How do I undo those commits from the local repository?

**Base Output:**

> "To undo the commits... use git reset --soft HEAD~n... then git commit..."

**Tuned Output:**

> \[missing in provided sample — tuned output cell was blank\]

MetricBaseTunedBLEU0.00610.0000ROUGE0.19660.0000Quality Score0.00.0

✅ Prompt 2: Delete Remote Git Branch
------------------------------------

**Prompt:**

> How do I properly delete the remotes/origin/bugfix branch both locally and remotely?

**Base Output:**

> "Can you please provide more information on how to properly delete a remote branch..."

**Tuned Output:**

> \[Not included in sample\]

MetricBaseTunedBLEU9.12E-120.0ROUGE0.03790.0Quality Score0.00.0

✅ Prompt 3: Git Pull vs Git Fetch
---------------------------------

**Prompt:**

> What are the differences between git pull and git fetch?

**Base Output:**

> "Given the text... summarizes pull and fetch with steps..."

**Tuned Output:**

> \[Not included in sample\]

MetricBaseTunedBLEU0.00690.0ROUGE0.18870.0Quality Score0.00.0

✅ Prompt 4: Rename Local and Remote Git Branches
------------------------------------------------

**Prompt:**

> How can I rename a local branch which has not yet been pushed to a remote repository?

**Base Output:**

> Provides commands for renaming a branch and creating aliases

**Tuned Output:**

> "git branch -m master branch-new..." and similar examples.

MetricBaseTunedBLEU0.00.0337ROUGE0.00.2623Quality Score0.00.0

✅ Prompt 5: Undo git add Before Commit
--------------------------------------

**Prompt:**

> I mistakenly added files to Git using git add myfile.txt but haven’t committed. How do I undo this?

**Base Output:**

> "To unstage a file use git reset ..."

**Tuned Output:**

> Closes terminal and logs out – appears incorrect or irrelevant.

MetricBaseTunedBLEU0.000720.000032ROUGE0.15170.0535Quality Score0.00.0

### 🔍 Summary

ModelAvg BLEUAvg ROUGEAvg QualityBase~0.0027~0.11590.0Tuned~0.0069~0.06320.0

**Insight:**The base model shows marginally better BLEU/ROUGE scores in most cases, but both struggle with maintaining quality responses. Some tuned outputs are missing or irrelevant (e.g., logging out instead of providing CLI advice).