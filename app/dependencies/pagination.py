from fastapi import Query


def pagination_param(
        page:int = Query(
            1,
            ge=1,
            description="Page Number"
        ),
        size:int=Query(
            1,
            ge=1,
            le=20,
            description="items per page")
):
    return {
        "page":page,
        "size":size,
    }