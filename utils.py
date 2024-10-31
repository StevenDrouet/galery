from uuid import uuid4

def make_uuid():
    '''
        Description: Returns a UUID V4 for postgres based models
        Parameters:
            None
        Return:
            uuid.UUID
    '''
    return uuid4()