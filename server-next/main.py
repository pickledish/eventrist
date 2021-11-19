from datetime import datetime, timedelta

from starlette.applications import Starlette
from starlette.background import BackgroundTask
from starlette.responses import JSONResponse
from starlette.routing import Route

# -----------------------------------------------------------------------------
# Global state! Woohoo
# -----------------------------------------------------------------------------

post_enabled = True
flush_buffer = []
flush_interval = timedelta(seconds=30)
flush_next_time = datetime.now() + flush_interval

# -----------------------------------------------------------------------------
# Background functions
# -----------------------------------------------------------------------------

async def add_to_buffer(request):
    """
    """
    body = await request.json()

    flush_buffer.append(body)

async def flush_if_necessary():
    """
    """
    wait = flush_next_time - datetime.now()

    if wait.days >= 0:
        print(f"Not yet time to flush, {wait.seconds} seconds remaining...")
        return

    post_enabled = False

    print(f"Would flush now! Stuff: {flush_buffer}")

    flush_buffer = []
    flush_next_time = datetime.now() + flush_interval

    post_enabled = True

# -----------------------------------------------------------------------------
# Request handling functions
# -----------------------------------------------------------------------------

async def post(request):
    """
    """
    if not post_enabled:
        raise Exception("Currently flushing, please try again in a moment")

    stream_id = request.path_params['stream_id']

    print(f"Received request to {stream_id}")

    await add_to_buffer(request)

    task = BackgroundTask(flush_if_necessary)

    return JSONResponse({'ok': True}, background=task)

# -----------------------------------------------------------------------------
# Setting up the main service
# -----------------------------------------------------------------------------

routes = [
    Route('/stream/{stream_id}', post, methods=['POST']),
]

app = Starlette(debug=True, routes=routes)
