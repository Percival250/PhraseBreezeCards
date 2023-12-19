from django.shortcuts import redirect


class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return redirect('register')  # Измените 'register' на имя вашей страницы регистрации
        response = self.get_response(request)
        return response
