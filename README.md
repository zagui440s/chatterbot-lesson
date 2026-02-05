# Chatterbots — Lesson Project

https://www.youtube.com/watch?v=Et0iuK68pjU

A minimal lesson project demonstrating a simple chatbot using the ChatterBot library (Python).

## Project layout
- main.py — create, train, and run the chatbot
- README.md
- (optional) corpus/english/custom.yml — add custom corpus files here
- chatbot.sqlite3 — optional persisted database created when configured

## Prerequisites (macOS)
- Python 3.x
- pip
- A virtual environment

## Quick setup
1. Create + activate virtualenv
   - python3 -m venv chatbot-env
   - source chatbot-env/bin/activate
2. Install dependencies
   - pip install chatterbot
   - pip install chatterbot-corpus

## Run the example
- Run once to train and chat:
  - python3 main.py
- Type messages; type `exit` to quit.

Tip: training can take time. Train once and then comment out or remove training calls for normal runs.

## Notes & common error
Error: AttributeError: 'list' object has no attribute 'split'  
Cause: calling ChatterBotCorpusTrainer.train(...) with a Python list. ChatterBotCorpusTrainer expects corpus path strings (e.g. `"chatterbot.corpus.english"`).  
Fix:
- Use ListTrainer for Python lists:
  ```python
  from chatterbot.trainers import ListTrainer
  list_trainer = ListTrainer(chatbot)
  list_trainer.train(["Hi", "Hello"])
  ```
- Use ChatterBotCorpusTrainer for corpus names:
  ```python
  trainer = ChatterBotCorpusTrainer(chatbot)
  trainer.train("chatterbot.corpus.english")
  ```

## Next steps (lesson)
- Create a custom YAML corpus under corpus/english/
- Train offline, then load the DB for interactive usage
