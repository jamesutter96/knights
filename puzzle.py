from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
sentenceA = And(AKnight, AKnave)
knowledge0 = And(
    # each person is either a knight or a knave 
    # importiung the known information
    Or(AKnight, AKnave), Or(BKnight, BKnave), Or(CKnight, CKnave),
    # the person cannot be a knight and a knave 
    Not(And(AKnight, AKnave)), Not(And(BKnight, BKnave)), Not(And(CKnight, CKnave)), 
    # if the person is a knight then according to the rules of the game the sentence is true 
    Biconditional(AKnight, sentenceA)

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
sentenceA = And(AKnave, BKnave)
knowledge1 = And(
    # importiung the known information
    Or(AKnight, AKnave), Or(BKnight, BKnave), Or(CKnight, CKnave),
    # the person cannot be a knight and a knave 
    Not(And(AKnight, AKnave)), Not(And(BKnight, BKnave)), Not(And(CKnight, CKnave)), 
    # if the person is a knight then according to the rules of the game the sentence is true 
    Biconditional(AKnight, sentenceA)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
sentenceA = Or(And(AKnight, BKnight), And(AKnave, BKnave))
sentenceB = Or(And(AKnight, BKnave), And(AKnave, BKnight))
knowledge2 = And(
    # importing known knowledge
    Or(AKnight, AKnave), Or(BKnight, BKnave), Or(CKnight, CKnave),
    # person cannot be both
    Not(And(AKnight, AKnave)), Not(And(BKnight, BKnave)), Not(And(CKnight, CKnave)),
    # biconditional for the sentence 
    Biconditional(AKnight, sentenceA), 
    Biconditional(BKnight, sentenceB) 

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

sentenceA = Biconditional(AKnight, Not(AKnave))
sentenceB = And(Biconditional(AKnave, BKnight), CKnave)
sentenceC = AKnight
knowledge3 = And(
    # importing known knowledge
    Or(AKnight, AKnave), Or(BKnight, BKnave), Or(CKnight, CKnave),
    # person cannot be both
    Not(And(AKnight, AKnave)), Not(And(BKnight, BKnave)), Not(And(CKnight, CKnave)),
    # biconditional statments 
    Biconditional(AKnight, sentenceA), 
    Biconditional(BKnight, sentenceB), 
    Biconditional(CKnight, sentenceC)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
