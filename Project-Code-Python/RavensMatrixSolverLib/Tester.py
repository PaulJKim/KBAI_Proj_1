
class Tester:
    def __init__(self):
        pass

    def testPossibleAnswers(self, figures, possibleAnswers):
        for i in range(0, 7):
            self.calculateFigureSimilarityScore(figure[str(i)], possibleAnswers)
            
    def calculateFigureSimilarityScore(self, figure, possibleAnswers):
        similarityScore = 0

        for objectName, objectModel in figure.objects.items():
            if attributeName in potentiallyRelatedObjectModel.attributes:
                similarityScore += self.compareAttributeValues(attributeValue, potentiallyRelatedObjectModel.attributes[attributeName])
        
        return similarityScore
    
    def compareAttributeValues(self, v1, v2):
        if v1 == v2:
            return 1
        else:
            return 0
