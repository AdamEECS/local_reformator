from . import MongoModel


class Product(MongoModel):
    @classmethod
    def _fields(cls):
        fields = [
            ('operation_time', int, 0),
            ('originator_input', int, 0),
            ('remaining_ori_money', int, 0),
            ('plan_code', str, ''),
            ('remaining_money', int, 0),
            ('voter_profit', str, ''),
            ('min_input', int, 0),
            ('originator_login', int, 0),
            ('product_name', str, ''),
            ('manager_login', int, 0),
            ('launch_end', str, ''),
            ('product_type', int, ''),
            ('manager_uid', int, 0),
            ('product_symbol', str, ''),
            ('om_input_ratio', str, ''),
            ('so_line', int, 0),
            ('launch_money', int, 0),
            ('initiator', str, ''),
            ('manager', str, ''),
            ('originator_uid', int, 0),
            ('is_customization', int, 0),
            ('EQUITY', str, ''),
            ('actual_operation', str, ''),
            ('operation_end', str, ''),
            ('operation_start', str, ''),
            ('phase', int, 0),
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
            print(m)
        else:
            m.update(form)
        return m
