

volume  = '1'
id = '1932-2545'
name = 'kovacs julianna' 
sex  = 'n'
date_of_birth = '1932-06-25'
    
    

class Record:
    def __init__(self, volume, id1, name, sex,  date_of_birth):
        self._volume = volume
        self._id1= id1
        self._name=name
        self._sex = sex
        self._date_of_birth  = date_of_birth
    @property
    def volume(self):
        return self._volume
    
    @volume.setter
    def set_volume(self, value):
        self._volume = value
    
    @property
    def id1(self):
        return self._id1
    
    @id1.setter
    def set_id1(self, value):
        self._id1= value

    @property
    def name(self):
        return self._name
    
    @name.setter
    def set_name(self, value):
        self._name= value
        
    
    @property
    def sex(self):
        return self._sex
    
    @sex.setter
    def set_sex(self, value):
        self._sex= value
    
    @property
    def date_of_birth(self):
        return self._sex
    
    @date_of_birth.setter
    def set_date_of_birth(self, value):
        self._date_of_birth= value







new_record = Record(volume, id, name, sex, date_of_birth)

volume  = '3'
id = '1932-2545'
name = 'toth janos' 
sex  = 'f'
date_of_birth = '1932-06-25'

ano_new = Record(volume, id, name, sex, date_of_birth)




new_record.set_volume = ano_new.volume


