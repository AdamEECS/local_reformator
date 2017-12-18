from . import MongoModel


class User(MongoModel):
    @classmethod
    def _fields(cls):
        fields = [

        ]
        fields.extend(super()._fields())
        return fields
