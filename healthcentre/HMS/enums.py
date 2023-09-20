from enum import Enum
class maritalStatus(Enum):
    SINGLE =     'S', 'SINGLE'
    MARRIED =    'M', 'MARRIED'

class bloodGroup(Enum):
        A_PLUS =     'A+'
        A_MINUS =    'A-'
        B_PLUS =     'B+'
        B_MINUS =    'B-'
        O_PLUS =     'O+'
        O_MINUS =    'O-'
        AB_PLUS =     'AB+'
        AB_MINUS  =     'AB-'
        UNKNOWN = 'UNKNOWN'

class Genotypes(Enum):
        AA =    'AA'
        AC =   'AC'
        AS =   'AS'
        CC =    'CC'
        SC =     'SC'
        SS =      'SS'
        UNKNOWN =  'UNKNOWN'

class sexChoices(Enum):
        MALE =   'Male'
        FEMALE = 'Female'
        OTHERS = 'prefer not to say',
        
        
class titleStatus(Enum):
        MR = 'mr', 
        MISS = 'miss'
        MRS = 'mrs'
        DR =  'dr'
    
class Kins(Enum):
        COUSIN = 'cousin'
        SPOUSE =  'spouse'
        PARENT = 'parent'
        SISTER = 'sister'
        BROTHER = 'brother'
        GUARDIAN = 'guardian'
        
class Kind(Enum):

        UNDERGRADUATE = 'Undergraduate'
        GRADUATE =    'Graduate'
        ACADEMIC= 'Academic Staff'
        NON_ACADEMIC = 'Non-academic Staff'
        VISITOR = 'Visitor'
        UNKNOWN = 'Unknown'