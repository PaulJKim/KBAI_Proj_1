FILL = 'Fill'
UNFILL = 'Unfill'
NONE = 'None'

class Generator:

    correspondingRelationshipStartFigure = {'Row1' : 'C', 'Col1' : 'B'}

    def __init__(self):
        pass

    def generatePossibleAnswers(self, figures, relationships):
        possibleAnswers = {}

        for key, startFigure in self.correspondingRelationshipStartFigure.items():

            possibleAnswer = {}
            possibleAnswerName = startFigure + '_' + key
            possibleAnswer['name'] = startFigure + '_' + key

            possibleAnswerObjects = {}
            for relationship in relationships[key]:
                appliedRelationshipResult = self.ApplyRelationshipToStartingFigure(figures[startFigure], relationship)
                possibleAnswerObjects[appliedRelationshipResult['name']] = appliedRelationshipResult
            
            possibleAnswer['objects'] = possibleAnswerObjects
            possibleAnswers[possibleAnswerName] = possibleAnswer

            # This logic is faulty
            # The way we want to generate possible answers is in the same structure as the 
            # models that we're provided here.
            # Right now though, I'm generating answers at the Object level. We need to bundle
            # these possibilities up into one structure.

            # Thinking from the bottom up, I think this means that we should generate all the attribute transformations
            # Collect those into individual objects. Then we can collect those objects and roll them up into a figure.
            # Then at the Tester level, we can just compare the generated figures to all the possible answers and then
            # select the answer that was most similar to either/both.

        return possibleAnswers

    def consolidateAnswer(firstAnswer, secondAnswer):
        pass
                
    # This method should return an object model
    def ApplyRelationshipToStartingFigure(self, startingFigure, relationship):
        correspondingObject = self.findSimilarObjectInFigure(relationship.originalObject, startingFigure)

        transformedAttributes = {}
        for attributeName, attributeValue in correspondingObject.attributes.items():
            transformedAttributes[attributeName] = self.applyTransformActionToAttribute(attributeName, attributeValue, relationship.transformations[attributeName])

        return {'name': 'b_transformed', 'attributes': transformedAttributes}

        # mapObjectsInOriginalToCorrespondingFigure()
        # applyRelationshipsToGenerateAnswer()
    def applyTransformActionToAttribute(self, attributeName, attributeValue, action):
        attributeValueResult = None

        if attributeName == 'fill' and action == FILL:
            attributeValueResult = 'yes'
        elif attributeName == 'fill' and action == UNFILL:
            attributeValueResult = 'no'
        elif attributeName == 'fill' and action == NONE:
            attributeValueResult = attributeValue
        elif attributeName == 'size' and action == NONE:
            attributeValueResult = attributeValue
        elif attributeName == 'shape' and action == NONE:
            attributeValueResult = attributeValue

        return attributeValue


    # These methods could go in a library of some sort and are repeated from SemanticNetwork.py
    def findSimilarObjectInFigure(self, ravensObject, ravensFigure):
        highestSimilarity = 0
        mostSimilarObject = None

        for objectName, objectModel in ravensFigure.objects.items():
            currentSimilarity = self.calculateObjectSimilarityScore(ravensObject, objectModel)

            if currentSimilarity > highestSimilarity:
                highestSimilarity = currentSimilarity
                mostSimilarObject = objectModel

        return mostSimilarObject

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
