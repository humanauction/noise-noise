from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from allauth.account.views import SignupView, LoginView
from .models import GuestSession
import logging

# Create your views here.

logger = logging.getLogger(__name__)


class CustomSignupView(SignupView):
    """Custom signup view with enhanced security"""
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Signup successful!")
        logger.info(f"New user signup: {form.cleaned_data.get('username')}")
        return response


class CustomLoginView(LoginView):
    """Custom login view with session logging"""
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            f'Welcome back, {self.request.user.username}!'
        )
        logger.info(f"User logged in: {self.request.user.username}")
        return response


@method_decorator(csrf_protect, name='dispatch')
class GuestAccessView(TemplateView):
    """Handle guest user access"""

    @require_POST
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Create or get guest session
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key

            guest_session, created = GuestSession.objects.get_or_create(
                session_key=session_key
            )

            if created:
                logger.info(
                    f"New guest session created: {guest_session.guest_token}"
                )
                message = (
                    "Guest access granted! "
                    "Sign up to save your noise preferences."
                )
            else:
                logger.info(
                    (
                        "Existing guest session accessed: "
                        f"{guest_session.guest_token}"
                    )
                )
                message = "Welcome! Sign up to save your noise preferences."

            return JsonResponse({
                'success': True,
                'message': message,
                'guest_token': str(guest_session.guest_token),
                'is_guest': True
            })
        else:
            return JsonResponse({
                'success': True,
                'message': f'Welcome, {request.user.username}!',
                'is_guest': False
            })
