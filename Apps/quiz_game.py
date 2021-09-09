class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n",
    "What color are bananas?\n(a) Yellow\n(b) Purple\n(c) Orange\n",
    "What color are watermelon?\n(a) Red/Green\n(b) Purple\n(c) Orange\n",
    "What color are lemon?\n(a) White\n(b) Yellow\n(c) Green\n",
    "What color are strawberries?\n(a) Red\n(b) Purple\n(c) Magenta\n",
    "What color are kiwi?\n(a) Black\n(b) Green\n(c) Orange\n",
    "What color are dragon fruit?\n(a) Red\n(b) Purple\n(c) Orange\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "a"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "a"),

]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print(f"You got {score}/{len(questions)} correct")


run_test(questions)
