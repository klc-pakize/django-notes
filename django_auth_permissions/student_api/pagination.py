from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

#? We will add some information views.py to enable Custom Pagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 15
    page_query_param = "leaf"  # http://127.0.0.1:8000/api/student/?page=1  orginal
                               # http://127.0.0.1:8000/api/student/?leaf=1  custom 

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10  # the number of data to display on the page
    limit_query_param = "total"  # limit = number of data to be displayed on the page
    offset_query_param = "numberofdataattheendofthepage"  # offset= indicates the number of data at the end of the page from the beginning to the location. 
    #? http://127.0.0.1:8000/api/student/?limit=10&offset=20  orginal
    #? http://127.0.0.1:8000/api/student/?numberofdataattheendofthepage=20&total=10 custom

class CustomCursorPagination(CursorPagination):
    cursor_query_param = 'pointer'  # http://127.0.0.1:8000/api/student/?cursor=bz0zMA%3D%3D orginal
                                    # http://127.0.0.1:8000/api/student/?pointer=bz0zMA%3D%3D custom
    page_size = 5  # the number of data to display on the page
    ordering = "number"  # will be sorted by number. If we type -number, it will be sorted in reverse.