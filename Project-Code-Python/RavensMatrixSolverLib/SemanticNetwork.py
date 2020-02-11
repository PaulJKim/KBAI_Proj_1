

from RavensMatrixSolverLib.ObjectRelationship import ObjectRelationship

class SemanticNetwork:

    associations = {'Row1':('A', 'B'), 'Col1':('A', 'C')}
    
    def __init__(self, figures):
        self.figures = figures

    def Apply(self):
        relationshipsByAssociation = {}

        for key, association in self.associations.items():
            relationshipsByAssociation[key] = self.BuildRelationships(association)

        return relationshipsByAssociation

    def BuildRelationships(self, association):
        transformationsByObjectMapping = []

        for objectName, objectModel in self.figures[association[0]].objects.items():

            for relatedObjectName, relatedObjectModel in self.figures[association[1]].objects.items():

                score = self.calculateObjectSimilarityScore(objectModel, relatedObjectModel)

                if score >= 3:
                    #Objects are pretty similar, Identify any transformations if any exist
                    relatedObjectMapping = ObjectRelationship(objectModel, relatedObjectModel)
                    relatedObjectMapping.IdentifyTransformations()
                    transformationsByObjectMapping.append(relatedObjectMapping)

        return transformationsByObjectMapping

    # These methods could go in a library of some sort
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
