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

            # This logic is faulty
            # The way we want to generate possible answers is in the same structure as the 
            # models that we're provided here.
            # Right now though, I'm generating answers at the Object level. We need to bundle
            # these possibilities up into one structure.

            # Thinking from the bottom up, I think this means that we should generate all the attribute transformations
            # Collect those into individual objects. Then we can collect those objects and roll them up into a figure.
            # Then at the Tester level, we can just compare the generated figures to all the possible answers and then
            # select the answer that was most similar to either/both.
            
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
