# Quiz 052

## Prompt
Create a class that passes the tests in the file `test_quiz053.py`.
## Code Structure

### Python File
```python
#2023-03-03 Quiz052.md
#2023-03-07 Quiz 053
class WordCounter():
    def __init__(self,text):
        self.text = text
        self.word_count = {}
    def count_words(self):
        self.word_count = {}
        for char in self.text:
            if char in ",. ":
                self.text = self.text.replace(char, " ")
        for word in self.text.lower().split():
            if word in self.word_count:
                self.word_count[word] += 1
            else:
                self.word_count[word] = 1
    def get_results(self):
        return self.word_count
```

## Evidence

![](/Assets/Quiz053_Evidence.jpg)
*Fig.1* **Image showing output of program**

