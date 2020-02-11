from RavensObject import RavensObject
from RavensMatrixSolverLib.PossibleAnswerModel import PossibleAnswerModel

class Tester:
    def __init__(self):
        pass

    def testPossibleAnswers(self, figures, possibleAnswers):
        currentHighestIndex = 1
        currentHighestScore = 0

        for i in range(1, 7):
            for possibleAnswerFigureName, possibleAnswerFigure in possibleAnswers.items():
                score = self.identifyExistingSimilarObjectScore(figures[str(i)], possibleAnswerFigure)

                if score > currentHighestScore:
                    currentHighestIndex = i
                    currentHighestScore = score
        
        return currentHighestIndex
            
    def identifyExistingSimilarObjectScore(self, figure, possibleAnswerFigure):
        overallScore = 0

        for possibleAnswerObjectName, possibleAnswerObjectDict in possibleAnswerFigure['objects'].items():
            possibleAnswerObjectModel = PossibleAnswerModel(possibleAnswerObjectName, possibleAnswerObjectDict['attributes'])
            # Will probably have to use my own model for this part.
            # Train of thought here is to use the method below to iterate through every object
            # in the figure in question. Compare these objects with the object in the possible answer
            # we have right now. Either see if we find a match or calculate some sort of score somehow.
            # Leverage this to determine the best answer

            overallScore += self.findSimilarObjectInFigure(possibleAnswerObjectModel, figure)

        return overallScore
    
     # These methods could go in a library of some sort and are repeated from SemanticNetwork.py
    def findSimilarObjectInFigure(self, ravensObject, ravensFigure):
        highestSimilarity = 0
        mostSimilarObject = None

        for objectName, objectModel in ravensFigure.objects.items():
            currentSimilarity = self.calculateObjectSimilarityScore(ravensObject, objectModel)

            if currentSimilarity > highestSimilarity:
                highestSimilarity = currentSimilarity
                mostSimilarObject = objectModel

        return highestSimilarity

    def calculateObjectSimilarityScore(self, objectModel, potentiallyRelatedObjectModel):
        similarityScore = 0

        for attributeName, attributeValue in objectModel.attributes.items():
            if attributeName in potentiallyRelatedObjectModel.attributes:
                similarityScore += self.compareAttributeValues(attributeValue, potentiallyRelatedObjectModel.attributes[attributeName])
        
        return similarityScore
    
    def compareAttributeValues(self, v1, v2):
        if v1 == v2:
            return 1
        else:
            return 0
