from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

async def post(request):
    """
    """
    stream_id = request.path_params['stream_id']

    print(f"Received request to {stream_id}")

    body = await request.json()

    print(f"Request contents: {body}")

    return JSONResponse({'hello': 'world'})

routes = [
    Route('/stream/{stream_id}', post, methods=['POST']),
]

app = Starlette(debug=True, routes=routes)
