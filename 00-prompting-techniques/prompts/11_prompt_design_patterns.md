# Assignment 11 — Prompt Design Patterns

## Task
Apply 4 prompt design patterns to a cricket academy student feedback note

## Why this is Prompt Design Patterns
The same input text is used across all 4 patterns.
Each pattern gives a completely different output from the same input.
This proves that changing the pattern changes the output, not the input.

## Input Text

Ravi has been training at our cricket academy for the past three months.
His batting technique has improved significantly and he shows great focus during practice.
However, his fielding needs more work, especially in catching high balls.
His fitness levels are average and he should work on building stamina.
Overall, Ravi is a dedicated student and shows good potential for the upcoming trials.

## Pattern 1 — Classification

Prompt:
Classify the overall performance of the student in the following feedback note
as Excellent, Good, Average, or Poor.

Response:
--------------------------------------------------
The overall performance of the student is Good.

Strengths:
- Significant improvement in batting technique
- Great focus during practice
- Dedicated student with good potential

Areas for Improvement:
- Fielding needs more work, especially catching high balls
- Average fitness levels, needs to build stamina

The positive aspects outweigh the areas needing work, indicating a generally
strong and promising performance.

## Pattern 2 — Extraction

Prompt:
Extract the following details from the feedback note.
Return the answer in this format:
- Student Name:
- Strong Areas:
- Areas to Improve:
- Fitness Level:
- Overall Potential:

Response:
--------------------------------------------------
- Student Name: Ravi
- Strong Areas: Batting technique, focus during practice
- Areas to Improve: Fielding (especially catching high balls), building stamina
- Fitness Level: Average (needs work on building stamina)
- Overall Potential: Good potential for the upcoming trials (dedicated student)

## Pattern 3 — Transformation

Prompt:
Rewrite the following student feedback note in a formal tone
suitable for an official academy progress report.

Response:
--------------------------------------------------
Cricket Academy Progress Report

Student: Mr. Ravi
Reporting Period: Past Three Months

Mr. Ravi has demonstrated significant improvement in his batting technique.
He consistently exhibits commendable focus and concentration during practice sessions.

Areas requiring further development have been identified within his fielding skills,
specifically concerning the execution and consistency of high catches.
Dedicated practice in this aspect is recommended.

His current fitness levels are assessed as satisfactory. However, a targeted focus
on enhancing cardiovascular stamina and overall endurance is advisable.

Mr. Ravi is a dedicated and committed student who consistently applies himself to
his training. He exhibits promising potential, making him a strong candidate for
the forthcoming trials.

## Pattern 4 — Generation

Prompt:
Based on the following feedback note, generate a short motivational message
from the coach to encourage the student before the upcoming trials.

Response:
--------------------------------------------------
Hi Ravi, your dedication and improved batting technique over the past three months
have been excellent, and your focus in practice is outstanding.
Trust in your hard work, play with confidence, and remember the great potential you have.
We are all backing you for the trials — go out there and give it your absolute best!

## What Each Pattern Produced from the Same Input

Pattern 1 — Classification : Labelled overall performance as Good with reasoning
Pattern 2 — Extraction     : Pulled structured key details into a clean format
Pattern 3 — Transformation : Rewrote the same content in formal report style
Pattern 4 — Generation     : Created brand new content inspired by the input