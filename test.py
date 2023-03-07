if __name__ == "__main__":
    print("Hello World")
    import spacy
    import spacy_transformers

    print(spacy.__version__)
    nlp = spacy.load("./model")

    # Process whole documents
    text = ("When Sebastian Thrun started working on self-driving cars at "
            "Google in 2007, few people outside of the company took him "
            "seriously. “I can tell you very senior CEOs of major American "
            "car companies would shake my hand and turn away because I wasn’t "
            "worth talking to,” said Thrun, in an interview with Recode earlier "
            "this week.")
    doc = nlp(text)

    print(doc)

    print("Good bye World")