class CodeReview:
    def __init__(self):
        self.submissions = {}

    def submit_code(self, user, code):
        if user not in self.submissions:
            self.submissions[user] = []
        self.submissions[user].append({'code': code, 'feedback': []})

    def give_feedback(self, user, feedback):
        if user not in self.submissions:
            print("No submission found for this user.")
            return
        print("Submissions:")
        for idx, submission in enumerate(self.submissions[user]):
            print(f"Submission {idx+1}:")
            print(submission['code'])
            print("Feedback:")
            for fb in submission['feedback']:
                print(fb)
            print()
        submission_idx = int(input("Enter the submission number you want to give feedback on: ")) - 1
        self.submissions[user][submission_idx]['feedback'].append(feedback)
        print("Feedback added successfully.")

# Example usage
if __name__ == "__main__":
    code_review = CodeReview()

    # Submitting code
    code_review.submit_code("user1", """
    def greet():
        print("Hello, world!")

    greet()
    """)

    # Giving feedback
    code_review.give_feedback("user1", "Good job on the code structure.")
