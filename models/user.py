from . import MongoModel
from . import timestamp, time_str


class User(MongoModel):
    @classmethod
    def _fields(cls):
        fields = [
            ('uid', int, -1),
            ('nickname', str, ''),
            ('history', list, []),
        ]
        fields.extend(super()._fields())
        return fields

    @classmethod
    def new(cls, form=None, **kwargs):
        m = super().new(form)
        m.save()
        return m

    @classmethod
    def upsert(cls, form):
        mid = int(form.get('id', -1))
        m = cls.find_one(id=mid)
        if m is None:
            m = cls.new(form)
        else:
            name = form.get('nickname')
            if m.nickname != name:
                m.history.append([m.nickname, time_str(timestamp())])
                m.nickname = name
                m.ut = timestamp()
                m.save()
        return m
