import re
import logging

from django.shortcuts import render
from django.contrib import messages

from Base.models import Contact

logger = logging.getLogger(__name__)


def contact(request):
    """Handle the home page and contact form submissions."""
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        content = request.POST.get('content', '').strip()
        number = request.POST.get('number', '').strip()

        # --- Validation ---
        if not name or len(name) < 2 or len(name) > 30:
            messages.error(
                request,
                'Name must be between 2 and 30 characters.'
            )
            return render(request, 'home.html')

        if not email or len(email) < 3 or len(email) > 50:
            messages.error(
                request,
                'Please enter a valid email address (3–50 characters).'
            )
            return render(request, 'home.html')

        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            messages.error(request, 'Please enter a valid email address.')
            return render(request, 'home.html')

        if not number or not number.isdigit() or len(number) < 7 or len(number) > 15:
            messages.error(
                request,
                'Phone number must be 7–15 digits.'
            )
            return render(request, 'home.html')

        if not content or len(content) < 5:
            messages.error(
                request,
                'Message must be at least 5 characters long.'
            )
            return render(request, 'home.html')

        # --- Save to database ---
        Contact.objects.create(
            name=name,
            email=email,
            content=content,
            number=number,
        )
        logger.info("New contact message from %s <%s>", name, email)
        messages.success(
            request,
            'Thank you for reaching out! Your message has been received.'
        )

    return render(request, 'home.html')
