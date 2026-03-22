# Module 04 — Multi-shot Prompting

## Task
Category Tagging (Cricket Headlines)

## Why this is Multi-shot
This prompt provides multiple examples across categories to guide the model before asking it to classify a new headline.

## Prompt
Tag each cricket headline with one label only:
Performance, Injury, Selection, Record, Controversy

Headline: Virat Kohli scores a brilliant century in the third Test match.
Label: Performance

Headline: Jasprit Bumrah ruled out of the series due to a back injury.
Label: Injury

Headline: BCCI announces squad for the upcoming T20 World Cup.
Label: Selection

Headline: Rohit Sharma becomes the highest run-scorer in T20 internationals.
Label: Record

Headline: Match referee penalises team for slow over rate during the final.
Label: Controversy

Headline: Hardik Pandya returns to the squad after recovering from ankle surgery.
Label: Selection

Headline: Shubman Gill hits three consecutive half-centuries in the ODI series.
Label: Performance

Now tag this:
Headline: Ravindra Jadeja breaks the record for most catches by a fielder in Tests.
Label:

## Model Response
Label: Record