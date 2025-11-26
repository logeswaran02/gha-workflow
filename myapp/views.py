"""Views for myapp."""
from django.http import JsonResponse, HttpResponse


def home(request):
    """Home page view."""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Django App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            h1 {
                color: #0c4b33;
            }
            .info {
                color: #666;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Simple Django Web App</h1>
            <p>Welcome! This is a simple Django application running in a Docker container.</p>
            <div class="info">
                <p><strong>Endpoints:</strong></p>
                <ul>
                    <li><code>/</code> - This home page</li>
                    <li><code>/health/</code> - Health check endpoint</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)


def health(request):
    """Health check endpoint."""
    return JsonResponse({
        'status': 'healthy',
        'message': 'My new Django app is running successfully'
    })
