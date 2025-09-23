from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schemas import BookSchema
import pandas as pd
from schemas import BookSchema

blp = Blueprint('books', 'books', url_prefix='/books', description='Operations on books')

# 데이터 저장소
# {'SEQ_NO': 309324494, 'RANK_CO': 886, 'INPT_DE': '2021-12-15', 'ISBN_THIRTEEN_NO': 9788970942551, 'BOOK_TITLE_NM': '딱 맞아 ', 'AUTHR_NM': '송선옥 글·그림', 'BOOK_INTRCN_CN': '딱 맞아 마을의 작고 귀여운 동물들은 각자 딱 맞는 집에서 평화롭게 살아간다. 그런데 덩치가 커다란 공룡 브리또는 몸집보다 작은 집에서 옴짝달싹할 수 없다! 작은 집에서 잠들기 위해 이리저리 자세를 바꿔 보던 공룡 브리또에게 무슨 일이 생겼을까?', 'PUBLISHER_NM': '한림출판사', 'BOOK_IMAGE_NM': 'https://bookthumb-phinf.pstatic.net/cover/147/218/14721849.jpg?type=m1&udate=20190817'}
books = []

# methodView : HTTP 메서드와 동일한 이름의 클래스 메소드에 매핑
@blp.route("/")
class BookList(MethodView):
    @blp.response(200)
    def get(self):
        # 모든 아이템을 반환하는 GET 요청 처리
        return books

    @blp.arguments(BookSchema)
    @blp.response(201, description="Book added")
    def post(self, new_data):
        # 새 아이템을 추가하는 POST 요청 처리
        books.append(new_data)
        return new_data

# 'Book' 클래스 - GET, PUT, DELETE 요청을 처리
@blp.route("/<int:seq_no>")
class Book(MethodView):
    @blp.response(200)
    def get(self, seq_no):
        item = next((item for item in books if item["seq_no"] == seq_no), None)
        if item is None:
            abort(404, message="Book not found")
        return item
    
    # required=True로 설정된 필드라도 PUT 요청에서는 필수가 아니게 만듬.
    # 이 옵션은 기존 자원의 일부만 수정할 때 주로 사용.
    # @blp.arguments(BookSchema)
    @blp.arguments(BookSchema(partial=True))
    @blp.response(200, description="Book updated")
    def put(self, new_data, seq_no):
        # 특정 ID를 가진 아이템을 업데이트하는 PUT 요청 처리
        item = next((item for item in books if item["seq_no"] == seq_no), None)
        if item is None:
            abort(404, message="Book not found")
        item.update(new_data)
        return item

    @blp.response(204, description="Book deleted")
    def delete(self, seq_no):
        # 특정 ID를 가진 아이템을 삭제하는 DELETE 요청 처리
        global books
        if not any(item for item in books if item["seq_no"] == seq_no):
            abort(404, message="Book not found")
        books = [item for item in books if item["seq_no"] != seq_no]
        return ''

def book_csv_list() -> list[dict]:
    ''' 
    booklist return
    '''
    global books
    try:
        df_loaded = pd.read_csv('bookList.csv', encoding='utf-8')
        list_of_dicts = df_loaded.to_dict(orient='records')
        books = list_of_dicts
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
    return books
