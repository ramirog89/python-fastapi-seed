from src.schemas.pagination import PaginationSchema


def paginator(query, page: int, limit: int) -> PaginationSchema:
    '''
        paginator util function is a utility used by the Repositories and consumes a
        model query session and add offset and limit to the current query and
        and creates a PaginationSchema with the current resut
        @query: Model session query
        @page: number
        @limit: number
        @return: PaginationSechma { page: 1, limit: 10, total: 5, item: [{ ...item1 }, { ...item2 }, ...] }
    '''
    result = query.offset(page).limit(limit).all()
    total = query.order_by(None).count()
    return PaginationSchema(page=page, limit=limit, items=result, total=total)
