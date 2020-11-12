from src.app.schemas.pagination import PaginationSchema

def paginator(query, page: int, limit: int) -> PaginationSchema:
  result = query.offset(page).limit(limit).all()
  total = query.order_by(None).count()
  return PaginationSchema(page=page, limit=limit, items=result, total=total)