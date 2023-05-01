from voluptuous import Schema, PREVENT_EXTRA

user_schema = Schema(
    {
        "id": int,
        "email": str,
        "first_name": str,
        "last_name": str,
        "avatar": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

list_user_schema = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": [user_schema],
        "support": {
            "url": str,
            "text": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)

resource_schema = Schema(
    {
        "id": int,
        "name": str,
        "year": int,
        "color": str,
        "pantone_value": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

created_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

updated_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

register_schema = Schema(
    {
        "id": int,
        "token": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

