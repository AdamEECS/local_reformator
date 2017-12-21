from . import MongoModel


class ProductUser(MongoModel):
    @classmethod
    def _fields(cls):
        fields = [
            ('id', int, -1),
            ('uid', int, -1),
            ('role', int, -1),
            ('launch_type', int, -1),
            ('is_master_ori', int, -1),
            ('investor_capital_total', float, -1),
            ('investor_capital_total_init', int, -1),
            ('investor_login', int, -1),
            ('om_equal', int, -1),
            ('nickname', str, ''),
            ('plan_code', str, ''),
            ('create_time', str, ''),
        ]
        fields.extend(super()._fields())
        return fields

    @classmethod
    def new(cls, form=None, **kwargs):
        m = super().new(form)
        m.id = int(form.get('id', -1))
        m.save()
        return m

    @classmethod
    def upsert(cls, form):
        mid = int(form.get('id', -1))
        m = cls.find_one(id=mid)
        if m is None:
            m = cls.new(form)
        else:
            m.update(form)
        return m
