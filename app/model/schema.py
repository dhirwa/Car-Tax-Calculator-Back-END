from marshmallow import Schema,fields

class Cars_Schema(Schema):
    cr_id = fields.Integer(dump_only = True)
    cr_brand = fields.String()
    cr_mark = fields.String()
    cr_engine = fields.String()
    cr_drive = fields.String()
    cr_year = fields.Integer()
    cr_newprice = fields.Integer()
    cr_body = fields.String()
    cr_category=fields.String()

cr_schema = Cars_Schema()
crs_schema = Cars_Schema(many = True)
