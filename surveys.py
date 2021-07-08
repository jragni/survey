class Question:
    """Question on a questionnaire."""

    def __init__(self, question, choices=None, allow_text=False):
        """Create question (assume Yes/No for choices).

        question = question text {String}
        choices = list, like ["Yes", "No", "Maybe"] {List[Strings]}
        allow_text = T/F to control free-form textual explanation {Bool}"""

        if not choices:
            choices = ["Yes", "No"]

        self.question = question
        self.choices = choices
        self.allow_text = allow_text  # Comments for the question

    #potential TODO: add a __repr___ for data visualization
    # describing actual question


class Survey:
    """Questionnaire."""

    def __init__(self, title, instructions, questions):
        """Create questionnaire.

        title = title of Survey {string}
        instructions = textual instructions  {string}
        question = list of Question instances: [q1, q2, ...] {list[[Question]]}
        """

        self.title = title
        self.instructions = instructions
        self.questions = questions

#TODO: Focus here
satisfaction_survey = Survey(
    "Customer Satisfaction Survey",
    "Please fill out a survey about your experience with us.",
    [
        Question("Have you shopped here before?"),
        Question("Did someone else shop with you today?"),
        Question("On average, how much do you spend a month on frisbees?",
                 ["Less than $10,000", "$10,000 or more"]),
        Question("Are you likely to shop here again?"),
    ])

personality_quiz = Survey(
    "Rithm Personality Test",
    "Learn more about yourself with our personality quiz!",
    [
        Question("Do you ever dream about code?"),
        Question("Do you ever have nightmares about code?"),
        Question("Do you prefer porcupines or hedgehogs?",
                 ["Porcupines", "Hedgehogs"]),
        Question("Which is the worst function name, and why?",
                 ["do_stuff()", "run_me()", "wtf()"],
                 allow_text=True),
    ]
)

surveys = {
    "satisfaction": satisfaction_survey,
    "personality": personality_quiz,
}
