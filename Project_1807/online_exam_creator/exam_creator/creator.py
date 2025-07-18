
question_bank = {}  # { (question_id,): { "question": ..., "options": [...], "answer": ..., "topic": ... } }
topics = set()      # Unique topics

def add_question(qid, question, options, answer, topic):
    key = (qid,)
    if key in question_bank:
        print("Question ID already exists.")
        return
    question_bank[key] = {
        "question": question,
        "options": options,
        "answer": answer,
        "topic": topic
    }
    topics.add(topic)
    print("Question added successfully.")

def get_question(qid):
    return question_bank.get((qid,), "Question not found.")

def get_all_questions():
    return question_bank

def get_topics():
    return topics
