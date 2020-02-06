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
            possibleAnswer['name'] = startFigure + '_' + key

            for objectName, objectModel in figures[startFigure].objects.items():
                objectRelationships = relationships[key]

                possibleAnswer['objects'] = self.applyRelationship(objectRelationships, objectModel)
                answers[name] = self.applyRelationship(objectRelationships, objectModel)
        
        possibleAnswer = {'name' : startFigure + '_' + key, 'attributes': self.applyRelationship(objectRelationships, objectModel)}

        return possibleAnswers
                
    def applyRelationship(self, objectRelationships, objectModel):
        
        answerObjectAttributes = {}

        for ObjectRelationshipModel in objectRelationships:
            for attributeName, action in ObjectRelationshipModel.transformations.items():
                if attributeName == 'fill' and action == FILL:
                    answerObjectAttributes[attributeName] = 'yes'
                elif attributeName == 'fill' and action == UNFILL:
                    answerObjectAttributes[attributeName] = 'no'
                elif attributeName == 'fill' and action == NONE:
                    answerObjectAttributes[attributeName] = objectModel.attributes[attributeName]
                elif attributeName == 'size' and action == NONE:
                    answerObjectAttributes[attributeName] = objectModel.attributes[attributeName]
                elif attributeName == 'shape' and action == NONE:
                    answerObjectAttributes[attributeName] = objectModel.attributes[attributeName]

        return answerObjectAttributes

        # mapObjectsInOriginalToCorrespondingFigure()
        # applyRelationshipsToGenerateAnswer()
