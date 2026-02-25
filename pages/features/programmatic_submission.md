---
layout: two-cols
layoutClass: gap-4
---

# Automated Submission

- Personal API Token (Header: `X-API-Key`) with same access privileges
- REST API (https://scorpion.bi.denbi.de/nfdi/docs)
- Available solutions:
    - <a target="_blank" href="https://github.com/IPK-BIT/scorpion-client">Scorpion Client</a> (SDK)
    - <a target="_blank" href="https://github.com/usadellab/ScorpionSubmission">Scorpion Submission</a> (CLI Tool)

<br>

<AdmonitionType type="caution">
Scorpion Client is still work in progress
</AdmonitionType>

<AdmonitionType type="note">
Thanks to Sebastian Beier for providing ScorpionSubmission
</AdmonitionType>

::right::
<<< @/snippets/scorpion-submission.py py {*|1-12|13-14|15-22|*}
