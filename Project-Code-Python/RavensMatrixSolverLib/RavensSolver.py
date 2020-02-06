from RavensMatrixSolverLib.SemanticNetwork import SemanticNetwork
from RavensMatrixSolverLib.Generator import Generator
from RavensMatrixSolverLib.Tester import Tester

class RavensSolver:
    def __init__(self):
        pass

    def SetProblem(self, problem):
        self.problem = problem

    def SolveVerbally(self):

        relationships = {}

        if self.problem.problemType == '2x2':
            semanticNetwork = SemanticNetwork(self.problem.figures)
            relationships = semanticNetwork.Apply()

            generator = Generator()
            possibleAnswers = generator.generatePossibleAnswers(self.problem.figures, relationships)

            tester = Tester()
            answerChoice = tester.testPossibleAnswers(possibleAnswers, self.problem.figures)

            return answerChoice
        
