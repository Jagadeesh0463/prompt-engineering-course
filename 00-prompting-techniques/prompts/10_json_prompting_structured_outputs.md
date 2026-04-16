# Assignment 10 — JSON Prompting for Structured Outputs

## Task
Book Recommendations for a Beginner who wants to learn Artificial Intelligence

## Why this is JSON Prompting
The model is instructed to return only valid JSON with a clearly defined structure.
No extra text, no markdown, no code fences.
The output is directly parsed by Python using json.loads() without any cleanup.

## Prompt

Generate book recommendations for a beginner who wants to learn about Artificial Intelligence.
Return only valid JSON.
Do not include markdown.
Do not include code fences.
Do not add any explanation before or after the JSON.

Use this exact structure:
{
  "topic": "string",
  "audience": "string",
  "total_books": 0,
  "books": [
    {
      "rank": 1,
      "title": "string",
      "author": "string",
      "genre": "string",
      "why_read": "string",
      "difficulty": "Beginner | Intermediate | Advanced",
      "estimated_read_days": 0
    }
  ]
}

Rules:
- Recommend exactly 5 books
- Keep difficulty at Beginner or Intermediate only
- Keep why_read to one simple sentence
- Make sure estimated_read_days is a realistic number
- Focus only on AI-related books suitable for a first-time learner

## Raw Response

Raw Response:
--------------------------------------------------
{
  "topic": "Artificial Intelligence",
  "audience": "Beginner interested in AI",
  "total_books": 5,
  "books": [
    {
      "rank": 1,
      "title": "Life 3.0: Being Human in the Age of Artificial Intelligence",
      "author": "Max Tegmark",
      "genre": "Popular Science, Future Studies",
      "why_read": "This book provides a broad overview of AI's potential future and its profound implications for humanity.",
      "difficulty": "Beginner",
      "estimated_read_days": 7
    },
    {
      "rank": 2,
      "title": "AI 2041: Ten Visions for Our Future",
      "author": "Kai-Fu Lee, Chen Qiufan",
      "genre": "Science Fiction, Future Studies",
      "why_read": "Explore plausible future scenarios where AI dramatically impacts daily life through engaging short stories.",
      "difficulty": "Beginner",
      "estimated_read_days": 6
    },
    {
      "rank": 3,
      "title": "The Master Algorithm: How the Quest for the Ultimate Learning Machine Will Remake Our World",
      "author": "Pedro Domingos",
      "genre": "Non-fiction, Machine Learning",
      "why_read": "Gain an accessible understanding of the core concepts behind various machine learning algorithms that power AI.",
      "difficulty": "Intermediate",
      "estimated_read_days": 8
    },
    {
      "rank": 4,
      "title": "Artificial Intelligence: A Guide for Thinking Humans",
      "author": "Melanie Mitchell",
      "genre": "Non-fiction, Introductory",
      "why_read": "This book offers a balanced and comprehensive introduction to the history, capabilities, and limitations of AI.",
      "difficulty": "Intermediate",
      "estimated_read_days": 9
    },
    {
      "rank": 5,
      "title": "You Look Like a Thing and I Love You: How AI Works and Why It's Making the World a Weirder Place",
      "author": "Janelle Shane",
      "genre": "Humorous Non-fiction, Popular Science",
      "why_read": "Discover the often amusing and surprising ways AI works by understanding its limitations through real-world examples.",
      "difficulty": "Beginner",
      "estimated_read_days": 5
    }
  ]
}

## Parsed JSON

Parsed JSON:
--------------------------------------------------
{
  "topic": "Artificial Intelligence",
  "audience": "Beginner interested in AI",
  "total_books": 5,
  "books": [
    {
      "rank": 1,
      "title": "Life 3.0: Being Human in the Age of Artificial Intelligence",
      "author": "Max Tegmark",
      "genre": "Popular Science, Future Studies",
      "why_read": "This book provides a broad overview of AI's potential future and its profound implications for humanity.",
      "difficulty": "Beginner",
      "estimated_read_days": 7
    },
    {
      "rank": 2,
      "title": "AI 2041: Ten Visions for Our Future",
      "author": "Kai-Fu Lee, Chen Qiufan",
      "genre": "Science Fiction, Future Studies",
      "why_read": "Explore plausible future scenarios where AI dramatically impacts daily life through engaging short stories.",
      "difficulty": "Beginner",
      "estimated_read_days": 6
    },
    {
      "rank": 3,
      "title": "The Master Algorithm: How the Quest for the Ultimate Learning Machine Will Remake Our World",
      "author": "Pedro Domingos",
      "genre": "Non-fiction, Machine Learning",
      "why_read": "Gain an accessible understanding of the core concepts behind various machine learning algorithms that power AI.",
      "difficulty": "Intermediate",
      "estimated_read_days": 8
    },
    {
      "rank": 4,
      "title": "Artificial Intelligence: A Guide for Thinking Humans",
      "author": "Melanie Mitchell",
      "genre": "Non-fiction, Introductory",
      "why_read": "This book offers a balanced and comprehensive introduction to the history, capabilities, and limitations of AI.",
      "difficulty": "Intermediate",
      "estimated_read_days": 9
    },
    {
      "rank": 5,
      "title": "You Look Like a Thing and I Love You: How AI Works and Why It's Making the World a Weirder Place",
      "author": "Janelle Shane",
      "genre": "Humorous Non-fiction, Popular Science",
      "why_read": "Discover the often amusing and surprising ways AI works by understanding its limitations through real-world examples.",
      "difficulty": "Beginner",
      "estimated_read_days": 5
    }
  ]
}