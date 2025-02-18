
### **🐍 script.py**
```python
import statistics

scores = {}
while True:
    subject = input("Enter subject: ")
    score = int(input("Enter score (out of 100): "))
    scores[subject] = score

    if input("Add another? (yes/no): ").lower() != "yes":
        break

avg_score = statistics.mean(scores.values())
weak_subjects = [sub for sub, sc in scores.items() if sc < 60]

print(f"\n📊 Average Score: {avg_score}")
if weak_subjects:
    print(f"⚠️ Focus more on: {', '.join(weak_subjects)}")
