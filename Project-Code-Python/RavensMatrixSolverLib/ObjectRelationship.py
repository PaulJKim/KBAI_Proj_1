
FILL = 'Fill'
UNFILL = 'Unfill'
NONE = 'None'

class ObjectRelationship:
    def __init__(self, originalObject, relatedObject):
        self.originalObject = originalObject
        self.relatedObject = relatedObject

    def IdentifyTransformations(self):
        
        transformations = {}

        for attributeName in self.originalObject.attributes:
            transformations[attributeName] = self.determineChange(attributeName, self.originalObject.attributes, self.relatedObject.attributes)
    
        self.transformations = transformations

    def determineChange(self, attributeName, attributes, relatedAttributes):
        attributeValue = attributes[attributeName]
        relatedAttributeValue = relatedAttributes[attributeName]

        if attributeName == 'fill':
            if attributeValue == relatedAttributeValue:
                return NONE
            if attributeValue == 'yes' and relatedAttributeValue == 'no':
                return UNFILL
            elif attributeValue == 'no' and relatedAttributes == 'yes':
                return FILL
        elif attributeName == 'size':
            if attributeValue == relatedAttributeValue:
                return NONE
        elif attributeName == 'shape':
            return NONE
