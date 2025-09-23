from marshmallow import Schema, fields

class BookSchema(Schema):
    # dump_only : 파이썬 객체를 JSON으로 변환하여 API 응답(response)을 생성할 때만 포함
    # required : 클라이언트로부터 API 요청(예: POST, PUT)을 받을 때, 해당 필드가 필수적으로 포함되어야 함
    seq_no = fields.Int(required=True)
    book_title_nm = fields.String(required=True)
    author_nm = fields.String(required=True)
    publisher_nm = fields.String(required=True)
    book_image_nm = fields.String()
    book_intrcn_cn = fields.String()
    inpt_de = fields.String()
    isbn_thirteen_no = fields.Int()
    rank_co = fields.Int()
    